from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.homepage,name='home'),
    path('blog-post.html',views.blog_post,name='fullview'),
    path('about.html',views.aboutme,name='aboutme'),
    path('homepage',views.homepage,name='home'),
    path('commenter',views.commenter,name='commente'),
    path('subscribers',views.subscribers,name='sub'),
    path('hct',views.hct,name='hct'),  #hct stands for health coordinators team
    path('website_about',views.about_site,name='about_site'), #het stands for health experts team
    path('tt',views.tt,name='tt'), #tt stands for the tech team
    path('supporter_detail',views.supporter_detail,name='sd'),
    path('comment_action',views.comment_action,name='comment_action')
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)