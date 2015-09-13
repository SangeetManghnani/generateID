from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Information
from django.core.urlresolvers import reverse
from django.utils import timezone

def index(request):
    return render(request,'easyID/index.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['Fname']
        lname = request.POST['Lname']
        email_id = request.POST['Email']
        contact_no = request.POST['Contact']
        add = request.POST['Address']
        pub_date = timezone.now()
        user = Information(first_name = fname, last_name = lname, contact = contact_no, email = email_id, address =add, published_date = pub_date)
        user.save()
        return HttpResponseRedirect(reverse("easyID:generate"))

def generate(request):
    information = Information.objects.latest('published_date')
    context = {'information':information}
    return render_to_response('easyID/generate.html',context)
# Create your views here.
