from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .models import *


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
    about = AboutContent.objects.filter()[:1].get()
    testimonial = Testimonial.objects.all()
    team = TeamMember.objects.all()
    faq = Faqs.objects.all()
    home = HomeContent.objects.filter()[:1].get()
    context = {
            'testimonial':testimonial,
            'home':home,
            'about':about,
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

        Contact.objects.create(name=name, email=email, subject=subject, message=message,contact=contact)

        return redirect('contact_us')
    else:
        return render(request,'contact_us.html')


def team(request):
    home = HomeContent.objects.filter()[:1].get()
    team = TeamMember.objects.all()
    faq = Faqs.objects.all()

    context = {
        'team':team,
        'home':home,
        'faq':faq,
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