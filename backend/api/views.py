# Import necessary modules
import json
from django.http import JsonResponse

# Define a Django view to handle API requests
def api_home(request, *args, **kwargs):
    """
    This view handles incoming HTTP requests and returns a JSON response
    including request data, headers, and content type.
    """

    # Step 1: Get the raw request body (usually JSON sent via POST/PUT)
    body = request.body  # This is a byte string
    
    # Step 2: Try to parse the JSON body into a Python dictionary
    data = {}
    try:
        data = json.loads(body)  # Convert JSON byte string to Python dict
    except:
        # If there's an error in JSON parsing, ignore it
        pass

    # Step 3: Print parsed data to the console for debugging
    print(data)

    # Step 4: Add the request headers to the response data
    # request.headers is a case-insensitive mapping of HTTP headers
    data['headers'] = dict(request.headers)

    # Step 5: Add content type (e.g., 'application/json', 'text/html') to the response
    data['content_type'] = request.content_type

    # Step 6: Return the full data as a JSON response to the client
    return JsonResponse(data)

    print("API HOME VIEW CALLED")


