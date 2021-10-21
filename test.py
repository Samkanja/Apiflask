import requests

BASE = ' http://127.0.0.1:5000/'

data = [{"likes":70,'name':'joe', 'views':100000},
        {"likes":1050,'name':'how to make REST API', 'views':10000},
        {"likes":10,'name':'Tim', 'views':50000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())
input()
response = requests.get(BASE + 'video/6')
print(response.json())