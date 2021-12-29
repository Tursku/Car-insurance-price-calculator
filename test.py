import urllib
import urllib2

name =  "name field"
data = {
        "name" : name 
       }

encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("http://www.abc.com/messages.php?action=send",
        encoded_data)
print (content.readlines())