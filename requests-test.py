import requests

ID = 'daperry'

url = 'https://sites-uat.ualberta.ca/~'

req = requests.get(url+ID)

print ID + " | " + str(req.status_code) + " | " + req.headers['content-type']
