from django.http import JsonResponse

def api_home(request , *args ,  **kwargs):
    return  JsonResponse({"message": "Hii there this is your django json response !!"})



