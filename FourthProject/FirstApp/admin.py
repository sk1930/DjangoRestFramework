from django.contrib import admin

from FirstApp.models import Car
# or from .models import Car
# Register your models here.

'''
admin.site.register(Car)

this single line is enough all below code is not needed

with below code we can have our own ModelAdmin'''

class CarAdmin(admin.ModelAdmin):
    
    '''fields=['year','brand']
    # earlier it was brand first next year on the UI
    # in fields we can specify our own custom order
    '''

    # we can also group fields using fieldsets
    fieldsets =[('Time Information',{'fields':['year']}),
    ('Car Information',{'fields':['brand']}),]
    # like TimeInformation section will have the fields year,...
    # Car information section will have brand....




admin.site.register(Car,CarAdmin)

