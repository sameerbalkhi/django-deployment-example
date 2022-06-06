from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request,'first_app/index.html',context = date_dict)

def forms_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form':form })
