from django.contrib import admin
from .models import Competitor, Competition, Lift, Modality, Attempt, UserStaff

admin.site.register(Competitor)
admin.site.register(Competition)
admin.site.register(Modality)
admin.site.register(Attempt)
admin.site.register(Lift)
admin.site.register(UserStaff)

