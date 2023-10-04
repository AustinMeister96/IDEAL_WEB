"""
URL configuration for IDEAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from accounts.views import login_view, logout_view
from DataEntry.views import add_breath_collection, add_participant, index, add_blood_collection, add_lab_processing, add_exposure_form, add_mandatory_questionaire, add_ct_scan, add_mandatory_questionaire_c, add_mandatory_questionaire_de, add_inclusion
from DataEntry.views import list_participants, show_participants, update_mandatory_questionaire, add_mandatory_questionaire, add_exposure_form, add_clinical_procedures,add_protocol_deviations
from django.conf import settings
from django.conf.urls.static import static
from DataEntry.views import  add_lab_processing_with_data, history_page, add_mandatory_questionaire_c_with_id, add_plco_score, add_yearly_update, add_data_test
from DataEntry.views import GeneratePDF, generate_mandatory_questionnaire_pdf, download_pdf


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^DataEntry/", include("DataEntry.urls")),
    re_path("login/$", login_view, name="login"),
    re_path("logout/$", logout_view, name="logout"),
    #re_path("register/$", register_view, name="register"),
    re_path('login/DataEntry/add_lab_processing', add_lab_processing, name='add_lab_processing'),
    re_path(r"^$", index, name="index"),
    re_path(r"^add_participant/$", add_participant, name="add_participant"),
    #re_path(r"^add_breath_collection/$", add_breath_collection, name="add_breath_collection"),
    path('DataEntry/add_breath_collection/<int:participant_id>', add_breath_collection, name='add_breath_collection'),
    #re_path(r"^add_blood_collection/$", add_blood_collection, name="add_blood_collection"),
    path('DataEntry/add_blood_collection/', add_blood_collection, name='add_blood_collection'),
    #re_path(r"^add_lab_processing/$", add_lab_processing, name="add_lab_processing"),
    path('DataEntry/add_lab_processing/', add_lab_processing, name='add_lab_processing'),
    #re_path(r"^add_exposure_form/$", add_exposure_form, name="add_exposure_form"),
    path('DataEntry/add_exposure_form/<int:participant_id>/', add_exposure_form, name='add_exposure_form'),
    path('DataEntry/add_data', add_data_test, name='add_data'),
    #re_path(r"^add_mandatory_questionaire/$", add_mandatory_questionaire, name="add_mandatory_questionaire"),
    path('DataEntry/add_ct_scans/<int:participant_id>/', add_ct_scan, name='add_ct_scan'),
    path('DataEntry/add_mandatory_questionaire/<int:participant_id>/', add_mandatory_questionaire, name='add_mandatory_questionaire'),
    #path('DataEntry/add_mandatory_questionaire_c/<int:participant_id>/', add_mandatory_questionaire_c, name='add_mandatory_questionaire_c'),
    path('DataEntry/add_mandatory_questionaire_c/<int:participant_id>/', add_mandatory_questionaire_c, name='add_mandatory_questionaire_c'),
    path('DataEntry/add_mandatory_questionaire_de/<int:participant_id>/', add_mandatory_questionaire_de, name='add_mandatory_questionaire_de'),
    path('DataEntry/PLCO_score/', add_plco_score, name='add_plco_score'),
    path('DataEntry/add_yearly_update/', add_yearly_update, name='add_yearly_update'),
    #re_path(r"^add_mandatory_questionaire_c/$", add_mandatory_questionaire_c, name="add_mandatory_questionaire_c"),
    #re_path(r"^add_mandatory_questionaire_de/$", add_mandatory_questionaire_de, name="add_mandatory_questionaire_de"),
    path('DataEntry/add_clinical_procedures/', add_clinical_procedures, name='add_clinical_procedures'),
    #re_path(r"^add_inclusion/<id>", add_inclusion, name="add_inclusion"),
    path('DataEntry/add_inclusion/', add_inclusion, name='add_inclusion'),
    path('DataEntry/add_inclusion/<str:participant_num>/', add_inclusion, name='add_inclusion_with_num'),
    re_path('^list_participants/$', list_participants, name="list-participants"),
    re_path('^show_participants/(?P<participant_id>\d+)/$', show_participants, name="show-participants"),
    re_path('^update_mandatory_questionaire/(?P<participant_id>\d+)/$', update_mandatory_questionaire, name="update_mandatory_questionaire"),
    path('DataEntry/add_protocol_deviations', add_protocol_deviations, name='add_protocol_deviations'),
    path('history/', history_page, name='history'),
    path('generate_pdf/', GeneratePDF.as_view(), name='generate_pdf'),
    path('generate_mandatory_questionnaire_pdf/', generate_mandatory_questionnaire_pdf, name='generate_mandatory_questionnaire_pdf'),
    path('download-pdf/', download_pdf, name='download_pdf'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#    re_path(r"^add_inclusion/$", add_inclusion, name="add_inclusion"),