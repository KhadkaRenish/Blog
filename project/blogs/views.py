from django.shortcuts import render,redirect

from blogs.models import Aboutus,Contact


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    post = Aboutus.objects.first()  # Assuming you want to get the first post
    return render(request, 'about.html', {'post': post})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #print(name, email, phone, subject, message)
        query = Contact(fullname=name, email=email, phone=phone, subject=subject, message=message)
        query.save()
        return redirect('/contact')

    return render(request,'contact.html')

def blog_finance(request):
    return render(request,'blog_finance.html')