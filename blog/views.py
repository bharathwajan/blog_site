from django.shortcuts import render
from .models import blog,comments,short_intro,experts_team_bio, supporters,users,cordinators_team_bio,tech_team,website_about,supporters_non_teaching
from django.core.mail import send_mail,EmailMultiAlternatives
from django.views.generic import ListView,DetailView
from .forms import commentform
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string,get_template
import datetime
import pytz


# Create your views here.
def homepage(request):
    blogs=blog.objects.all().order_by('-id')   #  - before column name mean descending order without - mean ascending
    intro=short_intro.objects.all()
    form=commentform
    form_class= commentform
    #reference = request.POST.get('blog')
    #print('hey babe i am here',reference)

    if request.method=='POST':
        form=form(request.POST)
        
        if form.is_valid():
            form.save()
            #messages.success(request,'comment added successfully')
            return redirect('/homepage')

    return render(request,'index.html',{'blogs':blogs,'intro':intro,'form':form,}  )   #this render function accepts only one dictionary

def blog_post(request):
    blogs=blog.objects.filter(id=1) 
    return render(request,'blog-post.html',{'blogs':blogs})

def hct(request):
    intro=short_intro.objects.all()
    admins=cordinators_team_bio.objects.all().order_by('id') 
    return render(request, 'hct.html',{'intro':intro,'admins':admins})

def about_site(request):
    intro=short_intro.objects.all()
    admins=website_about.objects.all().order_by('id')
    return render(request,'about_site.html',{'intro':intro,'admins':admins})

def tt(request):
    intro=short_intro.objects.all()
    admins=tech_team.objects.all().order_by('id') 
    return render(request, 'tt.html',{'intro':intro,'admins':admins})

def aboutme(request):
    intro=short_intro.objects.all()
    admins=experts_team_bio.objects.all().order_by('id')
    return render(request, 'about.html',{'intro':intro,'admins':admins})

def supporter_detail(request):
    intro=short_intro.objects.all()
    admins=supporters.objects.all().order_by('id')
    supporter=supporters_non_teaching.objects.all().order_by('id')
    return render(request, 'supporters.html',{'intro':intro,'admins':admins,'supporters':supporter})

def commenter(request):
    if request.method=="POST":
        blogs=blog.objects.all().order_by('-id')   #  - before column name mean descending order without - mean ascending
        intro=short_intro.objects.all()
        objects=request.POST
        print(objects)
        print(objects['name'])
        print(objects['comment'])
        print(objects['blog_id'])
        return render(request,'index.html',{'blogs':blogs,'intro':intro}  )
    else:
        print('wtf')

def commenter_final(request):
    form=commentform
    return render(request,'',{'form':form })

def subscribers(request):  # This method is used to save users to save to database
    recipient = request.POST.get('semail1')
    #print('reciptent is',recipient)
    #print(type(recipient))
    temp_receiptent=list(enumerate(recipient))
    for index,words in temp_receiptent:
        if words=="@":
            marking=index
    correctmail=recipient[marking:]
    if correctmail=="@gmail.com": #condition only allows to enter only gmail id
        if users.objects.filter(email=recipient).exists() == True:
            messages.success(request,'hurrah ! you are already subscribed')
            return redirect('/homepage')
            return render(request, 'index.html')

        else:
            to_db = users.objects.create(email=recipient) 
            subject, from_email, to = 'welcome to our community',settings.EMAIL_HOST_USER, recipient
            text_content="thank_you_for_subscribing"
            html_content = render_to_string('welcome.html',{ 'email':recipient })  
            msg = EmailMultiAlternatives(subject, text_content,from_email,[to])
            msg.attach_alternative(html_content, "text/html") 
            msg.send()
            messages.success(request,'Thank you for subscribing')
            return redirect('/homepage')
            return render(request, 'index.html')
    else :
        messages.success(request,'please enter a valid email id')
        return redirect('/homepage')
        return render(request, 'index.html')

    
    

def comment_action(request):
    name=request.POST.get('name')
    content=request.POST.get('content')
    objid=request.POST.get('objid')
    to_db=comments.objects.create(name=name,content=content,post_id=objid)
    print(name,content,objid)
    return redirect('/homepage')
    return render(request, 'index.html')
