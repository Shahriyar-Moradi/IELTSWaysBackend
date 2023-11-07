from django.contrib import admin

# Register your models here.
from .models import IELTSExam,Book,Test

# Register your models here.
admin.site.register(IELTSExam)
admin.site.register(Book)
admin.site.register(Test)