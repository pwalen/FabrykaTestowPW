import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
print(response.status_code)
print(response.text)

print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')

data = {'title':'Python Requests','body':'Requests are awesome','userId':1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data)
print(response.status_code)
print(response.text)

print('\n=  =  =  =  =  =  =  =  =  =  =  =  =  =  =\n')


print(response.content)           # To print response bytes
print(response.text)              # To print unicode response string
jsonRes = response.json()         # To get response dictionary as JSON
print(jsonRes['title'] , jsonRes['body'], sep = ' : ')  # output: Python Requests : Requests are awesome