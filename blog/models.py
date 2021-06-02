from collections import defaultdict
from django.db import models
import os
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string,get_template #get_template has no use in the code even though i added for server purposes





class blog(models.Model):
    title = models.CharField(max_length=100,blank=True)
    first_img = models.ImageField(upload_to='pics',blank=True,help_text="This image will be displayed on the start of the paragraph")
    paragraph = models.TextField(blank=True,help_text="Dont use any paragraph field if you want to put meme or video else it may cause error")
    inter_img = models.ImageField(upload_to='pics',blank=True,help_text="This image will be displayed on the middle of the paragraph")
    paragraph2=models.TextField(blank=True)
    final_img = models.ImageField(upload_to='pics',blank=True,help_text="This image will be displayed on the end of the paragraph")
    final_paragraph=models.TextField(blank=True)
    

    meme=models.ImageField(upload_to= 'pics',blank=True)
    meme_description=models.TextField(blank=True,help_text="This will be the description of the meme on the page")
    
    
    posted_on = models.DateTimeField(auto_now_add=True)
    video=models.FileField(upload_to='vdo',blank=True)
    video_description=models.TextField(blank=True,help_text="This will be the description of your video on the page")
    blogger_name = models.ForeignKey(User, models.CASCADE)  

def save_post(sender,instance,**kwargs):
    obj = blog
    latest = obj.objects.latest('posted_on')
    title = str(latest.title)
    blogger_name=str(latest.blogger_name)
    date=str(latest.posted_on)
   
    
    subs=users
    subscribers=subs.objects.values_list('email') #gets all the subscribers list from database as a query set
    subscribers=list(subscribers)
    subscribers_new = []
    for t in subscribers:
        for x in t:
            subscribers_new.append(x)
    recipient = subscribers_new
    
    subject, from_email, to = 'New post on apothecary-re.com',settings.EMAIL_HOST_USER, recipient
    text_content=f'check out the new post on {title}' 
    html_content = render_to_string('mail.html',{ 'title':title , 'blogger_name':blogger_name , 'date':date})    
    msg = EmailMultiAlternatives(subject, text_content,from_email,bcc=recipient)
    msg.attach_alternative(html_content, "text/html") 
    msg.send()
  

post_save.connect(save_post,sender=blog)

class comments(models.Model):
    name=models.CharField(max_length=255)
    content=models.TextField()
    post=models.ForeignKey(blog,related_name="comments",on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
class short_intro(models.Model):
    profile_pic = models.ImageField(upload_to='pics',blank=True)
    content=models.TextField()

class experts_team_bio(models.Model):
    name=models.CharField(max_length=40,default="admin",blank=False)
    male = 'male'
    female = 'female'
    other = 'other'
    gender = [
    (male, 'Male'),
    (female, 'female'),
    (other, 'other'),
    ]
    gender = models.CharField(max_length=20,choices=gender,default=male) 
    #phone=PhoneField(blank=True, help_text='Contact phone number')
    picture=models.ImageField(upload_to='pics',default='default.png',blank=True)
    bio=models.TextField(help_text='upload atleast seven lines to get proper alignment')

class users(models.Model):
    email=models.EmailField(max_length=254)

class website_about(models.Model):
    paragraph = models.TextField(blank=True,help_text="this text will be dispalyed in about our websites tab")

class cordinators_team_bio(models.Model):
    name=models.CharField(max_length=40,default="admin",blank=False)
    male = 'male'
    female = 'female'
    other = 'other'
    gender = [
    (male, 'Male'),
    (female, 'female'),
    (other, 'other'),
    ]
    gender = models.CharField(max_length=20,choices=gender,default=male) 
    #phone=PhoneField(blank=True, help_text='Contact phone number')
    picture=models.ImageField(upload_to='pics',default='default.png',blank=True)
    bio=models.TextField(help_text='upload atleast seven lines to get proper alignment')


class supporters(models.Model):
    name=models.CharField(max_length=40,default="admin",blank=False)
    male = 'male'
    female = 'female'
    other = 'other'
    gender = [
    (male, 'Male'),
    (female, 'female'),
    (other, 'other'),
    ]
    gender = models.CharField(max_length=20,choices=gender,default=male) 
    #phone=PhoneField(blank=True, help_text='Contact phone number')
    picture=models.ImageField(upload_to='pics',default='default.png',blank=True)
    bio=models.TextField(help_text='upload atleast seven lines to get proper alignment')

   
class tech_team(models.Model):
    name=models.CharField(max_length=40,default="admin",blank=False)
    male = 'male'
    female = 'female'
    other = 'other'
    gender = [
    (male, 'Male'),
    (female, 'female'),
    (other, 'other'),
    ]
    gender = models.CharField(max_length=20,choices=gender,default=male) 
    #phone=PhoneField(blank=True, help_text='Contact phone number')
    picture=models.ImageField(upload_to='pics',default='default.png',blank=True)
    bio=models.TextField(help_text='upload atleast seven lines to get proper alignment')

class supporters_non_teaching(models.Model):
    name=models.CharField(max_length=40,default="admin",blank=False)
    picture=models.ImageField(upload_to='pics',default='default.png',blank=True)

