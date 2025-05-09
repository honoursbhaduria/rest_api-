import requests 


# endpoint = "https://www.httpbin.org/status/200"

# endpoint  = "https://www.httpbin.org"

endpoint = " http://127.0.0.1:8000/"

get_response = requests.get(endpoint, json={"query": "hello world"})



#  this is a simple example of how to use the requests library in python



print(get_response.text)

#  to print the response code
 #aplication programming interface4

 # phone ->  camera -> app -> api -> CAMERA 

#  REST API'S ia a web api 

# http request is used in this 
# http request -> http response

# http response -> HTML 
# rest api http request -> json (XML)



# _________________this are required this response code __________________-
# 200 - OK
# 201 - Created
# 204 - No Content
# 301 - Moved Permanently
# 400 - Bad Request
# 401 - Unauthorized
# 403 - Forbidden
# 404 - Not Found
# 500 - Internal Server Error
# 503 - Service Unavailable
# 504 - Gateway Timeout
# 200 - OK  

print(f"Response Code: {get_response.status_code}")

