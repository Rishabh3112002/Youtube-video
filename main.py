import webbrowser
from requests_html import HTMLSession
url = 'https://www.youtube.com/c/KalleHallden/videos'
session = HTMLSession()
r = session.get(url)
r.html.render(sleep=1)
article = r.html.find('h3')

newslist = []
for item in article:
    try:
        newsitem = item.find('h3', first = True)
        title = newsitem.text
        link = newsitem.absolute_links
        break
    except:
        pass

links = list(link).pop()
with open ("currentnew.txt", "r") as myfile:
    data=myfile.readlines()

if title==data[0]:
    print('No New Video Avaliable')
else:
    print('New Video Avaliable: ',title)
    print(links)
    with open('currentnew.txt', "w") as myfile:
        myfile.write(title)

print("Type 'y' to see the latest video and 'n' if you dont want to see")
str = input()
if str=='y' or str=='Y':
    webbrowser.open(links)
else:
    print('Thank you for using this application')
