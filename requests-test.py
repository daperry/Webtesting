import requests

with open('ids2test.txt','r') as handle:
    for line in handle:
        req = requests.get(''.join(['https://sites-uat.ualberta.ca/~',line.rstrip()]))
        print line.rstrip() + " | " + str(req.status_code) + " | " + req.headers['content-type']
