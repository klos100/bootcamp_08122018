from Mathematics.views import do_math
from django.urls import path

urlpatterns = [

    path('maths/<operation>/<int:a>/<int:b>', do_math)
]
