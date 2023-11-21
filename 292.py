import urllib.request as ur
s = ur.urlopen("http://www.google.com")
sl = s.read()
print(sl)
