from django.contrib import admin
from django.contrib import sessions
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from jobs.views import view_job
from candidates.views import view_candidate
from applications.views import applications_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/<int:id>/', view_job),
    path('candidate/<int:id>/', view_candidate),
    path('applications', applications_list_view),
    path('accounts/', include('django.contrib.auth.urls')),
] + staticfiles_urlpatterns()
