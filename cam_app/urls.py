from django.urls import path
from .views import camera_feed_page,camera_hls_view,CameraFeedProxy

urlpatterns = [
    # path('camera-feed/', camera_feed_proxy, name='camera_feed'),
    path('camera-feed/', CameraFeedProxy.as_view(), name='camera_feed'),
    path('camera/', camera_feed_page, name='camera_feed_page'),
    path('camera-hls/', camera_hls_view, name='camera_hls_view'),
]
