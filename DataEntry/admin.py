from django.contrib import admin
from .models import Question, Choice, Breath_Collection, Blood_Collection, Participant, lab_processing, Exposure2, testParticipant, UserAccounts, inclusion, Mandatory_questionaire, Mandatory_questionaire_c, Mandatory_questionaire_de, Mandatory_questionaire_fg, Exposure, Exposure3, lab_processing, ct_scan, biological_relatives_with_cancer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']

class Blood_Collection_Admin(admin.ModelAdmin):
    model = Blood_Collection
    list_display = [field.name for field in Blood_Collection._meta.fields]
"""     fieldsets = [
        (None, {'fields': ['ideal_participant_num']}),
        ('Date information', {'fields': ['date_of_birth']}),
        ('Visit Type', {'fields': ['visit_type']}),
        ('Comments', {'fields': ['comments']}),
        ('Date of Collection', {'fields': ['date_of_collection']}),
        ('Collected By', {'fields': ['collected_by']}),
        ('Time Collected', {'fields': ['time_collected']}),
        ('Processing Start Time', {'fields': ['processing_start_time']}),
        ('Time Placed in Freezer', {'fields': ['time_placed_freezer']}),
        ('Freezer Box Number', {'fields': ['freezer_box_num']}),
        ('Yellow Plasma Barcode 1', {'fields': ['y_plasma_barcode_1']}),
        ('Yellow Plasma Barcode 2', {'fields': ['y_plasma_barcode_2']}),
        ('Pink Plasma Barcode 1', {'fields': ['p_plasma_barcode_1']}),
        ('Pink Plasma Barcode 2', {'fields': ['p_plasma_barcode_2']}),
        ('Red RBC Barcode 1', {'fields': ['r_rbc_barcode_1']}),
        ('Red RBC Barcode 2', {'fields': ['r_rbc_barcode_2']}),
        ('Yellow Bottom Barcode 1', {'fields': ['y_bottom_barcode_1']}),
        ('Yellow Bottom Barcode 2', {'fields': ['y_bottom_barcode_2']}),
        ('Pink Bottom Barcode 1', {'fields': ['p_bottom_barcode_1']}),
        ('Pink Bottom Barcode 2', {'fields': ['p_bottom_barcode_2']}),

    ] """

class Breath_collection_Admin(admin.ModelAdmin):
    model = Breath_Collection
    list_display = [field.name for field in Breath_Collection._meta.fields]
"""     fieldsets = [
        (None, {'fields': ['collection_date']}),
        ('Collection Time', {'fields': ['collection_time']}),
        ('Collected By', {'fields': ['collected_by']}),
    ] """

class Participant_Admin(admin.ModelAdmin):
    model = Participant
    list_display = [field.name for field in Participant._meta.fields]
"""     fieldsets = [
        (None, {'fields': ['ideal_participant_num']}), 
        ('Date of Birth', {'fields': ['date_of_birth']}),
        ('Visit Type', {'fields': ['visit_type']}),
        ('Comments', {'fields': ['comments']}),
    ] """

class lab_processing_Admin(admin.ModelAdmin):
    model = lab_processing
    list_display = [field.name for field in lab_processing._meta.fields]
"""     fieldsets = [
        (None, {'fields': ['ideal_participant_num']}),
        ('Date of Collection', {'fields': ['date_of_collection']}),
        ('Collected By', {'fields': ['collected_by']}),
        ('Time Collected', {'fields': ['time_collected']}),
        ('Processing Start Time', {'fields': ['processing_start_time']}),
        ('Time Placed in Freezer', {'fields': ['time_placed_freezer']}),
        ('Freezer Box Number', {'fields': ['freezer_box_num']}),
        ('Yellow Plasma Barcode 1', {'fields': ['y_plasma_barcode_1']}),
        ('Yellow Plasma Barcode 2', {'fields': ['y_plasma_barcode_2']}),
        ('Pink Plasma Barcode 1', {'fields': ['p_plasma_barcode_1']}),
        ('Pink Plasma Barcode 2', {'fields': ['p_plasma_barcode_2']}),
        ('Red RBC Barcode 1', {'fields': ['r_rbc_barcode_1']}),
        ('Red RBC Barcode 2', {'fields': ['r_rbc_barcode_2']}),
        ('Yellow Bottom Barcode 1', {'fields': ['y_bottom_barcode_1']}),
        ('Yellow Bottom Barcode 2', {'fields': ['y_bottom_barcode_2']}),
        ('Pink Bottom Barcode 1', {'fields': ['p_bottom_barcode_1']}),
        ('Pink Bottom Barcode 2', {'fields': ['p_bottom_barcode_2']}),
    ] """



admin.site.register(Question, QuestionAdmin)
admin.site.register(Blood_Collection, Blood_Collection_Admin)
admin.site.register(Breath_Collection, Breath_collection_Admin)
admin.site.register(Participant, Participant_Admin)
admin.site.register(lab_processing, lab_processing_Admin)
admin.site.register(Exposure2)
admin.site.register(testParticipant)
admin.site.register(UserAccounts)
admin.site.register(inclusion)
admin.site.register(Mandatory_questionaire)
admin.site.register(Mandatory_questionaire_c)
admin.site.register(Mandatory_questionaire_de)
admin.site.register(Mandatory_questionaire_fg)
admin.site.register(Exposure)
admin.site.register(Exposure3)
admin.site.register(ct_scan)
admin.site.register(biological_relatives_with_cancer)
