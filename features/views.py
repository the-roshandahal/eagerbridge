from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .models import *
# from django.db.models import Q
# from django.contrib import messages, auth


def home(request):
    testimonial = Testimonial.objects.all()
    gallery = Gallery.objects.all()
    blogs = Blog.objects.all()
    if HomeContent.objects.all().exists():
        home = HomeContent.objects.filter()[:1].get()

        context = {
            'home':home,
            'testimonial':testimonial,
            'gallery':gallery,
            'blogs':blogs
        }
    else:
        context = {
            'testimonial':testimonial,
            'gallery':gallery,
            'blogs':blogs
        }
    return render(request,'index.html',context)



def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blogs.html',context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
        'blog':blog
    }
    return render(request,'blog_single.html',context)


def about_us(request):
    home = HomeContent.objects.filter()[:1].get()
    testimonial = Testimonial.objects.all()
    team = TeamMember.objects.all()
    member = BoardMember.objects.all()
    faq = Faqs.objects.all()
    context = {
            'testimonial':testimonial,
            'home':home,
            'member':member,
            'team':team,
            'faq':faq,
        }
    return render(request,'about_us.html',context)


def contact_us(request):
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        Contact.objects.create(
            name=name, email=email, subject=subject, message=message,contact=contact
        )
        return redirect('contact_us')
    else:
        return render(request,'contact_us.html')


def team(request):
    home = HomeContent.objects.filter()[:1].get()
    team = TeamMember.objects.all()
    member = BoardMember.objects.all()
    faq = Faqs.objects.all()

    if Message.objects.all():
        message = Message.objects.filter()[:1].get()
    else:
        message=None
    context = {
        'team':team,
        'member':member,
        'home':home,
        'message':message,
        'faq':faq
    }
    return render(request,'team.html',context)