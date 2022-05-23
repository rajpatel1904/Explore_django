from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    # path("politics/",views.politics_views),
    # path("sports/",views.sports_views),
    # path("finance/",views.finance_views)
    path("<topic>/",views.news_views),
    path("<int:n1>/<int:n2>",views.add_view),

    
]   