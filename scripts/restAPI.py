import requests

r = requests.get('https://fabrykatestow.pl')

print(r)

print('\n===========\n')

post = requests.post('http://httpbin.org/post')
put = requests.put('http://httpbin.org/put')
delete = requests.delete('http://httpbin.org/delete')

print(post)
print(put)
print(delete)

print('\n===========\n')

parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)

print(r.url)
print((r.iter_content()))
print(r.cookies)
print(r.text)
print(r.encoding)
print(requests.get('https://fabrykatestow.pl', params=parameters).links)