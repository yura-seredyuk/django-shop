"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include('shop.urls', namespace='shop')),
    # url(r'^cart/', include('cart.urls', namespace='cart')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    # url(r'^account/', include('account.urls')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




