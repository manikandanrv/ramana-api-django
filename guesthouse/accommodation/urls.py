from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accommodation import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('devotees/',
        views.DevoteeList.as_view(),
        name='devotee-list'),
    path('devotees/<int:pk>/',
        views.DevoteeDetail.as_view(),
        name='devotee-detail'),
    path('rooms/',
        views.RoomList.as_view(),
        name='room-list'),
    path('rooms/<int:pk>/',
        views.RoomDetail.as_view(),
        name='room-detail'),
    path('requests/',
        views.RequestList.as_view(),
        name='request-list'),
    path('requests/<int:pk>/',
        views.RequestDetail.as_view(),
        name='request-detail'),
    path('checkins/',
        views.CheckinList.as_view(),
        name='checkin-list'),
    path('checkins/<int:pk>/',
        views.CheckinDetail.as_view(),
        name='checkin-detail'),
    # path('devotees/<int:pk>/highlight/',
    #     views.SnippetHighlight.as_view(),
    #     name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])