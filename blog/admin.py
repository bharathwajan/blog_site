from django.contrib import admin
from .models import blog,comments,short_intro,experts_team_bio,users,website_about,cordinators_team_bio,tech_team,supporters,supporters_non_teaching
# Register your models here.
admin.site.register(blog)
admin.site.register(comments)
admin.site.register(short_intro)
admin.site.register(experts_team_bio)
admin.site.register(users)
admin.site.register(website_about)
admin.site.register(cordinators_team_bio)
admin.site.register(tech_team)
admin.site.register(supporters)
admin.site.register(supporters_non_teaching)