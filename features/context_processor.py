from .models import *
from django.template.context_processors import request


def custom_data(request):


    if SchoolSetup.objects.all().exists():
        setup = SchoolSetup.objects.all().order_by('-created')
        data = setup[0]
        return {'data': data}
    else:
        data=None
        return {'data': data}
  

