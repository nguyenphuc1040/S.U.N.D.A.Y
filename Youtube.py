import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query=" : input("Type search query and hit enter: ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
#print("http://www.youtube.com/watch?v=" + search_results[-1])

import webbrowser
for i in search_results:
    webbrowser.open("https://www.youtube.com/"+search_results[i])