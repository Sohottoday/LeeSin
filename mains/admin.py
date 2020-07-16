from django.contrib import admin
from .models import SkillStack, Recruit, Company, CountIssue, CountRepository
# Register your models here.

class CountIssueAdmin(admin.ModelAdmin):
    list_display= ['shell','date',]
    fields = ('date',)

admin.site.register(SkillStack)
admin.site.register(Recruit)
admin.site.register(Company)
admin.site.register(CountIssue,CountIssueAdmin)
admin.site.register(CountRepository)