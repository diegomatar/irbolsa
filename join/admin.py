from django.contrib import admin
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Join
    list_display = ('email', 'nome', 'timestamp')
    search_fields = ['email']
    
admin.site.register(Join, JoinAdmin)


