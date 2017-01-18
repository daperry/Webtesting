import httplib, urllib, urllib2
conn = httplib.HTTPConnection("sites-uat.ualberta.ca:443")
conn.request("GET", "/~daperry/")
r1 = conn.getresponse()
print vars(r1)

print r1.status, r1.reason
conn.close()
