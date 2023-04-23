from django.urls import path
from . import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static  


urlpatterns = [
    path("", views.home, name="home"),
    path('about_us/', views.about_us, name="about_us"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog_details/<slug:slug>', views.blog_details, name="blog_details"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('team/', views.team, name="team"),
    path('gallery/', views.gallery, name="gallery"),
    path('notice/', views.notice, name="notice"),
    path('gallery_single/<int:id>', views.gallery_single, name="gallery_single"),
    
    path('results/', views.results, name="results"),
    path('searched_results/', views.searched_results, name="searched_results"),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)