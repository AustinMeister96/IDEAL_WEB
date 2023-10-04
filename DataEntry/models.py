from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

""" class User(AbstractUser):


    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('data_entry', 'Data Entry'),
        ('lab_processing', 'Lab'),
    )

    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='data_entry')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.username """
class UserAccounts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):    
        return self.username + ' ' + self.first_name + ' ' + self.last_name
    


class Participant(models.Model):
    participant_number = models.CharField(primary_key=True, unique=True, max_length=7)

    def __str__(self):
        return self.participant_number


class testParticipant(models.Model):
    number = models.IntegerField()
    birthday = models.DateField()
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_address = models.TextField()
    UserAccounts = models.ManyToManyField(UserAccounts, blank=True)


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True 
    was_published_recently.short_description='Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    

    
#create a blood_collection class with the following attributes: Ideal_participant_num, Date_of_birth, Visit_type, Comments , Date_of_collection, Collected_by, Time_collected, Processing_start_time, Time_placed_freezer, Freezer_box_num , Y_Plasma_barcode_1, Y_Plasma_barcode_2, P_plasma_barcode_1 , p_plasma_barcode_2, r_rbc_barcode_1, r_rbc_barcode_2, y_bottom_barcode_1, y_bottom_barcode_2, p_bottom_barcode_1, p_bottom_barcode_2
class Blood_Collection(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    ideal_participant_num = models.IntegerField(default=0)
    date_of_birth = models.DateTimeField('date of birth')
    visit_type = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    date_of_collection = models.DateTimeField('date of collection')
    collected_by = models.CharField(max_length=200)
    time_collected = models.DateTimeField('time collected')
    processing_start_time = models.DateTimeField('processing start time')
    time_placed_freezer = models.DateTimeField('time placed freezer')
    freezer_box_num = models.IntegerField(default=0)
    y_plasma_barcode_1 = models.IntegerField(default=0)
    y_plasma_barcode_2 = models.IntegerField(default=0)
    p_plasma_barcode_1 = models.IntegerField(default=0)
    p_plasma_barcode_2 = models.IntegerField(default=0)
    r_rbc_barcode_1 = models.IntegerField(default=0)
    r_rbc_barcode_2 = models.IntegerField(default=0)
    y_bottom_barcode_1 = models.IntegerField(default=0)
    y_bottom_barcode_2 = models.IntegerField(default=0)
    p_bottom_barcode_1 = models.IntegerField(default=0)
    p_bottom_barcode_2 = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ideal_participant_num

#create a breath_collection class with the following attributes: Collection_date, collection_time, collected_by, location, brush_teeth, brush_teeth_time, mouthwash, face_cream, perfume_cologne, deodorant, smoke_exposure, fuel_car, arrival_type, last_meal, last_meal_time, last_drink, last_drink_time, short_of_breath, fever, cough, cold, no_symptoms, halitosis, reciva_barcode, tennax_number, casper_flow, collection_start_time, collection_stop_time, collection_duration, breathing_rate, aborted, incomplete, declined, room_air_barcode, room_air_tennax, casper_barcode, casper_tennax, notes
class Breath_Collection(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    collection_date = models.DateTimeField('collection date')
    collection_time = models.DateTimeField('collection time')
    collected_by = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    brush_teeth = models.BooleanField(default=False, null=True, blank=True)
    brush_teeth_time = models.DateTimeField('brush teeth time', null=True, blank=True)
    mouthwash = models.BooleanField(default=False, null=True, blank=True)
    face_cream = models.BooleanField(default=False, null=True, blank=True)
    perfume_cologne = models.BooleanField(default=False, null=True, blank=True)
    deodorant = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure = models.BooleanField(default=False, null=True, blank=True)
    fuel_car = models.BooleanField(default=False, null=True, blank=True)
    arrival_type = models.CharField(max_length=200, null=True, blank=True)
    last_meal = models.CharField(max_length=200, null=True, blank=True)
    last_meal_time = models.DateTimeField('last meal time', null=True, blank=True)
    last_drink = models.CharField(max_length=200, null=True, blank=True)
    last_drink_time = models.DateTimeField('last drink time', null=True, blank=True)
    short_of_breath = models.BooleanField(default=False, null=True, blank=True)
    fever = models.BooleanField(default=False, null=True, blank=True)
    cough = models.BooleanField(default=False, null=True, blank=True)
    cold = models.BooleanField(default=False, null=True, blank=True)
    no_symptoms = models.BooleanField(default=False, null=True, blank=True)
    halitosis = models.BooleanField(default=False, null=True, blank=True)
    reciva_barcode = models.IntegerField(default=0, null=True, blank=True)
    tennax_number = models.IntegerField(default=0, null=True, blank=True)
    casper_flow = models.IntegerField(default=0, null=True, blank=True)
    collection_start_time = models.DateTimeField('collection start time', null=True, blank=True)
    collection_stop_time = models.DateTimeField('collection stop time', null=True, blank=True)
    collection_duration = models.IntegerField(default=0, null=True, blank=True)
    breathing_rate = models.IntegerField(default=0, null=True, blank=True)
    aborted = models.BooleanField(default=False, null=True, blank=True)
    incomplete = models.BooleanField(default=False, null=True, blank=True)
    declined = models.BooleanField(default=False, null=True, blank=True)
    room_air_barcode = models.IntegerField(default=0, null=True, blank=True)
    room_air_tennax = models.IntegerField(default=0, null=True, blank=True)
    casper_barcode = models.IntegerField(default=0, null=True, blank=True)
    casper_tennax = models.IntegerField(default=0, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    casper_caps = models.IntegerField(default=0, null=True, blank=True)
    volume_collected = models.IntegerField(default=0, null=True, blank=True)
    birth_control = models.BooleanField(default=False, null=True, blank=True)
    birth_control_duration = models.IntegerField(default=0, null=True, blank=True)
    menopausal = models.BooleanField(default=False, null=True, blank=True)
    hrt_menopause = models.BooleanField(default=False, null=True, blank=True)
    grt_menopause_duration = models.IntegerField(default=0, null=True, blank=True)
    gender_affirming_surgery = models.BooleanField(default=False, null=True, blank=True)
    gender_affirming_type = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication = models.BooleanField(default=False, null=True, blank=True)
    inhaled_medication_type = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication_brand = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication_name = models.CharField(max_length=200, null=True, blank=True)
    pneumonia = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure_type = models.CharField(max_length=200, null=True, blank=True)
    room_air_collection_time = models.DateTimeField('room air collection time', null=True, blank=True)
    casper_collection_time = models.DateTimeField('casper collection time', null=True, blank=True)


    def __str__(self):
        return self.location

#room_air_storage, casper_storage, reciva_caps, room_air_caps, casper_caps, sweat_location, sweat_caps, micro_int_std_sln, micro_int_std_vol, micro_hs_left, micro_hs_right, micro_extraction, micro_incubation, hs_blk_tennax, hs_blk_micro_num, hs_blk_purge, hs_blk_storage, hs_blk_caps, hs_blk_wbrush_tennax, hs_blk_wbrush_micro_num, hs_blk_wbrush_purge, hs_blk_wbrush_storage, hs_blk_wbrush_caps, hs_l_tennax, hs_l_micro_num, hs_l_purge, hs_l_storage, hs_l_caps, hs_r_tennax, hs_r_micro_num, hs_r_purge, hs_r_storage, hs_r_caps, da_reciva_spiked, da_reciva_int_std, da_reciva_method, da_reciva_date, da_room_air_spiked, da_room_air_inst_std, da_room_air_method, da_room_air_date, da_capser_spiked, da_casper_int_std, da_casper_method, da_casper_date, da_sweat_spiked, da_sweat_int_std, da_sweat_method, da_sweat_date, da_hs_blk_spiked, da_hs_blk_int_std, da_hs_blk_method, da_hs_blk_date, da_hs_blk_wbrush_spiked, da_hs_blk_wbrush_int_std, da_hs_blk_wbrush_method, da_hs_blk_wbrush_date, da_hs_l_spiked, da_hs_l_int_std, da_hs_l_method, da_hs_l_date, da_hs_r_spiked, da_hs_r_int_std, da_hs_r_method, da_hs_r_date, notes    

#create a lab_processing class with the following attributes: int_std_sln, int_std_sln_vol, reciva_purge, room_air_purge, casper_purge, reciva_spiked, room_air_spiked, casper_spiked, reciva_storage
class lab_processing(models.Model):
    collection_site = (
        ('British Columbia', 'British Columbia'),
        ('Ontario', 'Ontario'),
        ('Quebec', 'Quebec'),
    )
    gas_used = (
        ('Nitrogen 4.8', 'Nitrogen 4.8'),
        ('Nitrogen 5.0', 'Nitrogen 5.0'),
        ('Nitrogen 6.0', 'Nitrogen 6.0'),
        ('Helium 5.0', 'Helium 5.0'),
    )
    intrument = (
        ('Orbitrap 736', 'Orbitrap 736'),
        ('Bench TOF', 'Bench TOF'),
        ('Orbitrap XXX', 'Orbitrap XXX'),
    )
    spiking_method = (
        ('Maual', 'Manual'), 
        ('CSLR', 'CSLR'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    reciva_tennax = models.IntegerField(default=0)
    reciva_barcode = models.IntegerField(default=0)
    reciva_collection_date = models.DateTimeField('reciva collection date', null=True)
    reciva_time_since_collection = models.IntegerField(default=0)
    reciva_collection_site = models.CharField(max_length=200, choices=collection_site,null=True)
    reciva_ship_date = models.DateTimeField('reciva ship date',null=True)
    reciva_received_date = models.DateTimeField('reciva received date',null=True)
    reciva_shipping_method = models.CharField(max_length=200)
    reciva_sample_stored = models.BooleanField(default=False)
    reciva_sample_storage_date = models.DateTimeField('reciva sample storage date',null=True)
    reciva_sample_storage_location = models.CharField(max_length=200)
    reciva_sample_storage_temperature = models.IntegerField(default=0)
    reciva_time_in_storage = models.IntegerField(default=0)
    reciva_purge = models.BooleanField(default=False)
    reciva_purge_gas = models.CharField(max_length=200, choices=gas_used,null=True)
    reciva_purge_gas_flow = models.IntegerField(default=0)
    reciva_purge_gas_duration = models.IntegerField(default=0)
    reciva_spiked = models.BooleanField(default=False)
    reciva_istd_used = models.CharField(max_length=200)
    reciva_istd_vol = models.IntegerField(default=0)
    reciva_istd_applied = models.CharField(max_length=200, choices=spiking_method,null=True)
    reciva_cslr_gas = models.CharField(max_length=200, choices=gas_used)
    reciva_cslr_gas_flow = models.IntegerField(default=0)
    reciva_cslr_gas_duration = models.IntegerField(default=0)
    reciva_sample_run = models.BooleanField(default=False)
    reciva_sample_run_date = models.DateTimeField('reciva sample run date',null=True)
    reciva_sample_run_instrument = models.CharField(max_length=200, choices=intrument,null=True)
    reciva_sample_td_method = models.CharField(max_length=200)
    reciva_sample_ms_method = models.CharField(max_length=200)
    reciva_sample_filename = models.CharField(max_length=200)
    reciva_sample_file_location = models.CharField(max_length=200)
    reciva_sample_visual_inspection = models.BooleanField(default=False)
    reciva_notes = models.TextField(max_length=200)
    room_air_tennax = models.IntegerField(default=0)
    room_air_barcode = models.IntegerField(default=0)
    room_air_collection_date = models.DateTimeField('room air collection date',null=True)
    room_air_time_since_collection = models.IntegerField(default=0)
    room_air_collection_site = models.CharField(max_length=200, choices=collection_site,null=True)
    room_air_ship_date = models.DateTimeField('room air ship date',null=True)
    room_air_received_date = models.DateTimeField('room air received date',null=True)
    room_air_shipping_method = models.CharField(max_length=200)
    room_air_sample_stored = models.BooleanField(default=False)
    room_air_sample_storage_date = models.DateTimeField('room air sample storage date',null=True)
    room_air_sample_storage_location = models.CharField(max_length=200)
    room_air_sample_storage_temperature = models.IntegerField(default=0)
    room_air_time_in_storage = models.IntegerField(default=0)
    room_air_purge = models.BooleanField(default=False)
    room_air_purge_gas = models.CharField(max_length=200, choices=gas_used,null=True)
    room_air_purge_gas_flow = models.IntegerField(default=0)
    room_air_purge_gas_duration = models.IntegerField(default=0)
    room_air_spiked = models.BooleanField(default=False)
    room_air_istd_used = models.CharField(max_length=200)
    room_air_istd_vol = models.IntegerField(default=0)
    room_air_istd_applied = models.CharField(max_length=200, choices=spiking_method,null=True)
    room_air_cslr_gas = models.CharField(max_length=200, choices=gas_used)
    room_air_cslr_gas_flow = models.IntegerField(default=0)
    room_air_cslr_gas_duration = models.IntegerField(default=0)
    room_air_sample_run = models.BooleanField(default=False)
    room_air_sample_run_date = models.DateTimeField('room air sample run date',null=True)
    room_air_sample_run_instrument = models.CharField(max_length=200, choices=intrument,null=True)
    room_air_sample_td_method = models.CharField(max_length=200)
    room_air_sample_ms_method = models.CharField(max_length=200)
    room_air_sample_filename = models.CharField(max_length=200)
    room_air_sample_file_location = models.CharField(max_length=200)
    room_air_sample_visual_inspection = models.BooleanField(default=False)
    room_air_notes = models.TextField(max_length=200)
    casper_tennax = models.IntegerField(default=0)
    casper_barcode = models.IntegerField(default=0)
    casper_collection_date = models.DateTimeField('casper collection date',null=True)
    casper_time_since_collection = models.IntegerField(default=0)
    casper_collection_site = models.CharField(max_length=200, choices=collection_site,null=True)
    casper_ship_date = models.DateTimeField('casper ship date',null=True)
    casper_received_date = models.DateTimeField('casper received date',null=True)
    casper_shipping_method = models.CharField(max_length=200)
    casper_sample_stored = models.BooleanField(default=False)
    casper_sample_storage_date = models.DateTimeField('casper sample storage date',null=True)
    casper_sample_storage_location = models.CharField(max_length=200)
    casper_sample_storage_temperature = models.IntegerField(default=0)
    casper_time_in_storage = models.IntegerField(default=0)
    casper_purge = models.BooleanField(default=False)
    casper_purge_gas = models.CharField(max_length=200, choices=gas_used,null=True)
    casper_purge_gas_flow = models.IntegerField(default=0)
    casper_purge_gas_duration = models.IntegerField(default=0)
    casper_spiked = models.BooleanField(default=False)
    casper_istd_used = models.CharField(max_length=200)
    casper_istd_vol = models.IntegerField(default=0)
    casper_istd_applied = models.CharField(max_length=200, choices=spiking_method,null=True)
    casper_cslr_gas = models.CharField(max_length=200, choices=gas_used)
    casper_cslr_gas_flow = models.IntegerField(default=0)
    casper_cslr_gas_duration = models.IntegerField(default=0)
    casper_sample_run = models.BooleanField(default=False)
    casper_sample_run_date = models.DateTimeField('casper sample run date',null=True)
    casper_sample_run_instrument = models.CharField(max_length=200, choices=intrument,null=True)
    casper_sample_td_method = models.CharField(max_length=200)
    casper_sample_ms_method = models.CharField(max_length=200)
    casper_sample_filename = models.CharField(max_length=200)
    casper_sample_file_location = models.CharField(max_length=200)
    casper_sample_visual_inspection = models.BooleanField(default=False)
    casper_notes = models.TextField(max_length=200)



    def __str__(self):
        return self.int_std_sln


class lab_processing2(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    da_hs_blk_spiked = models.TextField(max_length=20)
    da_hs_blk_int_std = models.TextField(max_length=20)
    da_hs_blk_method = models.TextField(max_length=20)
    da_hs_blk_date = models.TextField(max_length=20)
    da_hs_blk_wbrush_spiked = models.TextField(max_length=20)
    da_hs_blk_wbrush_int_std = models.TextField(max_length=20)
    da_hs_blk_wbrush_method = models.TextField(max_length=20)
    da_hs_blk_wbrush_date = models.TextField(max_length=20)
    da_hs_l_spiked = models.TextField(max_length=20)
    da_hs_l_int_std = models.TextField(max_length=20)
    da_hs_l_method = models.TextField(max_length=20)
    da_hs_l_date = models.TextField(max_length=20)
    da_hs_r_spiked = models.TextField(max_length=20)
    da_hs_r_int_std = models.TextField(max_length=20)
    da_hs_r_method = models.TextField(max_length=20)
    da_hs_r_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    
    def __str__(self):
        return self.da_hs_l_int_std




# create a class with the following attributes: total_exposure, asbestos_exposure, asbestos_exposure_duration, asbestos_exposure_age, sislica_exposure_age, silica_exposure_duration, silica_exposure, diesel, diesel_duration, diesel_exposure_age, radon, radon_duration, radon_exposure_age, cadmium, cadmium_duraition, cadmium_exposure_age, coal, coal_duration, coal_exposure_age, nickel, nickel_duration, nickel_exposure_age, plutonium, plutonium_duration, plutonium_exposure_age, beryllium, beryllium_duration, beryllium_exposure_age, ether, ether_duration, ether_exposure_age, soot, soot_duration, soot_exposure_age, welding, welding_duration, welding_exposure_age, radiation, radiation_duration, radiation_exposure_age, munitions, munitions_duration, munitions_exposure_age, warfare, warfare_duration, warfare_exposure_age, acheson, acheson_duration, acheson_exposure_age, aluminum, aluminum_duration, aluminum_exposure_age, coal, coal_duration, coal_exposure_age, coke, coke_duration, coke_exposure_age, mining, mining_duration, mining_exposure_age, iron, iron_duration, iron_exposure_age, painting, painting_duration, painting_exposure_age, rubber, rubber_duration, rubber_exposure_age, oil, oil_duration, oil_exposure_age, sulfur, sulfur_duration, sulfur_exposure_age, atsugi, atsugi_duration, atsugi_exposure_age, sand, sand_duration, sand_exposure_age

class Exposure(models.Model):

    yes_no_dk = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont Know', 'Dont Know'),
    )

    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    total_exposure = models.TextField(max_length=20)
    asbestos_exposure = models.TextField(max_length=100, choices=yes_no_dk)
    asbestos_exposure_duration = models.TextField(max_length=20)
    asbestos_exposure_age = models.TextField(max_length=20)
    silica_exposure_age = models.TextField(max_length=20)
    silica_exposure_duration = models.TextField(max_length=20)
    silica_exposure = models.TextField(max_length=20, choices=yes_no_dk)
    diesel = models.TextField(max_length=20)
    diesel_duration = models.TextField(max_length=20)
    diesel_exposure_age = models.TextField(max_length=20)
    radon = models.TextField(max_length=20)
    radon_duration = models.TextField(max_length=20)
    radon_exposure_age = models.TextField(max_length=20)
    cadmium = models.TextField(max_length=20)
    cadmium_duration = models.TextField(max_length=20)
    cadmium_exposure_age = models.TextField(max_length=20)
    chromium = models.TextField(max_length=20)
    chromium_duration = models.TextField(max_length=20)
    chromium_exposure_age = models.TextField(max_length=20)
    coal = models.TextField(max_length=20)
    coal_duration = models.TextField(max_length=20)
    coal_exposure_age = models.TextField(max_length=20)
    arsenic = models.TextField(max_length=20)
    arsenic_duration = models.TextField(max_length=20)
    arsenic_exposure_age = models.TextField(max_length=20)
    nickel = models.TextField(max_length=20)
    nickel_duration = models.TextField(max_length=20)
    nickel_exposure_age = models.TextField(max_length=20)
    plutonium = models.TextField(max_length=20)
    plutonium_duration = models.TextField(max_length=20)
    plutonium_exposure_age = models.TextField(max_length=20)
    beryllium = models.TextField(max_length=20)
    beryllium_duration = models.TextField(max_length=20)
    beryllium_exposure_age = models.TextField(max_length=20)
    ether = models.TextField(max_length=20)
    ether_duration = models.TextField(max_length=20)
    ether_exposure_age = models.TextField(max_length=20)
    soot = models.TextField(max_length=20)
    soot_duration = models.TextField(max_length=20)
    soot_exposure_age = models.TextField(max_length=20)
    welding = models.TextField(max_length=20)
    welding_duration = models.TextField(max_length=20)
    welding_exposure_age = models.TextField(max_length=20)
    radiation = models.TextField(max_length=20)
    radiation_duration = models.TextField(max_length=20)
    radiation_exposure_age = models.TextField(max_length=20)
    munitions = models.TextField(max_length=20)
    munitions_duration = models.TextField(max_length=20)
    munitions_exposure_age = models.TextField(max_length=20)
    warfare = models.TextField(max_length=20)
    warfare_duration = models.TextField(max_length=20)
    warfare_exposure_age = models.TextField(max_length=20)
    acheson = models.TextField(max_length=20)
    acheson_duration = models.TextField(max_length=20)
    acheson_exposure_age = models.TextField(max_length=20)
    aluminum = models.TextField(max_length=20)
    aluminum_duration = models.TextField(max_length=20)
    aluminum_exposure_age = models.TextField(max_length=20)
    coal = models.TextField(max_length=20)
    coal_duration = models.TextField(max_length=20)
    coal_exposure_age = models.TextField(max_length=20)
    coke = models.TextField(max_length=20)
    coke_duration = models.TextField(max_length=20)
    coke_exposure_age = models.TextField(max_length=20)
    mining = models.TextField(max_length=20)
    mining_duration = models.TextField(max_length=20)
    mining_exposure_age = models.TextField(max_length=20)
    iron = models.TextField(max_length=20)
    iron_duration = models.TextField(max_length=20)
    def __str__(self):
        return self.total_exposure 

    
class Exposure2(models.Model):
    yes_no_dk = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Dont Know', 'Dont Know'),
    )
    cooking_freq = (
    ('N/A', 'N/A'),
    ('Everyday', 'Everyday'),
    ('Every Week', 'Every Week'),
    ('Every Month', 'Every Month'),
    )
    cooking_fuel = (
        ('Wood', 'Wood'),
        ('Charcoal', 'Charcoal'),
        ('Gas', 'Gas'),
        ('Electricity', 'Electricity'),
        ('Other', 'Other'),
    )
    cooking_oils = (
        ('Animal Fat Store bought', 'Animal Fat Store bought'),
        ('Animal Fat Homemade', 'Animal Fat Homemade'),
        ('Vegetable Oil', 'Vegetable Oil'),
        ('Other', 'Other'),
    )
    total_exposure = (
        ('No or almost no exposure', 'No or almost no exposure'),
        ('Light exposure', 'Light exposure'),
        ('Moderate exposure', 'Moderate exposure'),
        ('Heavy exposure', 'Heavy exposure'),
    )

    eating_freq = (
        ('Never', 'Never'),
        ('Less than 1 time per month', 'Less than 1 time per month'),
        ('1 - 3 times per month', '1 - 3 times per month'),
        ('1 - 2 times per week', '1 - 2 times per week'),
        ('3 - 6 times per week', '3 - 6 times per week'),
        ('7 or more times per week', '7 or more times per week'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    total_exposure = models.TextField(max_length=40, choices=total_exposure)
    asbestos_exposure = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    asbestos_exposure_duration = models.TextField(max_length=20, blank=True, null=True)
    asbestos_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure_duration = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    diesel = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    diesel_duration = models.TextField(max_length=20, blank=True, null=True)
    diesel_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    radon = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    radon_duration = models.TextField(max_length=20, blank=True, null=True)
    radon_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    cadmium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    cadmium_duration = models.TextField(max_length=20, blank=True, null=True)
    cadmium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    chromium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    chromium_duration = models.TextField(max_length=20, blank=True, null=True)
    chromium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coal_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    arsenic = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    arsenic_duration = models.TextField(max_length=20, blank=True, null=True)
    arsenic_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    nickel = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    nickel_duration = models.TextField(max_length=20, blank=True, null=True)
    nickel_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    plutonium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    plutonium_duration = models.TextField(max_length=20, blank=True, null=True)
    plutonium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    beryllium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    beryllium_duration = models.TextField(max_length=20, blank=True, null=True)
    beryllium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    ether = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    ether_duration = models.TextField(max_length=20, blank=True, null=True)
    ether_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    soot = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    soot_duration = models.TextField(max_length=20, blank=True, null=True)
    soot_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    welding = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    welding_duration = models.TextField(max_length=20, blank=True, null=True)
    welding_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    radiation = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    radiation_duration = models.TextField(max_length=20, blank=True, null=True)
    radiation_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    munitions = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    munitions_duration = models.TextField(max_length=20, blank=True, null=True)
    munitions_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    warfare = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    warfare_duration = models.TextField(max_length=20, blank=True, null=True)
    warfare_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    acheson = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    acheson_duration = models.TextField(max_length=20, blank=True, null=True)
    acheson_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    aluminum = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    aluminum_duration = models.TextField(max_length=20, blank=True, null=True)
    aluminum_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coal_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coke = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coke_duration = models.TextField(max_length=20, blank=True, null=True)
    coke_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal_gasification = models.TextField(max_length=20, blank=True, null=True)
    coal_gasification_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_gasification_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sulfur = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    sulfur_duration = models.TextField(max_length=20, blank=True, null=True)
    sulfur_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    mining = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    mining_duration = models.TextField(max_length=20, blank=True, null=True)
    mining_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    iron = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    iron_duration = models.TextField(max_length=20, blank=True, null=True)
    iron_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    painting = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    painting_duration = models.TextField(max_length=20, blank=True, null=True)
    painting_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    rubber = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    rubber_duration = models.TextField(max_length=20, blank=True, null=True)
    rubber_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    burn_pits = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    burn_pits_duration = models.TextField(max_length=20, blank=True, null=True)
    burn_pits_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    oil_fires = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    oil_fires_duration = models.TextField(max_length=20, blank=True, null=True)
    oil_fires_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sulfur_fires = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    sulfur_fires_duration = models.TextField(max_length=20, blank=True, null=True)
    sulfur_fires_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    atsugi = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    atsugi_duration = models.TextField(max_length=20, blank=True, null=True)
    atsugi_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sand_storms = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    sand_storms_duration = models.TextField(max_length=20, blank=True, null=True)
    sand_storms_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    job_held = models.TextField(max_length=20, blank=True, null=True)
    job_held_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_industry = models.TextField(max_length=20, blank=True, null=True)
    job_held_2 = models.TextField(max_length=20, blank=True, null=True)
    job_held_2_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_2_industry = models.TextField(max_length=20, blank=True, null=True)
    job_held_3 = models.TextField(max_length=20, blank=True, null=True)
    job_held_3_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_3_industry = models.TextField(max_length=20, blank=True, null=True)
    duration_outdoor_pollution = models.TextField(max_length=20, blank=True, null=True)
    duraiton_indoor_pollution = models.TextField(max_length=20, blank=True, null=True)
    cooking_location = models.TextField(max_length=20, blank=True, null=True)
    cooking_appliances = models.TextField(max_length=20, blank=True, null=True)
    cooking = models.TextField(max_length=20, blank=True, null=True)
    frequency_in_cooking_location = models.TextField(max_length=20, blank=True, null=True)
    kitchen_range = models.TextField(max_length=20, blank=True, null=True)
    kitchen_range_age = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_0_20_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_fuel = models.TextField(max_length=25, choices=cooking_fuel, blank=True, null=True)
    cooking_0_20_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_0_20_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_cooking_oil_homemade = models.TextField(max_length=2, blank=True, null=True)
    cooking_0_20_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_21_40_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_fuel = models.TextField(max_length=25, choices=cooking_fuel, blank=True, null=True)
    cooking_21_40_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_21_40_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_41_60_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_fuel = models.TextField(max_length=25, choices=cooking_fuel, blank=True, null=True)
    cooking_41_60_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_41_60_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_61_above_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_fuel = models.TextField(max_length=25, choices=cooking_fuel, blank=True, null=True)
    cooking_61_above_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_61_above_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    processed_meat_frequency = models.TextField(max_length=50, choices=eating_freq, blank=True, null=True)
    red_meat_frequency = models.TextField(max_length=50, choices=eating_freq, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Exposure3(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    home_1_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_1_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_1_country = models.TextField(max_length=20, blank=True, null=True)
    home_1_city = models.TextField(max_length=20, blank=True, null=True)
    home_1_province = models.TextField(max_length=20, blank=True, null=True)
    home_1_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_1_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_1_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_1_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_1_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_1_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_1_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_1_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_1_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_1_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_1_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_2_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_2_country = models.TextField(max_length=20, blank=True, null=True)
    home_2_city = models.TextField(max_length=20, blank=True, null=True)
    home_2_province = models.TextField(max_length=20, blank=True, null=True)
    home_2_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_2_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_2_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_2_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_2_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_2_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_2_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_2_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_2_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_3_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_3_country = models.TextField(max_length=20, blank=True, null=True)
    home_3_city = models.TextField(max_length=20, blank=True, null=True)
    home_3_province = models.TextField(max_length=20, blank=True, null=True)
    home_3_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_3_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_3_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_3_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_3_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_3_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_3_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_3_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_3_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_4_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_4_country = models.TextField(max_length=20, blank=True, null=True)
    home_4_city = models.TextField(max_length=20, blank=True, null=True)
    home_4_province = models.TextField(max_length=20, blank=True, null=True)
    home_4_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_4_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_4_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_4_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_4_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_4_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_4_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_4_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_4_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_5_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_5_country = models.TextField(max_length=20, blank=True, null=True)
    home_5_city = models.TextField(max_length=20, blank=True, null=True)
    home_5_province = models.TextField(max_length=20, blank=True, null=True)
    home_5_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_5_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_5_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_5_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_5_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_5_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_5_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_5_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_5_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_6_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_6_country = models.TextField(max_length=20, blank=True, null=True)
    home_6_city = models.TextField(max_length=20, blank=True, null=True)
    home_6_province = models.TextField(max_length=20, blank=True, null=True)
    home_6_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_6_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_6_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_6_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_6_housing_type = models.TextField(max_length=20, blank=True, null=True)
    home_6_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_6_water_src = models.TextField(max_length=20, blank=True, null=True)
    home_6_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_heat_src = models.TextField(max_length=20, blank=True, null=True)
    home_6_heat_src_other = models.TextField(max_length=20, blank=True, null=True)   

    def __str__(self):
        return self.total_exposure
    





class Mandatory_questionaire(models.Model):
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ("Prefer not to say", "Prefer not to say"),
    )
    sex_assinged_birth = (
        ('Male', 'Male'),
        ('Female', 'Female'),   
    )
    ethnicity = (
        ('Indigenous', 'Indigenous'),
        ('Middle Eastern', 'Middle Eastern'),
        ('African or Caribbean', 'African or Caribbean'),
        ('European', 'European'),
        ('Filipino', 'Filipino'),
        ('Jewish', 'Jewish'),
        ('Latin American', 'Latin American'),
        ('South Asian', 'South Asian'),
        ('Southeast Asian', 'Southeast Asian'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),     
     )
    born_in_canada_choice = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont know', 'Dont know'),
    )
    highest_education_lvl = (
        ('Less than high school', 'Less than high school'),
        ('High school graduate', 'High school graduate'),
        ('Post High School Training', 'Post High School Training'),
        ('Some college', 'Some college'),
        ('University degree', 'University degree'),
        ('Post graduate degree', 'Post graduate degree'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    )
   
    gender_surgery = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Prefer not to answer', 'Prefer not to answer'),
    )
    gender_hormone = (
        ('Feminizing', 'Feminizing'),
        ('Masculinizing', 'Masculinizing'),
    )
    height_unit = (
        ('cm', 'cm'),
        ('inches', 'inches'),
    )
    weight_unit = (
        ('kg', 'kg'),
        ('lbs', 'lbs'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    visit_date = models.DateField()
    date_of_birth = models.DateField()
    current_height = models.IntegerField()
    current_height_unit = models.TextField(max_length=20, choices=height_unit)
    current_weight = models.IntegerField()
    current_weight_unit = models.TextField(max_length=20, choices=weight_unit)
    sex_birth = models.TextField(max_length=200, choices=sex_assinged_birth)
    postal_code = models.TextField(max_length=6)
    current_age = models.IntegerField()
    gender_identity = models.TextField(max_length=200, choices=gender, null=True, blank=True)
    gender_surgery  = models.TextField(max_length=20, choices=gender_surgery, null=True, blank=True)
    gender_surgery_harmone = models.TextField(max_length=20, choices=gender_hormone, null=True, blank=True)
    gender_identity_other = models.TextField(max_length=20, null=True, blank=True)
    ethnicity = models.TextField(max_length=20, choices=ethnicity)
    ethnicity_other = models.TextField(max_length=20)
    born_in_canada = models.TextField(max_length=20, choices=born_in_canada_choice, null=True, blank=True)
    year_moved_to_canada = models.TextField(max_length=20)
    birthplace = models.TextField(max_length=20)
    highest_education_lvl = models.TextField(max_length=30, choices=highest_education_lvl)
    highest_education_lvl_other = models.TextField(max_length=20)
    copd = models.BooleanField(default=False)
    emphysema = models.BooleanField(default=False)
    chronic_bronchitis = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    adult_pneumonia = models.BooleanField(default=False)
    pulmonary_fibrosis = models.BooleanField(default=False)
    hiv = models.BooleanField(default=False)
    long_covid = models.BooleanField(default=False)
    personal_cancer_history = models.BooleanField(default=False)
    personal_cancer_history_youngest_age = models.TextField(max_length=20)
    personal_history_cancer_type = models.TextField(max_length=20)
    num_sisters = models.TextField(max_length=20)
    num_brothers = models.TextField(max_length=20)
    num_half_sisters = models.TextField(max_length=20)
    num_half_brothers = models.TextField(max_length=20)
    children = models.TextField(max_length=20)
    biological_relatives_cancer = models.BooleanField(default=False)

class biological_relatives_with_cancer(models.Model):
    mandatory_questionaire = models.ForeignKey(Mandatory_questionaire, on_delete=models.CASCADE)
    biological_relationship = models.TextField(max_length=20)
    type_of_cancer = models.TextField(max_length=20)
    diagnosis_age = models.TextField(max_length=20)


class Mandatory_questionaire_c(models.Model):
    waking_cigs = (
    ('After 60 min', 'After 60 min'),
    ('31-60 min', '31-60 min'),
    ('5-30 min', '5-30 min'),
    ('Within 5 min', 'Within 5 min'),
    )
    chew_snuff = (
        ('Never', 'Never'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly'),
    )   
    give_up = (
        ('First thing in the morning', 'First thing in the morning'),
        ('Any Other', 'Any Other'),
    )
    mode_of_use_choices = (
        ('Joints', 'Joints'),
        ('Pipe', 'Pipe'),
        ('Bong', 'Bong'),
    )
    unit_choices = (
        ('Joints', 'Joints'),
        ('Ounces', 'Ounces'),
        ('Hits', 'Hits'),
    )
    quantity_choices = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    smoked_more_100_cigs = models.BooleanField(default=False)
    age_regular_smoking = models.TextField(max_length=20)
    avg_cig_per_day = models.TextField(max_length=20)
    stopped_smoking = models.BooleanField(default=False)
    last_cig_date = models.TextField(max_length=20)
    last_cig_age = models.TextField(max_length=20)
    marajuana_use = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_1 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_1 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_1_quantity = models.TextField(max_length=20, null=True, blank=True, choices=quantity_choices)
    marajuana_use_age_1_mode = models.TextField(max_length=20, null=True, blank=True, choices=mode_of_use_choices)
    marajuana_use_age_1_units = models.TextField(max_length=20, null=True, blank=True, choices=unit_choices)
    marajuana_use_age_2 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_2 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_2_quantity = models.TextField(max_length=20, null=True, blank=True, choices=quantity_choices)
    marajuana_use_age_2_mode = models.TextField(max_length=20, null=True, blank=True, choices=mode_of_use_choices)
    marajuana_use_age_2_units = models.TextField(max_length=20, null=True, blank=True, choices=unit_choices)
    marajuana_use_age_3 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_3 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_quantity = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_mode = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_units = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_4 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_quantity = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_mode = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_units = models.TextField(max_length=20, null=True, blank=True)
    smoked_pipe = models.BooleanField(default=False)
    smoked_pipe_avg_ounces = models.TextField(max_length=20, null=True, blank=True)
    smoked_pipe_avg_age = models.TextField(max_length=20, null=True, blank=True)
    still_smoking_pipe = models.BooleanField(default=False)
    still_smoking_pipe_stop_date = models.TextField(max_length=20, null=True, blank=True)
    still_smoking_pipe_stop_age = models.TextField(max_length=20, null=True, blank=True)
    smoked_cigars = models.BooleanField(default=False)
    avg_num_cigars = models.TextField(max_length=20, null=True, blank=True)
    avg_cigar_age = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars_stop_date = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars_stop_age = models.TextField(max_length=20, null=True, blank=True)
    chewing_tobacco = models.TextField(max_length=20, choices=chew_snuff)
    chewing_tobacco_age = models.TextField(max_length=20, null=True, blank=True)
    chewing_tobacco_years = models.TextField(max_length=20, null=True, blank=True)
    snuff = models.TextField(max_length=20, choices=chew_snuff)
    snuff_age = models.TextField(max_length=20, null=True, blank=True)
    snuff_years = models.TextField(max_length=20, null=True, blank=True)
    vape = models.BooleanField(default=False)
    vape_num_times = models.TextField(max_length=20, null=True, blank=True)
    vape_start_date = models.TextField(max_length=20, null=True, blank=True)
    vape_stop_date = models.DateField(max_length=20, null=True, blank=True)
    vape_start_age = models.TextField(max_length=20, null=True, blank=True)
    still_vape = models.TextField(max_length=20, null=True, blank=True)
    still_vape_stop_age = models.TextField(max_length=20, null=True, blank=True)
    still_vape_stop_date = models.TextField(max_length=20, null=True, blank=True)
    vape_flavor = models.TextField(max_length=20, null=True, blank=True)
    cigs_waking_up = models.TextField(max_length=20, choices=waking_cigs)
    smoke_refrain = models.TextField(max_length=20, null=True, blank=True)
    cig_giveup = models.TextField(max_length=26, choices=give_up)
    smoke_morning = models.TextField(max_length=20, null=True, blank=True)
    smoke_sick = models.TextField(max_length=20, null=True, blank=True)
    quit_smoking = models.BooleanField(default=False)
    quit_smoking_times = models.TextField(max_length=20)

class Mandatory_questionaire_de(models.Model):
    second_hand_youth_choices = (
    ('Minimal or zero', 'Minimal or zero'),
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Heavy', 'Heavy'),
    )
    second_hand_smoke= (
        ('light', 'light'),
        ('moderate', 'moderate'),
        ('heavy', 'heavy'),
    )
    second_hand_home_choices = (
        ('Exposure at Home', 'Exposure at Home'),
        ('Exposure at Work', 'Exposure at Work'),
        ('Exposure During leisure activities', 'Exposure During leisure activities'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    second_hand_smoke = models.TextField(max_length=20, choices=second_hand_smoke, null=True, blank=True)
    second_hand_1yr = models.BooleanField(default=False, null=True, blank=True)
    second_hand_home = models.TextField(max_length=34, choices = second_hand_home_choices, null=True, blank=True)
    second_hand_work = models.TextField(max_length=20, null=True, blank=True)
    second_hand_leisure = models.TextField(max_length=20, null=True, blank=True)
    second_hand_daily = models.TextField(max_length=20, null=True, blank=True)
    second_hand_4days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_13days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_occasionally = models.TextField(max_length=20, null=True, blank=True)
    second_hand_2hrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand24hrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_46hrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_6hrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_yrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_freq = models.TextField(max_length=20, null=True, blank=True)
    second_hand_avg_exposure = models.TextField(max_length=20, null=True, blank=True)
    second_hand_youth = models.TextField(max_length=40, choices=second_hand_youth_choices, null=True, blank=True)
    alcohol = models.BooleanField(default=False, null=True, blank=True)
    alcohol_from_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_current = models.BooleanField(default=False, null=True, blank=True)
    alcohol_stop_age = models.TextField(max_length=20, null=True, blank=True)

class Mandatory_questionaire_fg(models.Model):
    medication_frequency = (
    ('Less than 1 time per month', 'Less than 1 time per month'),
    ('1 - 3 times per month', '1 - 3 times per month'),
    ('1 - 2 times per month', '1 - 2 times per month'),
    ('3 - 6 times per month', '3 - 6 times per month'),
    ('7 or more times per month', '7 or more times per month'),
    )
    working_situation = (
    ('Working', 'Working'),
    ('Retired', 'Retired'),
    ('Unemployed', 'Unemployed'), 
    ('Disabled', 'Disabled'),
    ('On extended sick leave', 'On extended sick leave'),
    ('Other', 'Other'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inhaled_drugs = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_day = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_month = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_year = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    bronchodialators = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_day = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_month = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_year = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    statins = models.TextField(max_length=20, null=True, blank=True)
    statins_day = models.TextField(max_length=20, null=True, blank=True)
    statins_month = models.TextField(max_length=20, null=True, blank=True)
    statins_year = models.TextField(max_length=20, null=True, blank=True)
    statins_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    metformin = models.TextField(max_length=20, null=True, blank=True)
    metformin_day = models.TextField(max_length=20, null=True, blank=True)
    metformin_month = models.TextField(max_length=20, null=True, blank=True)
    metformin_year = models.TextField(max_length=20, null=True, blank=True)
    metformin_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    current_working_situation = models.TextField(max_length=30, choices=working_situation)
    current_working_situation_other = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest = models.TextField(max_length=20, null=True, blank=True)    
    occupation_longest_activities = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest_years = models.TextField(max_length=20, null=True, blank=True)
    occupation_exposure = models.TextField(max_length=20, null=True, blank=True)
    occupation_fumes = models.TextField(max_length=20, null=True, blank=True)
    occupation_years = models.TextField(null=True, blank=True)




class Cat_5_findings(models.Model):
    CONDITION_CHOICES = (
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    )

    name = models.CharField(max_length=50, choices=CONDITION_CHOICES)

    def __str__(self):
        return self.name

class Emphysema_type(models.Model):
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]

    name = models.CharField(max_length=50, choices=emphysema_type)

    def __str__(self):
        return self.name

class Airways_type(models.Model):
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]

    name = models.CharField(max_length=50, choices=airways_type)

    def __str__(self):
        return self.name




class ct_scan(models.Model):
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
        ('actionable', 'actionable'),
        ('non-actionable', 'non-actionable'),
    )
    PLEURA_CHOICES = (
        ('effusion', 'Pleural Effusion'),
        ('asbestos', 'Asbestos-Related'),
    )
    ilst_categories = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    fu_dates = (
        (1, 1),
        (3, 3),
        (6, 6),
        (9, 9),
        (12, 12),
        (24, 24),
    )
    emphysema_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unclear', 'Unclear'),
        ('not assessed', 'Not Assessed'),
        ('not reported', 'Not Reported'),
    )
    emphysema_extent = (
        ('trivial', 'Trivial (<5%)'),
        ('mild', 'Mild (5-25%)'),
        ('moderate', 'Moderate (25-50%)'),
        ('marked', 'Marked (50-75%)'),
        ('severe', 'Severe (>75%)'),
    )

    emphysema_distrobution = (
        ('upper zone', 'Upper Zone'),
        ('lower zone', 'Lower Zone'),
        ('Diffuse or Homogenous', 'Diffuse / Homogenous'),
    )
    cor_art_calc = (
        ('absent', 'Absent'),
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    )
    airways = (
        ('normal', 'Normal'),
        ('abnormal', 'Abnormal'),

    )

    ct_scan_visit_id = (
        ('0', 'T0_Baseline'),
        ('1', 'T0_3_Months'),
        ('2', 'T0_6_Months'),
        ('3', 'T1_12_Months'),
        ('4', 'T2_24_Months'),
        ('5', 'T3_36_Months'),
        ('6', 'T4_48_Months'),
        ('7', 'T5_60_Months'),
    )

    yes_no = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE, null=False, blank=False)
    ct_scan_date = models.DateField(null=True, blank=True)
    ct_scan_visitID = models.TextField(max_length=20, choices=ct_scan_visit_id, default=None, blank=True)
    ct_scan_location = models.TextField(max_length=20, blank=True)
    ct_scan_radiologist = models.TextField(max_length=20, blank=True)
    ct_scan_review_date = models.DateField(null=True, blank=True)
    ct_scan_familty_history = models.BooleanField(null=True, blank=True)
    ct_scan_pt_lung_cancer = models.BooleanField(null=True, blank=True)
    ct_scan_dlp = models.TextField(max_length=20, blank=True)
    radiologist_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    radiologist_fu_mnths_date = models.DateField(null=True, blank=True)
    cad_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    cad_fu_mnths_date = models.DateField(null=True, blank=True)
    ilst_cat = models.IntegerField(choices=ilst_categories, null=True, blank=True)
    final_rec_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    final_rec_fu_mnths_date = models.DateField(null=True, blank=True)
    copd_emphysema = models.TextField(max_length=20, choices=emphysema_choices, default=None)
    copd_emphysema_extent = models.TextField(max_length=20, choices=emphysema_extent, default=None)
    copd_emphysema_type = models.ManyToManyField(Emphysema_type, blank=True)
    copd_emphysema_distribution = models.TextField(max_length=45, choices=emphysema_distrobution, default=None)
    cor_art_calc = models.TextField(max_length=20, choices=cor_art_calc, default=None, blank=True)
    cor_art_agatson = models.TextField(max_length=20)
    airways = models.TextField(max_length=20, choices=airways, default=None)
    airways_type = models.ManyToManyField(Airways_type, blank=True)
    airways_type_muc_impaction = models.TextField(max_length=20, blank=True)
    aiways_type_wall_thickening = models.TextField(max_length=20, blank=True)
    airways_type_bronchiectasis = models.TextField(max_length=20, blank=True)
    ariways_type_bronchiolectasis = models.TextField(max_length=20, blank=True)
    #cat_5_findings = models.TextField(max_length=22, choices=cat_5_findings, default=None, blank=True)
    cat_5_findings = models.ManyToManyField(Cat_5_findings, blank=True)
    cat_5_lymph_nodes = models.TextField(max_length=20, blank=True)
    cat_5_suspicious_nodes = models.TextField(max_length=20, blank=True)
    cat_5_endobronchial = models.TextField(max_length=20, blank=True)
    cat_5_comments = models.TextField(max_length=20, blank=True)
    other_cardiovascular = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_cardiovascular_comments = models.TextField(max_length=20, blank=True)
    other_vertebral = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_vertebral_comments = models.TextField(max_length=20, blank=True)
    other_GI = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_GI_comments = models.TextField(max_length=20, blank=True)
    other_breast = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_breast_comments = models.TextField(max_length=20, blank=True)
    other_endocrine = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_endocrine_comments = models.TextField(max_length=20, blank=True)
    other_lymph = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_lymph_comments = models.TextField(max_length=20, blank=True)
    other_pleura = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_pleura_comments = models.TextField(max_length=20, choices=PLEURA_CHOICES, default=None, blank=True)
    other_pulmonary_fibrosis = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_pulmonary_fibrosis_comments = models.TextField(max_length=20, blank=True)
    other_musculoskeletal = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_musculoskeletal_comments = models.TextField(max_length=20, blank=True)
    other_other = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_other_comments = models.TextField(max_length=20, blank=True)
    general_comments = models.TextField(max_length=200, blank=True)


"""     participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    ct_scan_date = models.DateField()
    ct_scan_visitID = models.TextField(max_length=20, choices=ct_scan_visit_id, default=None)
    ct_scan_location = models.TextField(max_length=20)
    ct_scan_radiologist = models.TextField(max_length=20)
    ct_scan_review_date = models.DateField()
    ct_scan_familty_history = models.BooleanField()
    ct_scan_pt_lung_cancer = models.BooleanField()
    ct_scan_dlp = models.TextField(max_length=20)
    radiologist_fu_mnths = models.IntegerField(choices=fu_dates)
    radiologist_fu_mnths_date = models.DateField()
    cad_fu_mnths = models.IntegerField(choices=fu_dates)
    cad_fu_mnths_date = models.DateField()
    ilst_cat = models.IntegerField(choices=ilst_categories)
    final_rec_fu_mnths = models.IntegerField(choices=fu_dates)
    final_rec_fu_mnths_date = models.DateField()
    copd_emphysema = models.TextField(max_length=20, choices=emphysema_choices, default=None)
    copd_emphysema_extent = models.TextField(max_length=20, choices=emphysema_extent, default=None)
    copd_emphysema_type = models.TextField(max_length=20, choices=emphysema_type, default=None)
    copd_emphysema_distribution = models.TextField(max_length=45, choices=emphysema_distrobution, default=None)
    cor_art_calc = models.TextField(max_length=20, choices=cor_art_calc)
    cor_art_agatson = models.TextField(max_length=20)
    airways = models.TextField(max_length=20, choices=airways, default=None)
    airways_type = models.TextField(max_length=20, choices=airways_type, default=None)
    airways_type_muc_impaction = models.TextField(max_length=20)
    aiways_type_wall_thickening = models.TextField(max_length=20)
    airways_type_bronchiectasis = models.TextField(max_length=20)
    ariways_type_bronchiolectasis = models.TextField(max_length=20)
    cat_5_findings = models.TextField(max_length=22, choices=cat_5_findings, default=None)
    cat_5_lymph_nodes = models.TextField(max_length=20)
    cat_5_suspicious_nodes = models.TextField(max_length=20)
    cat_5_endobronchial = models.TextField(max_length=20)
    cat_5_comments = models.TextField(max_length=20)
    other_cardiovascular = models.TextField(max_length=20, choices=findings_choices, default=None)
    other_cardiovascular_comments = models.TextField(max_length=20)
    other_vertebral = models.TextField(max_length=20, choices=findings_choices)
    other_vertebral_comments = models.TextField(max_length=20)
    other_GI = models.TextField(max_length=20, choices=findings_choices)
    other_GI_comments = models.TextField(max_length=20)
    other_breast = models.TextField(max_length=20, choices=findings_choices)
    other_breast_comments = models.TextField(max_length=20)
    other_endocrine = models.TextField(max_length=20, choices=findings_choices)
    other_endocrine_comments = models.TextField(max_length=20)
    other_lymph = models.TextField(max_length=20, choices=findings_choices)
    other_lymph_comments = models.TextField(max_length=20)
    other_pleura = models.TextField(max_length=20, choices=findings_choices)
    other_pleura_comments = models.TextField(max_length=20, choices=PLEURA_CHOICES, default=None)
    other_pulmonary_fibrosis = models.TextField(max_length=20, choices=findings_choices, default=None)
    other_pulmonary_fibrosis_comments = models.TextField(max_length=20)
    other_musculoskeletal = models.TextField(max_length=20, choices=findings_choices, default=None)
    other_musculoskeletal_comments = models.TextField(max_length=20)
    other_other = models.TextField(max_length=20, choices=findings_choices, default=None)
    other_other_comments = models.TextField(max_length=20)
    general_comments = models.TextField(max_length=200) """


class ct_scan_nodule_1(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('solid', 'Solid'),
        ('SSN', 'SSN'),
        ('GGO', 'GGO'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=1)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_2(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('solid', 'Solid'),
        ('SSN', 'SSN'),
        ('GGO', 'GGO'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=2)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_3(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('solid', 'Solid'),
        ('SSN', 'SSN'),
        ('GGO', 'GGO'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=3)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_4(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('solid', 'Solid'),
        ('SSN', 'SSN'),
        ('GGO', 'GGO'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=4)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)
    def str(self):
        return self.ct_scan_date

class ct_scan_nodule_5(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('solid', 'Solid'),
        ('SSN', 'SSN'),
        ('GGO', 'GGO'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=5)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)
# class protocol_deviations(models.Model):
#     participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
#     protocol_deviation_1 = models.TextField(max_length=20)
#     protocol_deviation_2 = models.TextField(max_length=20)
#     protocol_deviation_3 = models.TextField(max_length=20)
#     protocol_deviation_4 = models.TextField(max_length=20)
#     protocol_deviation_5 = models.TextField(max_length=20)
#     protocol_deviation_6 = models.TextField(max_length=20)
#     protocol_deviation_7 = models.TextField(max_length=20)
#     protocol_deviation_8 = models.TextField(max_length=20)
#     protocol_deviation_9 = models.TextField(max_length=20)
#     protocol_deviation_10 = models.TextField(max_length=20)


#test view
class MyForm(models.Model):
    variable1 = models.CharField(max_length=100)
    variable2 = models.CharField(max_length=100)
    variable3 = models.CharField(max_length=100)

class CancerHistory(models.Model):
    biological_rel = models.TextField(max_length=20)
    type_of_cancer = models.TextField(max_length=20)
    age_diagnosis = models.TextField(max_length=20)



class inclusion(models.Model):
    inclusion_status_choices = (
        ('eligible and willing to participate', 'eligible and willing to participate'),
        ('eligible but unwilling to participate', 'eligible but unwilling to participate'),
        ('ineligible', 'ineligible'),
        ('ineligible but willing to participate', 'ineligible but willing to participate'),

    )
    consent_status_choices = (
        ('consented', 'consented'),
        ('not consented', 'not consented'),
    )
    screening = (
        ('enrolled', 'enrolled'),
        ('pending interview', 'pending interview'),
        ('pending enrollment', 'pending enrollment'),
        ('ineligible', 'ineligible'),
        ('declined study', 'declined study'),
        ('off study', 'off study'),
        ('confirmed study', 'confirmed study'),
    )
    participant_status = (
        ('group 1', 'group 1'),
        ('group 2', 'group 2'),
        ('group 3', 'group 3'),
    )

    participant_number = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inclusion_criteria_1 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_2 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_3 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_4 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_5 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_6 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_7 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_8 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_9 = models.BooleanField(null=True, blank=True)
    inclusion_criteria_9_a = models.BooleanField(null=True, blank=True)
    inclusion_criteria_9_b = models.BooleanField(null=True, blank=True)
    inclusion_criteria_9_c = models.BooleanField(null=True, blank=True)
    inclusion_criteria_9_d = models.BooleanField(null=True, blank=True)
    inclusion_status = models.TextField(max_length=80, choices=inclusion_status_choices, null=True, blank=True)
    screening_status = models.TextField(max_length=50, choices=screening, null=True, blank=True)
    consent_status = models.TextField(max_length=20, choices=consent_status_choices, null=True, blank=True)


class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    field_name = models.CharField(max_length=100, null=True, blank=True)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content_type} #{self.object_id} - {self.field_name}: {self.old_value} -> {self.new_value}"






class PLCO_score(models.Model):

    education_choices = (
        ('Less than High school graduate', 'Less than High school graduate'),
        ('High school graduate', 'High school graduate'),
        ('Post high school training', 'Post high school training'),
        ('Some college', 'Some college'),
        ('College graduate', 'College graduate'),
        ('Postgraduate', 'Postgraduate'),
    )
    race_choices = (
        ('White, Hispanic, Asian, Other', 'White, Hispanic, Asian, Other'),
        ('Black', 'Black'),
        ('First Nations', 'First Nations'),
    )




    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    education = models.TextField(max_length=60, choices=education_choices)
    bmi = models.TextField(max_length=20)
    copd = models.BooleanField(default=False)
    cancer_history = models.BooleanField(default=False)
    lung_cancer_history = models.BooleanField(default=False)
    race = models.TextField(max_length=50, choices=race_choices)
    smoking_status = models.BooleanField(default=False)
    avg_num_cigs_smoked_day = models.TextField(max_length=20)
    duration_smoked = models.TextField(max_length=20)
    years_quit = models.TextField(max_length=20)
    




class Protocol_Deviations(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    deviation_type = models.TextField(max_length=20)
    deviation_date = models.DateField()
    clinical_staff_notified = models.BooleanField(default=False)
    deviation_comments = models.TextField(max_length=200)
    