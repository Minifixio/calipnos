"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from plotter import views as plotter_views
from client import views as client_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', plotter_views.register, name='register'),
    path('admin/', admin.site.urls),
    
    path('', plotter_views.homepage, name='home'),

    path('home/', plotter_views.homepage, name='home'),
    path('results/', plotter_views.results, name='results'),
    path('change-graph-data', plotter_views.change_graph_data, name='change_graph_data'),
    path('change-graph-params', plotter_views.change_graph_params, name='change_graph_params'),
    path('usb-selection/', plotter_views.usb_selection, name='usb_selection'),

    path('client/measures', client_views.measures, name='client'),
    path('upload-binary/', client_views.upload_binary, name='upload_binary'),
    path('get-measures/', client_views.get_measures, name='get_measures'),
    path('delete_measure/<int:measure_id>/', client_views.delete_measure, name='delete_measure'),
    path('download_measure/<int:measure_id>/', client_views.download_measure, name='download_measure'),
]
