import requests, pprint
from time import sleep

f = open('workfile.txt', 'w')
pp = pprint.PrettyPrinter(indent=4,depth=6)

with open('ids2test.txt','r') as handle:
    for line in handle:
        req = requests.get(''.join(['https://sites-uat.ualberta.ca/~',line.rstrip(),'/']))
        # pp.pprint(req.headers)
        print line.rstrip() + " | " + str(req.status_code) + " | " + req.headers['content-type'] +"\n" 
        value=(line.rstrip() + " | " + str(req.status_code) + " | " + req.headers['content-type'] +"\n" )
        f.write(str(value))
        sleep(2)
        
f.close()
