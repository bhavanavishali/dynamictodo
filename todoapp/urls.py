from.import views
from django.urls import path
app_name ="todoproject"
urlpatterns = [

    path('',views.index,name='index'),
    path('cvlistview/',views.Taskview.as_view(),name='cvlistview'),


]
