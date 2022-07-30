import requests

url = 'https://static.xx.fbcdn.net/rsrc.php/yD/r/d4ZIVX-5C-b.ico'
r = requests.get(url, allow_redirects=True)

open('d4ZIVX-5C-b.ico', 'wb').write(r.content)
