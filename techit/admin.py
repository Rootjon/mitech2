from django.contrib import admin
from.models import Testimonial,Demo,Expert,Service,Brand,Award,Appointment,Contact,Banner,Design,Contactus,Post,Comment
# Register your models here.

@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]

@admin.register(Demo)
class DemoModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image'
    ]


@admin.register(Expert)
class ExpertModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','designation','image','social_facebook',
    ]

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display=[
        'image',
    ]

@admin.register(Award)
class AwardModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]

@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email',
    ]

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email',
    ]
    
    
@admin.register(Banner)
class BannerdModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]
    
@admin.register(Design)
class DesignModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image',
    ]
    
    
@admin.register(Contactus)
class ContactusModelAdmin(admin.ModelAdmin):
    list_display=[
        'name','email',
    ]
    
    
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=[
        'title','image','description',
    ]
    
    
@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'body','email'
    ]
    