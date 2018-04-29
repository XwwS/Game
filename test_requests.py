import requests

url = 'https://baike.baidu.com/item/Python/407313'
response = requests.get(url)
content = response.text
print (content)