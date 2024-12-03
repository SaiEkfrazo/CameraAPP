# import requests
# from django.http import StreamingHttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from requests.auth import HTTPDigestAuth

# @csrf_exempt
# def camera_feed_proxy(request):
#     CAMERA_URL = "http://192.168.1.32:8080/video"
#     USERNAME = "test"  # replace with your camera's username
#     PASSWORD = "test"  # replace with your camera's password
    
#     try:
#         # Add HTTP Digest Authentication to the request
#         response = requests.get(
#             CAMERA_URL,
#             auth=HTTPDigestAuth(USERNAME, PASSWORD),
#             stream=True,
#             timeout=10
#         )
        
#         # Check if the response contains the correct content type
#         if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("multipart/x-mixed-replace"):
#             # Return the response directly to the client, stream the content as is
#             return StreamingHttpResponse(
#                 response.iter_content(chunk_size=1024),
#                 content_type=response.headers['Content-Type']
#             )
#         elif response.status_code == 200:
#             return JsonResponse({
#                 'error': 'Response is not a video stream',
#                 'headers': dict(response.headers)
#             })
#         else:
#             return JsonResponse({'error': f"Failed with status {response.status_code}"}, status=response.status_code)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse, JsonResponse
from rest_framework import status
import requests
from requests.auth import HTTPDigestAuth

class CameraFeedProxy(APIView):

    def get(self, request, *args, **kwargs):
        CAMERA_URL = "http://192.168.1.32:8080/video"
        USERNAME = "test"  # Replace with your camera's username
        PASSWORD = "test"  # Replace with your camera's password
        
        try:
            # Add HTTP Digest Authentication to the request
            response = requests.get(
                CAMERA_URL,
                auth=HTTPDigestAuth(USERNAME, PASSWORD),
                stream=True,
                timeout=10
            )

            # Check if the response contains the correct content type
            if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("multipart/x-mixed-replace"):
                # Return the response directly to the client, stream the content as is
                return StreamingHttpResponse(
                    response.iter_content(chunk_size=1024),
                    content_type=response.headers['Content-Type']
                )
            elif response.status_code == 200:
                return JsonResponse({
                    'error': 'Response is not a video stream',
                    'headers': dict(response.headers)
                })
            else:
                return JsonResponse({'error': f"Failed with status {response.status_code}"}, status=response.status_code)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


from django.shortcuts import render

def camera_feed_page(request):
    """
    View to render the template displaying the live camera feed.
    """
    return render(request, 'cam_temp.html')


from django.shortcuts import render

def camera_hls_view(request):
    """
    View to render the HLS video stream in a template.
    """
    return render(request, 'camera_hls.html')
