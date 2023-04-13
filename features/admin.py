from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogField(SummernoteModelAdmin):
    summernote_fields = ('blog')
class HomeFields(SummernoteModelAdmin):
    summernote_fields = ('about_content')

class MessageFields(SummernoteModelAdmin):
    summernote_fields = ('message')

admin.site.register(Blog,BlogField)
admin.site.register(SchoolSetup)
admin.site.register(BoardMember)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Faqs)
admin.site.register(Contact)
admin.site.register(Gallery)
# admin.site.register(Message,MessageFields)
admin.site.register(HomeContent,HomeFields)