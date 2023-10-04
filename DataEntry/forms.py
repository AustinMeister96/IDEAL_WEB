from django import forms
from django.forms import ModelForm, RadioSelect
from .models import Question, Choice,  Blood_Collection, Breath_Collection, lab_processing, Exposure, Exposure2, Exposure3, Mandatory_questionaire, ct_scan, MyForm, CancerHistory, Mandatory_questionaire_c, Mandatory_questionaire_de, Mandatory_questionaire_fg, inclusion, testParticipant, Participant, ct_scan_nodule_1,ct_scan_nodule_2, ct_scan_nodule_3, ct_scan_nodule_4, ct_scan_nodule_5 ,biological_relatives_with_cancer
#-------------------
from django.utils.safestring import mark_safe
from .models import PLCO_score
from django.db.models.signals import post_save
from django.dispatch import receiver


#create a question form
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text','pub_date']

class Blood_Collection_Form(forms.ModelForm):
    class Meta:
        model = Blood_Collection
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={'type': 'date'}),
            'date_of_collection': forms.DateTimeInput(attrs={'type': 'date'}),
            'time_collected': forms.TimeInput(attrs={'type': 'time'}),
            'processing_start_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'time_placed_freezer': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'collected_by': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'visit_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'ideal_participant_num': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'freezer_box_num': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'y_plasma_barcode_1': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'y_plasma_barcode_2': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'p_plasma_barcode_1': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'p_plasma_barcode_2': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'r_rbc_barcode_1': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'r_rbc_barcode_2': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'y_bottom_barcode_1': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'y_bottom_barcode_2': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'p_bottom_barcode_1': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'p_bottom_barcode_2': forms.NumberInput(attrs={'class': 'form-control-sm'}),
        }
class DateInput(forms.DateInput):
    input_type = 'date'


class Breath_Collection_Form(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]
    brush_teeth = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    mouthwash = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    face_cream = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    perfume_cologne = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    deodorant = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    smoke_exposure = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    fuel_car = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    short_of_breath = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    fever = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cough = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    cold = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    no_symptoms = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    halitosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    aborted = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    incomplete = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    declined = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    pneumonia = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    inhaled_medication = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    hrt_menopause = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    menopausal = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    birth_control = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    class Meta:
        model = Breath_Collection
        fields = '__all__'
        widgets = {
            'collection_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'collection_time': forms.TimeInput(attrs={'type': 'date'}),
            'brush_teeth_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'last_meal_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'last_drink_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'collection_start_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'collection_stop_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'collected_by': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'arrival_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'last_meal': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'last_drink': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'notes': forms.TextInput(attrs={'class': 'form-control-lg', 'style': 'height: 100px; width: 100%;'}),
            'reciva_barcode': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'tennax_number': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'collection_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'breathing_rate': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_barcode': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_tennax': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_barcode': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_tennax': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_tennax': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_breathing_rate': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'brush_teeth': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'smoke_exposure': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'fuel_car': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'short_of_breath': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'fever': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'cough': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'cold': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'no_symptoms': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'halitosis': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'aborted': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'incomplete': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'declined': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'volume_collected': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'birth_control': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'birth_control_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'menopausal': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'hrt_menopause': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'grt_menopause_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'gender_affirming_surgery': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'gender_affirming_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'inhaled_medication': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'inhaled_medication_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'inhaled_medication_brand': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'inhaled_medication_name': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'pneumonia': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'smoke_exposure_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_collection_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            'casper_collection_time': forms.TimeInput(attrs={'type': 'datetime-local'}),
            
        }

class Lab_Processing_Form(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]
    reciva_sample_stored = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    reciva_purge = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    reciva_spiked = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    class Meta:
        model = lab_processing
        fields = '__all__'
        widgets = {

            'reciva_collection_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'reciva_collection_site': forms.Select(attrs={'class': 'form-control-sm'}),
            'reciva_ship_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'reciva_received_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'reciva_shipping_method': forms.TextInput(attrs={'class': 'short-entry-box'}),
            'reciva_sample_stored': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reciva_sample_storage_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'reciva_sample_storage_location': forms.TextInput(attrs={'class': 'input-sm'}),
            'reciva_sample_storage_temperature': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_purge_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'reciva_purge_gas_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_purge_gas_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_spiked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reciva_istd_used': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'reciva_istd_vol': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'reciva_istd_applied': forms.Select(attrs={'class': 'form-control-sm'}),
            'reciva_cslr_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'reciva_cslr_gas_flow': forms.NumberInput(attrs={'class': 'short-entry-box'}),
            'reciva_cslr_gas_duration': forms.NumberInput(attrs={'class': 'short-entry-box'}),
            'reciva_sample_run': forms.CheckboxInput(attrs={'class': 'form-check-input-sm'}),
            'reciva_sample_run_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'reciva_sample_run_instrument': forms.Select(attrs={'class': 'form-control-sm'}),
            'reciva_sample_td_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'reciva_sample_ms_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'reciva_sample_filename': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'reciva_sample_file_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'reciva_sample_visual_inspection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reciva_notes': forms.Textarea(attrs={'class': 'form-control-sm'}),
            'room_air_collection_site': forms.Select(attrs={'class': 'form-control-sm'}),
            'room_air_ship_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'room_air_received_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'room_air_shipping_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_stored': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_air_sample_storage_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_storage_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_storage_temperature': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_purge_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'room_air_purge_gas_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_purge_gas_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_spiked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_air_istd_used': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_istd_vol': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_istd_applied': forms.Select(attrs={'class': 'form-control-sm'}),
            'room_air_cslr_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'room_air_cslr_gas_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_cslr_gas_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_run': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_air_sample_run_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_run_instrument': forms.Select(attrs={'class': 'form-control-sm'}),
            'room_air_sample_td_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_ms_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_filename': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_file_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'room_air_sample_visual_inspection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_air_notes': forms.Textarea(attrs={'class': 'form-control-sm'}),
            'casper_collection_site': forms.Select(attrs={'class': 'form-control-sm'}),
            'casper_ship_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'casper_received_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'casper_shipping_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_stored': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casper_sample_storage_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_storage_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_storage_temperature': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_purge_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'casper_purge_gas_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_purge_gas_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_spiked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casper_istd_used': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_istd_vol': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_istd_applied': forms.Select(attrs={'class': 'form-control-sm'}),
            'casper_cslr_gas': forms.Select(attrs={'class': 'form-control-sm'}),
            'casper_cslr_gas_flow': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_cslr_gas_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_run': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casper_sample_run_date': forms.DateTimeInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_run_instrument': forms.Select(attrs={'class': 'form-control-sm'}),
            'casper_sample_td_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_ms_method': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_filename': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_file_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'casper_sample_visual_inspection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casper_notes': forms.Textarea(attrs={'class': 'form-control-sm'}),
        }
    

class BooleanRadioSelect(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        for i, (option_value, option_label) in enumerate(self.choices):
            radio_attrs = self.build_attrs(self.attrs.copy(), attrs)
            radio_attrs['type'] = 'radio'
            radio_attrs['name'] = name
            radio_attrs['value'] = forms.check_test(value, str(option_value))
            if option_value == value:
                radio_attrs['checked'] = True

            label_for = f' id="{attrs["id"]}_{i}"' if 'id' in attrs else ''
            label_attrs = self.build_attrs({'for': f'{attrs["id"]}_{i}'})

            option_label = forms.html.escape(option_label)
            radio = f'<input{self.flatatt(radio_attrs)} />'
            label = f'<label{self.flatatt(label_attrs)}>{option_label}</label>'
            output.append(f'<div>{radio} {label}</div>')

        return mark_safe('\n'.join(output))
    


class Exposure_Form(forms.Form):
    class Meta:
        model = Exposure2
        fields = '__all__'
        widgets = {
            'total_exposure': forms.Select(attrs={'class': 'form-control-sm'}),
            'asbestos_exposure': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'asbestos_exposure_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'asbestos_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'diesel': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'diesel_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'diesel_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radon': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'radon_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radon_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'cadmium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'cadmium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'cadmium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'chromium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'chromium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'chromium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'coal_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'arsenic': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'arsenic_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'arsenic_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'nickel': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'nickel_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'nickel_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'plutonium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'plutonium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'plutonium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'beryllium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'beryllium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'beryllium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'ether': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'ether_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'ether_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'soot': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'soot_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'soot_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'welding': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'welding_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'welding_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radiation': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'radiation_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radiation_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'munitions': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'munitions_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'munitions_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'warfare': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'warfare_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'warfare_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'acheson': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'acheson_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'acheson_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'aluminum': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'aluminum_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'aluminum_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coke': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'coke_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coke_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'mining': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'mining_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'mining_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'iron': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'iron_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'iron_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            
        }


class Exposure_Form2(forms.ModelForm):

    class Meta:
        model = Exposure2
        fields = '__all__'
        widgets = {
            'total_exposure': forms.Select(attrs={'class': 'form-control-sm in-line'}),
            'asbestos_exposure': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'asbestos_exposure_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'asbestos_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'silica_exposure': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'diesel': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'diesel_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'diesel_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radon': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'radon_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radon_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'cadmium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'cadmium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'cadmium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'chromium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'chromium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'chromium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'coal_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'arsenic': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'arsenic_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'arsenic_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'nickel': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'nickel_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'nickel_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'plutonium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'plutonium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'plutonium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'beryllium': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'beryllium_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'beryllium_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'ether': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'ether_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'ether_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'soot': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'soot_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'soot_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'welding': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'welding_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'welding_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radiation': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'radiation_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'radiation_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'munitions': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'munitions_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'munitions_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'warfare': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'warfare_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'warfare_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'acheson': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'acheson_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'acheson_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'aluminum': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'aluminum_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'aluminum_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal_gasification': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'coal_gasification_duration': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coal_gasification_exposure_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'coke': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'coke_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'coke_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sulfur': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'sulfur_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sulfur_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mining': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'mining_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mining_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'iron': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'iron_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'iron_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'painting': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'painting_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'painting_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'rubber': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'rubber_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'rubber_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'burn_pits': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'burn_pits_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'burn_pits_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'oil_fires': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'oil_fires_duration':  forms.TextInput(attrs={'class': 'form-control-sm'}),
            'oil_fires_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sulfur_fires': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'sulfur_fires_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sulfur_fires_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'atsugi': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'atsugi_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'atsugi_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sand_storms': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'sand_storms_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'sand_storms_exposure_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_industry': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_2': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_2_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_2_industry': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_3': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_3_duration': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'job_held_3_industry': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'duration_outdoor_pollution': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'duraiton_indoor_pollution': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_appliances': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'frequency_in_cooking_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'kitchen_range': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'kitchen_range_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_frequency': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_frequency_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_fuel': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_fuel_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_cooking_oil': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_cooking_oil_store': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_cooking_oil_homemade': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_cooking_oil_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_saute_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_fry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_0_20_deepfry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_frequency': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_frequency_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_fuel': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_fuel_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_cooking_oil': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_cooking_oil_store': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_cooking_oil_homemade': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_cooking_oil_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_saute_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_fry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_21_40_deepfry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_frequency': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_frequency_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_fuel': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_fuel_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_cooking_oil': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_cooking_oil_store': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_cooking_oil_homemade': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_cooking_oil_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_saute_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_fry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_41_60_deepfry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_frequency': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_frequency_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_fuel': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_fuel_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_cooking_oil': forms.Select(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_cooking_oil_store': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_cooking_oil_homemade': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_cooking_oil_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_saute_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_fry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cooking_61_above_deepfry_frequency': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'processed_meat_frequency': forms.Select(attrs={'class': 'form-control-sm'}),
            'red_meat_frequency': forms.Select(attrs={'class': 'form-control-sm'}),


        }


# add an exposure3 form class

class Exposure_Form3(ModelForm):
    class Meta:
        model = Exposure3
        fields = '__all__'
        widgets = {
            'home_1_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_1_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            # add the rest of the fields from the exposure3 model
            'home_2_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_province':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_2_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_postal_code':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_3_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_4_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_water_src_other':forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_5_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_start_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_end_yr': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_country': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_city': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_province': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_postal_code': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_street_address': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_map_coordinates': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_avg_monthly_stay': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_housing_type': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_housing_type_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_trucks': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_water_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_water_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_heat_src': forms.TextInput(attrs={'class': 'custom-class'}),
            'home_6_heat_src_other': forms.TextInput(attrs={'class': 'custom-class'}),
        }


class Mandatory_questionaire_form(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    copd = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    asthma = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    emphysema = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    chronic_bronchitis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    hiv = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    long_covid = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    tuberculosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    adult_pneumonia = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    pulmonary_fibrosis = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True',
    )
    hypertension = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    diabetes = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    personal_cancer_history = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    biological_relatives_cancer = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )


    class Meta:
        model = Mandatory_questionaire
        fields = '__all__'
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'current_height': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'current_height_unit': forms.Select(attrs={'class': 'form-select-sm'}),
            'current_weight': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'current_weight_unit': forms.Select(attrs={'class': 'form-select-sm'}),
            'sex_birth': forms.Select(attrs={'class': 'form-select-sm'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'current_age': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'gender_identity': forms.Select(attrs={'class': 'form-select-sm'}),
            'gender_identity_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'gender_surgery_harmone': forms.Select(attrs={'class': 'form-select-sm'}),
            'ethinicity': forms.Select(attrs={'class': 'form-select-sm'}),
            'ethnicity_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'born_in_canada': forms.Select(attrs={'class': 'form-select-sm'}),
            'year_moved_to_canada': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'highest_education_lvl': forms.Select(attrs={'class': 'form-select-sm'}),
            'highest_education_lvl_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'copd': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'emphysema': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'chronic_bronchitis': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'asthma': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'diabetes': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'hypertension': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'tuberculosis': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'adult_pneumonia': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'pulmonary_fibrosis': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'hiv': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'long_covid': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'personal_cancer_history': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'personal_cancer_history_youngest_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'personal_history_cancer_type': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'num_sisters': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'num_brothers': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'num_half_sisters': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'num_half_brothers': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'children': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'biological_relatives_cancer': forms.TextInput(attrs={'class': 'form-control-sm'}),                      
        }



class biological_relatives_with_cancer_form(forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['mandatory_questionaire', 'Id', 'participant_num']
        model = biological_relatives_with_cancer
        widgets = {
            'biological_relationship': forms.TextInput(attrs={'class': 'relatives'}),
            'type_of_cancer': forms.TextInput(attrs={'class': 'relatives'}),
            'diagnosis_age': forms.TextInput(attrs={'class': 'relatives'}),
        }

class Mandatory_questionaire_form_c(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    
    smoked_more_100_cigs = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    smoked_pipe = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    stop_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    still_smoking_pipe = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    still_smoke_cigars = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    vape = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    still_vape = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    smoke_refrain = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    smoke_morning = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    smoke_sick = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    quit_smoking = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    ) 
    marajuana_use = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )             
    class Meta:
        model = Mandatory_questionaire_c
        fields = '__all__'


        widgets = {
            'smoked_more_100_cigs': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'age_regular_smoking': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'avg_cig_per_day': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'stop_smoking': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'last_cig_date': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'last_cig_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_1': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use_to_age_1': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_1_quantity': forms.Select(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_1_mode': forms.Select(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_1_units': forms.Select(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_2': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use_to_age_2': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_2_quantity': forms.Select(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_2_mode': forms.Select(attrs={'class': 'form-control-sm'}),
            'marajuana_use_age_2_units': forms.Select(attrs={'class': 'form-control-sm'}),
            'mara_use_age_3': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_to_age_3': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_3_quantity': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_3_mode': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_3_units': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_4': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_to_age_4': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_4_quantity': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_4_mode': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'mara_use_age_4_units': forms.TextInput(attrs={'class': 'form-control-sm'}),    
            'smoked_pipe': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'smoked_pipe_avg_ounces': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'smoked_pipe_avg_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_smoking_pipe': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_smoking_pipe_start_date': forms.DateInput(attrs={'type': 'date'}),
            'still_smoking_pipe_start_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_smoking_pipe_stop_date': forms.DateInput(attrs={'type': 'date'}),
            'still_smoking_pipe_stop_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'smoked_cigars': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'avg_num_cigars': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'avg_cigar_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_smoke_cigars': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_smoke_cigars_stop_date': forms.DateInput(attrs={'type': 'date'}),
            'still_smoke_cigars_stop_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'chewing_tobacco': forms.Select(attrs={'class': 'form-control-sm'}),
            'chewing_tobacco_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'chewing_tobacco_years': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'snuff': forms.Select(attrs={'class': 'form-control-sm'}),
            'snuff_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'snuff_years': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'vape': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'vape_num_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'vape_start_date': forms.DateInput(attrs={'type': 'date'}),
            'vape_stop_date': forms.DateInput(attrs={'type': 'date'}),
            'vape_start_age' : forms.TextInput(attrs={'class': 'form-control-sm'}),
            'vape_flavor': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_vape': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_vape_stop_age': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'still_vape_stop_date': forms.DateInput(attrs={'type': 'date'}),
            'vape_flavor': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cigs_waking_up': forms.Select(attrs={'class': 'form-control-sm'}),
            'smoke_refrain': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'cig_giveup': forms.Select(attrs={'class': 'form-control-sm'}),
            'smoke_morning': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'smoke_sick': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'quit_smoking': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'quit_smoking_times': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }

class Mandatory_questionaire_form_de(forms.ModelForm):
    YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
    ]
    second_hand_daily_choices = [
        ('Daily', 'Daily'),
        ('At Least 4 Days/Week but not everyday', 'At Least 4 Days/Week but not everyday'),
        ('1 - 3 Days/Week', '1 - 3 Days/Week'),
        ('Occasionally', 'Occasionally'),
    ]

    second_hand_1yr = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )  
    alcohol = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )   
    alcohol_current = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    second_hand_daily = forms.TypedChoiceField(
    choices=second_hand_daily_choices,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )     
    class Meta:
        model = Mandatory_questionaire_de
        fields = '__all__'
        widgets = {
            'second_hand_smoke': forms.Select(attrs={'class': 'form-control-sm'}),
            'second_hand_1yr': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'second_hand_home': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-container in-line'}),
            'second_hand_work': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_leisure': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_daily': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'second_hand_4days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_13days': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_occasionally': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_2hrs': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand24hrs': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_46hrs': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_6hrs': forms.CheckboxInput(attrs={'class': 'checkbox-container'}),
            'second_hand_yrs': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'second_hand_youth': forms.Select(attrs={'class': 'form-control-sm'}),
            'second_hand_avg_exposure': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'alcohol': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'alcohol_from_age1': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_to_age1': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_beer1': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_wine1': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_liquor1': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_from_age2': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_to_age2': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_beer2': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_wine2': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_liquor2': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_from_age3': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_to_age3': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_beer3': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_wine3': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_liquor3': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_from_age4': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_to_age4': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_beer4': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_wine4': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_liquor4': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_current': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'alcohol_stop_age': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
        }
    
class Mandatory_questionaire_form_fg(forms.ModelForm):
    YES_NO_DK_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
    (2, 'Don''t know')
    ]
    inhaled_drugs = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )   
    bronchodialators = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )   
    statins = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )  
    metformin = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    ) 
    occupation_exposure = forms.TypedChoiceField(
    choices=YES_NO_DK_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )            
    class Meta:
        model = Mandatory_questionaire_fg
        fields = '__all__'
        widgets = {
            'inhaled_drugs': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'inhaled_drugs_day': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'inhaled_drugs_month': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'inhaled_drugs_year': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'inhaled_drugs_freq': forms.Select(attrs={'class': 'form-control-sm'}),
            'bronchodialators': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'bronchodialators_day': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'bronchodialators_month': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'bronchodialators_year': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'bronchodialators_freq': forms.Select(attrs={'class': 'form-control-sm'}),
            'statins': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'statins_day': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'statins_month': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'statins_year': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'statins_freq': forms.Select(attrs={'class': 'form-control-sm'}),
            'metformin': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'metformin_day': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'metformin_month': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'metformin_year': forms.TextInput(attrs={'class': 'form-control-sm entry'}),
            'metformin_freq': forms.Select(attrs={'class': 'form-control-sm'}),
            'current_working_situation': forms.Select(attrs={'class': 'form-control-sm'}),
            'current_working_situation_other': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'occupation_longest': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'occupation_longest_activities': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'occupation_longest_years': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'occupation_exposure': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
            'occupation_fumes': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'occupation_years': forms.TextInput(attrs={'class': 'form-control-sm'}),


        }
    
class SearchForm(forms.Form):
    class Meta:
        fields = '__all__'



class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs["attrs"] = {"type": "date", "required": kwargs.get("required", False)}
        super().__init__(*args, **kwargs)



class CT_Scan_Form(forms.ModelForm):

    cat_5_findings = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]

    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]

    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('non-actionalbe', 'non-actionalbe'),
        ('actionable', 'actionable'),
    )
    ct_scan_date = forms.DateField(widget=CustomDateInput)
    ct_scan_review_date = forms.DateField(widget=CustomDateInput)
    radiologist_fu_mnths_date = forms.DateField(widget=CustomDateInput)
    cad_fu_mnths_date = forms.DateField(widget=CustomDateInput)
    final_rec_fu_mnths_date = forms.DateField(widget=CustomDateInput)

  #  copd_emphysema_type = forms.MultipleChoiceField(
  #  choices=emphysema_type,
  #  widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm', 'style': 'checkbox-inline'})
  #  )




    CAT_5_CHOICES = [
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    ]

    EMPHYSEMA_CHOICES = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]

    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]
   

    cat_5_findings = forms.MultipleChoiceField(
        choices=CAT_5_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm'}),
        required=False,
    )

    copd_emphysema_type = forms.MultipleChoiceField(
        choices=EMPHYSEMA_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm', 'style': 'checkbox-inline'}),
        required=False,
    )

    airways_type = forms.MultipleChoiceField(
    choices=airways_type,
    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm', 'style': 'checkbox-inline'}),
    required=False,
    )

    class Meta:
        model = ct_scan
        fields = '__all__'

        widgets = {
        
        'ct_scan_visitID': forms.Select(attrs={'class': 'form-control-sm'}),
        'ct_scan_location': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'ct_scan_radiologist': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'ct_scan_familty_history': forms.CheckboxInput(attrs={'class': 'radio-inline'}),
        'ct_scan_pt_lung_cancer': forms.CheckboxInput(attrs={'class': 'radio-inline'}),
        'ct_scan_dlp': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'radiologist_fu_mnths': forms.Select(attrs={'class': 'form-control-sm'}),
        'cad_fu_mnths': forms.Select(attrs={'class': 'form-control-sm'}),
        'ilst_cat': forms.Select(attrs={'class': 'form-control-sm'}),
        'final_rec_fu_mnths': forms.Select(attrs={'class': 'form-control-sm'}),
        'copd_emphysema': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
        'copd_emphysema_extent': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
        #'copd_emphysema_type': forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm', 'style' : 'checkbox-inline'}),
        'copd_emphysema_distribution': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
        'cor_art_calc': forms.RadioSelect(attrs={'class': 'radio-inline'}),
        'cor_art_agatson': forms.TextInput(attrs={'class': 'form-control-sm','style': 'width: 60px;'}),
        'airways': forms.RadioSelect(attrs={'class': 'form-control-sm'}),
        'airways_type' : forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm'}),
        'airways_type_muc_impaction': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'aiways_type_wall_thickening': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'airways_type_bronchiectasis': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'ariways_type_bronchiolectasis': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'cat_5_findings': forms.CheckboxSelectMultiple(attrs={'class': 'form-control-sm'}),
        'cat_5_lymph_nodes': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'cat_5_suspicious_nodes': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'cat_5_endobronchial': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'cat_5_comments': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'width: 220px;', 'style': 'height: 150px;'}),
        'other_cardiovascular': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_cardiovascular_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_vertebral': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_vertebral_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_GI': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_GI_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_breast': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_breast_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_endocrine': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_endocrine_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_lymph': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_lymph_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_pleura': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_pleura_comments': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_pulmonary_fibrosis': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_pulmonary_fibrosis_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_musculoskeletal': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_musculoskeletal_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'other_other': forms.Select(attrs={'class': 'form-control-sm'}),
        'other_other_comments': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'general_comments': forms.TextInput(attrs={'class': 'form-control-lg', 'style': 'width: 500px;', 'height': '300px'}),
    }

class CT_Scan_Nodule_Form_1(ModelForm):
    class Meta:
        model = ct_scan_nodule_1
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_segment': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_cad_found': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_interval_change': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location_selection' : forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_type': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_density': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_sd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_description': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_change_avediam': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_dd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volsperc': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_comments': forms.Textarea(attrs={'class': 'form-control-sm', 'style':'width: 100px;', 'style': 'height: 100px;'}),
            'nodule_risk_index': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_key_nodule': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_recommended_fu': forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_fleicher_fu' : forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_orders': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }

class CT_Scan_Nodule_Form_2(ModelForm):
    class Meta:
        model = ct_scan_nodule_2
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_segment': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_cad_found': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_interval_change': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location_selection' : forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_type': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_density': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_sd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_description': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_change_avediam': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_dd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volsperc': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_comments': forms.Textarea(attrs={'class': 'form-control-sm', 'style':'width: 100px;', 'style': 'height: 100px;'}),
            'nodule_risk_index': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_key_nodule': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_recommended_fu': forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_fleicher_fu' : forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_orders': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }

class CT_Scan_Nodule_Form_3(ModelForm):
    class Meta:
        model = ct_scan_nodule_3
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_segment': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_cad_found': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_interval_change': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location_selection' : forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_type': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_density': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_sd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_description': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_change_avediam': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_dd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volsperc': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_comments': forms.Textarea(attrs={'class': 'form-control-sm', 'style':'width: 100px;', 'style': 'height: 100px;'}),
            'nodule_risk_index': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_key_nodule': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_recommended_fu': forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_fleicher_fu' : forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_orders': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }


class CT_Scan_Nodule_Form_4(ModelForm):
    class Meta:
        model = ct_scan_nodule_4
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_segment': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_cad_found': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_interval_change': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location_selection' : forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_type': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_density': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_sd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_description': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_change_avediam': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_dd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volsperc': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_comments': forms.Textarea(attrs={'class': 'form-control-sm', 'style':'width: 100px;', 'style': 'height: 100px;'}),
            'nodule_risk_index': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_key_nodule': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_recommended_fu': forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_fleicher_fu' : forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_orders': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }


class CT_Scan_Nodule_Form_5(ModelForm):
    class Meta:
        model = ct_scan_nodule_5
        fields = '__all__'
        widgets = {
            'nodule_rank': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_slice_num': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_segment': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_cad_found': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
            'nodule_status': forms.RadioSelect(attrs={'class': 'radio-inline'}),
            'nodule_radiologist_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_technition_accepted': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_interval_change': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location_selection' : forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_type': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_axis_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_density': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_axis_sd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_long': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_ssn_short': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_description': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_location': forms.RadioSelect(attrs={'class': 'radio-inline','style': 'width: 40px;'}),
            'nodule_change_avediam': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_dd': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volume': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_volsperc': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_change_mean': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_comments': forms.Textarea(attrs={'class': 'form-control-sm', 'style':'width: 100px;', 'style': 'height: 100px;'}),
            'nodule_risk_index': forms.TextInput(attrs={'class': 'form-control-sm', 'style':'width: 50px;'}),
            'nodule_key_nodule': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_cancer_confirmed': forms.CheckboxInput(attrs={'class': 'form-control-md'}),
            'nodule_recommended_fu': forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_fleicher_fu' : forms.Select(attrs={'class': 'form-control-sm'}),
            'nodule_orders': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }



class MyForm(forms.Form):
    model = MyForm
    fields = '__all__'
    widgets = {
        'variable1' : forms.CharField(max_length=100),
        'variable2' : forms.CharField(max_length=100),
        'variable3' : forms.CharField(max_length=100),
    }

class CancerHistoryForm(forms.Form):
    model = CancerHistory
    biological_rel = forms.CharField()
    type_of_cancer = forms.CharField()
    age_diagnosis = forms.CharField()


class inclusion_form(ModelForm):
    YES_NO_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
    ]
    inclusion_criteria_1 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_2 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_3 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_4 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_5 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_6 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_7 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_8 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9 = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9_a = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9_b = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9_c = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    inclusion_criteria_9_d = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )

    

    class Meta:  
        model = inclusion
        fields = '__all__'
        widgets = {
        'inclusion_criteria_1': forms.BooleanField(required=False),
        'inclusion_criteria_2': forms.BooleanField(required=False),
        'inclusion_criteria_3': forms.BooleanField(required=False),
        'inclusion_criteria_4': forms.BooleanField(required=False),
        'inclusion_criteria_5': forms.BooleanField(required=False),
        'inclusion_criteria_6': forms.BooleanField(required=False),
        'inclusion_criteria_7': forms.BooleanField(required=False),
        'inclusion_criteria_8': forms.BooleanField(required=False),
        'inclusion_criteria_9': forms.BooleanField(required=False),
        'inclusion_criteria_9_a': forms.BooleanField(required=False),
        'inclusion_criteria_9_b': forms.BooleanField(required=False),
        'inclusion_criteria_9_c': forms.BooleanField(required=False),
        'inclusion_criteria_9_d': forms.BooleanField(required=False),
        'inclusion_status': forms.Select(attrs={'class': 'form-control-sm'}),
        'screening_status': forms.Select(attrs={'class': 'form-control-sm'}),
        'consent_status': forms.Select(attrs={'class': 'form-control-sm'}),
        
        'parpticpant_status' : forms.TextInput(attrs={'class': 'form-control-sm'}),

        }
        def save(self, commit=True):
            inclusion_data = super().save(commit=False)
            participant_number = self.cleaned_data.get('participant_number')
            if participant_number:
                participant, created = Participant.objects.get_or_create(participant_number=participant_number)
                inclusion_data.participant_number = participant
            if commit:
                inclusion_data.save()
            return inclusion_data

# class protocol_deviations_form(forms.Form):
#     model = protocol_deviations
#     fields = '__all__'
#     widgets = {
#     'protocol_deviation_1': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_2': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_3': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_4': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_5': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_6': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_7': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_8': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_9': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     'protocol_deviation_10': forms.TextInput(attrs={'class': 'form-control-sm'}),
#     }


class ParticipantForm2(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['participant_number']


#----------------------------------#
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'participant_number': forms.TextInput(),  # Set the participant_number field as HiddenInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant_number'].required = False 



class testParticipantForm(forms.ModelForm):
    class Meta:
        model = testParticipant
        fields = '__all__'


class plco_score_form(forms.ModelForm):
    YES_NO_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
    ]   
    copd = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    cancer_history = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    lung_cancer_history = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    smoking_status = forms.TypedChoiceField(
    choices=YES_NO_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'radio'}),
    coerce=lambda x: x == 'True'
    )
    class Meta:
        model = PLCO_score
        fields = '__all__'
        widgets = { 
        'participant_num': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'education': forms.Select(attrs={'class': 'form-control-sm'}),
        'bmi': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'copd': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'cancer_history': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'lung_cancer_history': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'race': forms.Select(attrs={'class': 'form-control-sm'}),
        'smoking_status': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'avg_num_cigs_smoked_day': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'duration_smoked': forms.TextInput(attrs={'class': 'form-control-sm'}),
        'years_quit': forms.TextInput(attrs={'class': 'form-control-sm'}),
        }




class ParticipantSearchForm(forms.Form):
    participant_number = forms.CharField(label='Participant Number')