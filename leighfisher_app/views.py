from django.shortcuts import render
from django.views.generic import View, TemplateView

class About(TemplateView):
    template_name = "about.html"


class Index(TemplateView):
    template_name = "index.html"

class Contact(TemplateView):
    template_name = "contact.html"

class Services(TemplateView):
    template_name = "services.html"

class Team(TemplateView):
    template_name = "team.html"

class Portfolio(TemplateView):
    template_name = "portfolio.html"

class Portfolio_details(TemplateView):
    template_name = "portfolio_details.html"

class Pricing(TemplateView):
    template_name = "pricing.html"

class Testimonial(TemplateView):
    template_name = "testimonials.html"

class Blog(TemplateView):
    template_name = "blog.html"
        
