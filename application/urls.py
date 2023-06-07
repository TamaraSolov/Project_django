from django.urls import path


from .views import CurrentDateView
from .views import IndexView

urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
]


