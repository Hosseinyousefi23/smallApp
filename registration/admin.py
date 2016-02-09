from django.contrib import admin

# Register your models here.
from user.models import Person, Studentity, Role, Portfolio, SuperInstitution, University, Department, Tag

admin.site.register(Person)
admin.site.register(Studentity)
admin.site.register(Portfolio)
admin.site.register(Role)
admin.site.register(SuperInstitution)
admin.site.register(Department)
admin.site.register(University)
admin.site.register(Tag)




