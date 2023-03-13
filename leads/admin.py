from django.contrib import admin


from .models import Lead, Agent, User, UserProfile, Category, AreaCode, FollowUp

class LeadAdmin(admin.ModelAdmin):

    list_display = ['first_name','last_name', 'image']
    # list_display_links = ['first_name','last_name', 'image']
    list_editable = ['last_name']
    list_filter = ('first_name',)
    search_fields = ['first_name','last_name']
    list_editable = ['image']

class AgnetAdmin(admin.ModelAdmin):

    list_display = ('user','organization', 'image',)



class AreaCodeAdmin(admin.ModelAdmin):
    
    list_display = ['area_code', 'country']
    list_display_links = ['area_code', 'country']
    # list_filter = ('category__name',)
    search_fields = ['country']
    

admin.site.register(Lead, LeadAdmin)
admin.site.register(User)
admin.site.register(Agent, AgnetAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(FollowUp)
admin.site.register(AreaCode, AreaCodeAdmin)

