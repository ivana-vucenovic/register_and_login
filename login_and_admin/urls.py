
from django.urls import path, include

urlpatterns = [
    path('', include('login_and_admin_app.urls'))
]
