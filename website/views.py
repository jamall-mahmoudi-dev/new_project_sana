from django.shortcuts import render
from website.forms import NameForm, PostModelForm
from website.models import Posts
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostModelForm()
    return render(request, 'website/contact.html', {'form': form})

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')


def test(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostModelForm()
        # form = PostModelForm(request.POST)
        # if form.is_valid():
        
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
        #     subject = form.cleaned_data['subject']
        #     message = form.cleaned_data['message']
        #     description = form.cleaned_data['description']
        #     status = form.cleaned_data['status']
            
        #     print(name, email, subject, message, description, status)
        #     obj = Posts()
        #     obj.name = name
        #     obj.email = email
        #     obj.subject = subject
        #     obj.message = message
        #     obj.description = description
        #     obj.status = status
        #     obj.save()
    return render(request, 'website/test.html', {'form': form })

def sana(request):
    return render(request, 'website/sana.html')

def test_do(request):
    return render(request, 'website/test_do.html')

