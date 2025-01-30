from django.contrib import admin
from django.urls import path
from core.views import SearchApiView,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', SearchApiView.as_view()),
    path('', index)
]
