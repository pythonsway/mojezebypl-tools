from django.contrib import admin

from .models import Label, Translation

# titles
admin.site.site_header = "MojeZeby.pl-Tools backend"
admin.site.site_title = "MojeZeby.pl Administrator site backend"
admin.site.index_title = "Welcome to MojeZeby.pl-Tools"


# Menu
admin.site.register(Label)
admin.site.register(Translation)
