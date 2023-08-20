from django.urls import path

from mypage import views
from mypage.views import MyProfileView, MyLessonView, MyLessonReviewView, MyHelpersView, MyEventView, MyMessageListView, \
    MyMessageDetailView, MyMessageWriteView, MyPayView

app_name = 'mypage'

urlpatterns = [
    path('profile/', MyProfileView.as_view(), name='myprofile'),
    path('lesson/', MyLessonView.as_view(), name='mylesson'),
    path('lesson/<int:page>/', MyLessonView.as_view(), name='mylesson'),
    path('lesson-review/', MyLessonReviewView.as_view(), name='mylesson-review'),
    path('helpers/', MyHelpersView.as_view(), name='myhelpers'),
    path('helpers/<int:page>/', MyHelpersView.as_view(), name='myhelpers'),
    path('event/', MyEventView.as_view(), name='myevent'),
    path('event/<int:page>/', MyEventView.as_view(), name='myevent'),
    path('message-list/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<int:page>', MyMessageListView.as_view(), name='message-list'),
    path('message-detail/', MyMessageDetailView.as_view(), name='message-detail'),
    path('message-write/', MyMessageWriteView.as_view(), name='message-write'),
    path('pay/', MyPayView.as_view(), name='mypay'),
]
