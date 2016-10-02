import re
import urllib

url = 'http://www.tutorialspoint.com/'

pattern=re.compile('<img src="([^">]+)"')
a=urllib.urlopen(url)
b=a.read()
a.close()
c=re.findall(pattern,b)
d = open('intpic.txt',"w")
#d.append(c)

for i in c:
	d.write(url + i + '\n')

d.close()
