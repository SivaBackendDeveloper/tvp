from django.contrib import admin

from j.models import Member, Activity


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
   list_display=['name','role','mobilenumber']

class ActivityAdmin(admin.ModelAdmin):
   list_display=['date','activity','image','responce']

admin.site.register(Member,MemberAdmin)
admin.site.register(Activity,ActivityAdmin)
