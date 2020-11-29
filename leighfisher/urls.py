"""leighfisher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from leighfisher_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name="index"),
    path('about/', views.About.as_view(),name="about"),
    path('contact/', views.Contact.as_view(),name="contact"),
    path('services/', views.Services.as_view(),name="services"),
    path('portfolio/', views.Portfolio.as_view(),name="portfolio"),
    path('portfolio_details/', views.Portfolio_details.as_view(),name="portfolio_details"),
    path('pricing/', views.Pricing.as_view(),name="pricing"),
    path('team/', views.Team.as_view(),name="team"),
    path('testimonials/', views.Testimonial.as_view(), name="testimonial"),
    path('blogs/', views.Blog.as_view(), name="blog"),
    path('business_adv/', views.Business_adv.as_view(), name="Business_adv"),
    path('power_venture/', views.Power_Venture.as_view(), name="Power_Venture"),
    path('reality/', views.Reality.as_view(), name="Reality"),
    path('solar/', views.Solar.as_view(), name="Solar"),
    path('startups_ass/', views.Startups_ass.as_view(), name="Startups_ass"),
    path('tourism/', views.Tourism.as_view(), name="Tourism"),
    path('trust_funding/', views.trust_funding.as_view(), name="trust_funding"),
    path('logistics/', views.Logistics.as_view(), name="Logistics"),
    path('internationaltrading/', views.InternationalTrading.as_view(),
         name="InternationalTrading"),
    path('con_infra/', views.Con_infra.as_view(), name="Con_infra"),
    path('engg_serv/', views.Engg_serv.as_view(), name="Engg_serv"),
]

