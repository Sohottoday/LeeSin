from django.contrib import admin
from .models import SkillStack, Recruit, Company, CountIssue, CountRepository
# Register your models here.

class CountIssueAdmin(admin.ModelAdmin):
    list_display= [f.name for f in CountIssue._meta.fields]

admin.site.register(SkillStack)
admin.site.register(Recruit)
admin.site.register(Company)
admin.site.register(CountIssue,CountIssueAdmin)
admin.site.register(CountRepository)