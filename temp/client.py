import requests as reqs


#response = reqs.get('https://jsonplaceholder.typicode.com/todos/1', timeout=0.50)
#print(response.text)
#jsonRes = response.json()
#print(jsonRes['title'])


#cookie = {'username':'Pavneet'} 
#response = reqs.get('https://postman-echo.com/cookies/set',cookies = cookie)
#print(response.text)

#response = reqs.get('http://github.com/', timeout=0.50, allow_redirects=True)
#response = reqs.get('http://github.com/', timeout=0.50, allow_redirects=False)
# Note: false-szal nem működik
#print(response.text)

url = 'http://localhost:15400'
try: 
    response = reqs.get(url,timeout=3) 
    response.raise_for_status()
    print(response.text)
    # Raise error in case of failure 
except reqs.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except reqs.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except reqs.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except reqs.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr) 
