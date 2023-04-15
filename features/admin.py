from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django.forms import inlineformset_factory
from .forms import GalleryImageForm


# Register your models here.
class BlogField(SummernoteModelAdmin):
    summernote_fields = ('blog')

class HomeFields(SummernoteModelAdmin):
    summernote_fields = ('sub_text','intro_text','message')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False

class AboutFields(SummernoteModelAdmin):
    summernote_fields = ('sub_text','mission','vision')
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


class AddSingle(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        else:
            return True
    def has_delete_permission(self, request, obj=None):
        return False
    
class CompanySetupAdmin(SummernoteModelAdmin):
    summernote_fields = ('terms_and_conditions', 'privacy_policy')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        else:
            return True
        
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(SchoolSetup, CompanySetupAdmin)
admin.site.register(Blog,BlogField)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Faqs)
admin.site.register(Contact)
# admin.site.register(Gallery)
admin.site.register(HomeContent,HomeFields)
admin.site.register(AboutContent,AboutFields)







GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, form=GalleryImageForm, extra=1, can_delete=True)
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    formset = GalleryImageFormSet
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(Gallery, GalleryAdmin)
