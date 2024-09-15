from django.contrib import admin
from .models import Competitor, Competition, Modality, Attempt

admin.site.register(Competitor)
admin.site.register(Competition)
admin.site.register(Modality)
admin.site.register(Attempt)
