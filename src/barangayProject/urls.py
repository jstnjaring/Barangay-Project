from django.contrib import admin
from django.urls import path
from announcement import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # announcement.views
    path('save_announcement', views.save_brgy_announcement),
    path('get_announcement', views.get_brgy_announcement),
    path('update_announcement/<_id>',
         views.update_brgy_announcement),
    path('delete_announcement/<_id>',
         views.delete_brgy_announcement)
]
