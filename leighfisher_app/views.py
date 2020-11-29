from django.shortcuts import render
from django.views.generic import View, TemplateView
from . import mailHandler
from . import models


class About(TemplateView):
    template_name = "about.html"


class Index(TemplateView):
    template_name = "index.html"

class Contact(TemplateView):
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        subject = form.get('subject')
        message = form.get('message')


        new_contact = models.Contact.objects.create(
                name = name,
                email = email,
                subject = subject,
                message=message,

            )

        new_contact.save()
        mailHandler.sendMailToContactPerson(name, email)
        mailHandler.sendMailToLeighfisherContact(name, email, subject, message)





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
    
class Power_Venture(TemplateView):
    template_name = "Power Venture.html"


class Reality(TemplateView):
    template_name = "Reality.html"


class Solar(TemplateView):
    template_name = "Solar.html"


class Startups_ass(TemplateView):
    template_name = "Startups_ass.html"


class Tourism(TemplateView):
    template_name = "Tourism.html"


class trust_funding(TemplateView):
    template_name = "trust funding.html"


class Logistics(TemplateView):
    template_name = "Logistics.html"


class InternationalTrading(TemplateView):
    template_name = "InternationalTrading.html"


class Con_infra(TemplateView):
    template_name = "Con_infra.html"


class Business_adv(TemplateView):
    template_name = "Business_adv.html"


class Engg_serv(TemplateView):
    template_name = "Engg_serv.html"
