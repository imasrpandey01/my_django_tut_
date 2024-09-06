from django.contrib import admin
from django.urls import path
from myapp0 import views

urlpatterns=[path('admin/', admin.site.urls),
             path('greets/',views.greets),
             path('morning_wish/',views.morning_wish),
             path('evening_wish/',views.evening_wish),
             path('template_view/',views.template_view),
             path('view_data_db/',views.view_data_db),
              path('view_data_db_text/',views.view_data_db_text),
             
             ]