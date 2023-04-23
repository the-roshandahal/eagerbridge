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
    if request.method == 'POST':
        student = request.POST['student_id']
        student_id = student.lower()
        url = f'http://sms.eagerbridge.edu.np:82/api/external/get-exam-list?student_code={student_id}'
        response = requests.get(url)
        if response.status_code == 200:
            result_data = response.json()
            context = {
                'student_id':student_id,
                'result_data':result_data,
            }
            return render(request, 'result_select_exam.html',context)
        
        elif response.status_code == 422:
            message = f"Student Not Found for student id {student_id}"
            context = {
                'message':message,
            }
            return render(request, 'result.html',context)
        
        else:
            message = f"Student Not Found for student id {student_id}"
            context = {
                'message':message,
            }
            return render(request, 'result_select_exam.html',context)
    else:
        return render(request,'result.html')


def searched_results(request):
    if request.method == 'POST':
        exam_id = request.POST['exam_id']
        student_id = request.POST['student_id']
        url = f'http://sms.eagerbridge.edu.np:82/api/external/get-results?student_code={student_id}&exam_id={exam_id}'
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            print(result)
            message = "Result Published"
            context = {
                'message':message,
                'result':result,
            }
            return render(request, 'final_result.html',context)
        else:
            print(f'Request failed with status code {response.status_code}')
            message = "Result not published yet"
            context = {
                'message':message,
            }
            return render(request, 'final_result.html',context)

    return render(request,'result_data.html')