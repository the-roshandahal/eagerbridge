from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .models import *
import requests

def home(request):
    testimonial = Testimonial.objects.all()
    gallery = Gallery.objects.all()
    blogs = Blog.objects.all()
    slides = Slider.objects.all()
    home = HomeContent.objects.filter()[:1].get()

    context = {
        'slides':slides,
        'home':home,
        'testimonial':testimonial,
        'gallery':gallery,
        'blogs':blogs,
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
    about = AboutContent.objects.filter()[:1].get()
    testimonial = Testimonial.objects.all()
    faq = Faqs.objects.all()
    home = HomeContent.objects.filter()[:1].get()
    context = {
            'testimonial':testimonial,
            'home':home,
            'about':about,
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

        Contact.objects.create(name=name, email=email, subject=subject, message=message,contact=contact)

        return redirect('home')
    else:
        return render(request,'contact_us.html')


def team(request):
    home = HomeContent.objects.filter()[:1].get()
    team = TeamMember.objects.all()

    context = {
        'team':team,
        'home':home,
    }
    return render(request,'team.html',context)


def gallery(request):
    gallery = Gallery.objects.filter(galleryimage__isnull=False).distinct()
    context = {
        'gallery':gallery,
    }
    return render(request,'gallery.html',context)


def gallery_single(request,id):
    gallery = Gallery.objects.get(id=id)
    gallery_name = gallery.title
    gallery_images = GalleryImage.objects.filter(gallery_id=id)
    context = {
        'gallery_name':gallery_name,
        'gallery_images':gallery_images
    }
    return render(request,'gallery_single.html',context)


def notice(request):
    notices = Notice.objects.filter(type='notice')
    events = Notice.objects.filter(type='event')

    context = {
        'notices':notices,
        'events':events
    }
    return render(request,'notice.html',context)


def results(request):
    url = 'http://sms.eagerbridge.edu.np/api/external/get-exam-list?student_code=STD011'
    response = requests.get(url)
    if response.status_code == 200:  
        data = response.json()  
        
    else:
        print(f'Request failed with status code {response.status_code}')

    return render(request,'result.html')