import urllib2

ID = 'daperry'

url = 'https://sites-uat.ualberta.ca/~'

req = urllib2.Request(url+ID)

handler = urllib2.urlopen(req)

print handler.getcode()
