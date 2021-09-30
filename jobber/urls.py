from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name="landingpage" ),
    path('login', views.login_view, name="login" ),
    path('logout', views.logout_view, name="logout"),
    path('singup', views.sing_up, name="sign_up"),
    path('home', views.home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)