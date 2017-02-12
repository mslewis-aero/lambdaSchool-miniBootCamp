import requests

r = requests.get("http://google.com")

output = open('googleResponse.html','w')

output.write(r.text)
