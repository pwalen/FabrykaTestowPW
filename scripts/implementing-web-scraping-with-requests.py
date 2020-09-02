import requests
# import urllib
# import urllib.request
# from urllib.request import urlretrieve
# from urllib.request import urlopen, Request

url = "https://en.wikipedia.org/wiki/Avengers:_Endgame"

req1 = requests.get(url)

print(req1.content)
print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')
print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')
print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')

print(req1.headers)

print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')
print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')
print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')
text_object = req1.text
print(text_object)
