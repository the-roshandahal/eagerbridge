from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class SchoolSetup(models.Model):
    data_set = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="setup_images")
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    linkedin_url = models.URLField(null=True,blank=True)
    youtube_url = models.URLField(null=True,blank=True)
    
    map_url = models.URLField(null=True,blank=True)

    
    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()

    no_of_students = models.IntegerField()
    success_rate = models.FloatField()
    no_of_teachers = models.IntegerField()
    since = models.IntegerField()

    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. School Setup" 


class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_images/board')
    facebook= models.URLField(null=True, blank=True)
    instagram= models.URLField(null=True, blank=True)
    linkedin= models.URLField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "02. Board Members"

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_images/team')
    facebook= models.URLField(null=True, blank=True)
    instagram= models.URLField(null=True, blank=True)
    linkedin= models.URLField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "03. Team Members"


class Testimonial(models.Model):
    name= models.CharField(max_length=200)
    position= models.CharField(max_length=200)
    testimonial= models.TextField()
    image = models.ImageField(upload_to="testimonial_images/", blank=True, null=True)


    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "04. Testimonials"

class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "05. FAQs"

class Blog(models.Model):
    title = models.TextField()
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Blogs" 


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "07. Contact"

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery_images/")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "08. Gallery" 

class HomeContent(models.Model):
    data_set = models.CharField(max_length=200)
    mini_title_text = models.CharField(max_length=150)
    title_text = models.CharField(max_length=150)
    sub_text = models.CharField(max_length=255)

    button_text = models.CharField(max_length=100)
    button_url = models.URLField()
    banner_image = models.ImageField(upload_to="home_images/", null=True, blank=True)
    
    intro_title = models.CharField(max_length=255)
    intro_text = models.TextField()
    intro_image = models.ImageField(upload_to="home_images/", null=True, blank=True)

    message_title = models.CharField(max_length=255)
    message = models.TextField()
    message_image = models.ImageField(upload_to="home_images/", null=True, blank=True)

    no_of_students = models.IntegerField()
    success_rate = models.FloatField()
    no_of_teachers = models.IntegerField()
    since = models.IntegerField()
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "09.Home Page Content" 



class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    team = models.TextField()
    image = models.ImageField(upload_to="team_images/", null=True, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "10. team" 
