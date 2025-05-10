# Import the requests library - it helps us talk to websites/APIs
import requests

# The website address we want to talk to
api_url = "http://127.0.0.1:8000/api/"

# Our question/message to send
our_message = "this is honours how are you doing?"

print("Sending our message to the API...")

try:
    # Step 1: Send our message to the API (like sending a letter)
    response = requests.get(api_url, params={"query": our_message})
    
    # Step 2: Check if the API got our message (status code 200 means success)
    print(f"API responded with code: {response.status_code}")
    
    # Step 3: Try to read the API's reply
    try:
        api_reply = response.json()  # Convert reply to Python dictionary
        message = api_reply.get('message', "The API didn't send a message back")
        print("API says:", message)
    except:
        print("The API sent something we couldn't understand")
        
    # Bonus: Show the raw reply if you're curious
    # print("Full reply:", response.text)
    
except requests.exceptions.ConnectionError:
    print("Oops! Couldn't connect to the API. Is it running?")
except Exception as e:
    print(f"Something went wrong: {e}")

# ----------------------------#
# 📚 REST API CONCEPTS
# ----------------------------#
# API = Application Programming Interface
# Example: Your phone's app uses an API to talk to the phone's camera

# A REST API is a type of web API
# It uses HTTP methods like GET, POST, PUT, DELETE
# HTTP request -> HTTP response
# In REST APIs, the response is usually JSON (can also be XML, etc.)
# Example: REST API HTTP request → JSON response (not HTML)

# ----------------------------#
# ✅ COMMON HTTP RESPONSE status - CODES
# ----------------------------#
# 200 - OK (Request succeeded)
# 201 - Created (Resource created successfully)
# 204 - No Content (Success but no response body)
# 301 - Moved Permanently (URL changed)
# 400 - Bad Request (Invalid data sent)
# 401 - Unauthorized (Login needed)
# 403 - Forbidden (No permission)
# 404 - Not Found (Wrong URL or missing data)
# 500 - Internal Server Error (Server crashed)
# 503 - Service Unavailable (Server down or overloaded)
# 504 - Gateway Timeout (Server not responding in time)
