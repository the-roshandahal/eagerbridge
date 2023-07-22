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
    url = "http://sms.eagerbridge.edu.np:82/api/external/get-level-lists?&tenant_id=dcd7bbdc-47fc-4412-91f9-f8cf8e906f69"
    try:
        response = requests.get(url)
        result_data = response.json()
        levels = result_data['data']['levels']
    except requests.RequestException as e:
        levels = []
    context = {
        'levels':levels,
    }
    return render(request, 'result.html',context)



def select_exam(request):
    if request.method == "POST":
        level_id = request.POST['level_id']
        url = f"http://sms.eagerbridge.edu.np:82/api/external/get-exam-lists-updated?level_id={level_id}&tenant_id=dcd7bbdc-47fc-4412-91f9-f8cf8e906f69"
        try:
            response = requests.get(url)
            result_data = response.json()
            exams = result_data['data']['exams']
        except requests.RequestException as e:
            exams = []
        context = {
            'exams':exams,
            'level_id':level_id,
        }
        return render(request,'select_exam.html',context)
    else:
        return redirect('results')


def select_class(request):
    if request.method == "POST":
        exam_id = request.POST['exam_id']
        url = f"http://sms.eagerbridge.edu.np:82/api/external/get-class-lists?level_id={exam_id}&tenant_id=dcd7bbdc-47fc-4412-91f9-f8cf8e906f69"
        try:
            response = requests.get(url)
            result_data = response.json()
            classes_data = result_data['data']['classes']
            classes = [{'class_id': cls['class_id'], 'class_name': cls['class_name']} for cls in classes_data]
        except requests.RequestException as e:
            classes = []
        context = {
            'classes': classes,
            'exam_id': exam_id,
        }
        return render(request, 'select_class.html', context)

    else:
        return redirect('results')



def select_section(request):
    if request.method == "POST":
        class_id = request.POST['class_id']
        exam_id = request.POST['exam_id']
        url = f"http://sms.eagerbridge.edu.np:82/api/external/get-section-lists?class_id={class_id}&tenant_id=dcd7bbdc-47fc-4412-91f9-f8cf8e906f69"
        try:
            response = requests.get(url)
            result_data = response.json()
            sections = result_data['data']['sections']
        except requests.RequestException as e:
            sections = []
        context = {
            'sections':sections,
            'exam_id':exam_id,
            'class_id':class_id,
        }
        return render(request,'select_section.html',context)
    else:
        return redirect('results')



def searched_results(request):
    if request.method == 'POST':
        exam_id = request.POST['exam_id']
        class_id = request.POST['class_id']

        section_id = request.POST['section_id']
        roll_no = request.POST['roll_no']
        
        url = f'http://sms.eagerbridge.edu.np:82/api/external/get-result-updated?tenant_id=dcd7bbdc-47fc-4412-91f9-f8cf8e906f69&section_id={section_id}&class_id={class_id}&exam_id={exam_id}&roll_no={roll_no}'
        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            message = "Result Published"
            context = {
                'message':message,
                'result':result,
            }
            return render(request, 'final_result.html',context)
        else:
            result = response.json()
            message = result.get('message')
            context = {
                'message':message,
            }
            return render(request, 'final_result.html',context)

