from django.urls import re_path
from . import views
from accounts import views as accounts_views
from accounts.views import login_view, logout_view
from .views import add_lab_processing_with_data, add_ct_scan, add_mandatory_questionaire_c, add_mandatory_questionaire_de, add_inclusion

urlpatterns = [
    # re_path(r'^$', views.index, name='index'),
    # re_path(r'^add_participant/$', views.add_participant, name='add_participant'),
    # re_path(r'^add_breath_collection/$', views.add_breath_collection, name='add_breath_collection'),
    # re_path(r'^add_blood_collection/$', views.add_blood_collection, name='add_blood_collection'),
    # re_path(r'^add_lab_processing/$', views.add_lab_processing, name='add_lab_processing'),
    # re_path(r'^add_exposure_form/$', views.add_exposure_form, name='add_exposure_form'),
    # re_path(r'^add_mandatory_questionaire/$', views.add_mandatory_questionaire, name='add_mandatory_questionaire'),
    # re_path(r'add_lab_processing_with_data/<str:participant_num>/', add_lab_processing_with_data, name='add_lab_processing_with_data'),
    # re_path(r'add_ct_scans/<int:participant_id>/', add_ct_scan, name='add_ct_scan'),
    
    # re_path(r'add_mandatory_questionaire_de/', add_mandatory_questionaire_de, name='add_mandatory_questionaire_de'),
    # re_path(r'add_inclusion/', add_inclusion, name='add_inclusion'),


]
# Compare this snippet from IDEAL\DataEntry\models.py: