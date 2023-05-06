from django.db import models


class person_user(models.Model):
    email_address = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'person_user'

class agent(models.Model):
    email_address = models.CharField('person_user', primary_key=True)
    agency = models.CharField(max_length=25)
    license_number = models.CharField(max_length=5)
    commission_rate = models.CharField(max_length=4)


    class Meta:
        db_table = 'agent'

class perspective_renter(models.Model):
    email_address = models.CharField('person_user', primary_key=True)
    desired_move_in_date = models.DateField()
    preferred_location_city = models.CharField(max_length=20)
    preferred_location_state = models.CharField(max_length=15)
    budget = models.IntegerField()

    class Meta:
        db_table = 'perspective_renter'


class property(models.Model):
    property_id = models.AutoField(primary_key=True)
    agency = models.CharField(max_length=15)
    location_address = models.CharField(max_length=20)
    location_city = models.CharField(max_length=20)
    location_state = models.CharField(max_length=15)
    availability = models.DateField()
    listing_type=models.CharField(max_length=10)
    building_type=models.CharField(max_length=15)
    class Meta:
        db_table = 'property'


class house(models.Model):
    property_id = models.IntegerField('property', primary_key=True)
    number_of_rooms = models.IntegerField()
    square_footage = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    class Meta:
        db_table = 'house'


class apartment(models.Model):
    property_id = models.IntegerField('property', primary_key=True)
    number_of_rooms = models.IntegerField()
    square_footage = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    class Meta:
        db_table = 'apartment'


class commercial_building(models.Model):
    property_id = models.IntegerField('property', primary_key=True)
    square_footage = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=200)
    type_of_business = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = 'commercial_building'


class credit_card(models.Model):
    email_address = models.CharField('person_user')
    card_number = models.CharField(primary_key=True,  max_length=19)
    billing_address = models.CharField(max_length=35)
    cardholder_name = models.CharField(max_length=25)

    class Meta:
        db_table = 'credit_card'


class booking(models.Model):
    property_id = models.IntegerField('property', primary_key=True)
    start_booking_date = models.DateField()
    end_booking_date = models.DateField()
    card_number = models.CharField('credit_card', max_length=19)
    email_address = models.CharField('person_user')
    class Meta:
        db_table = 'booking'


class email_address_telephone(models.Model):
    email_address = models.CharField('person_user', primary_key=True)
    telephone = models.CharField(max_length=16)

    class Meta:
        db_table = 'email_address_telephone'


class user_address(models.Model):
    email_address = models.CharField('person_user', primary_key=True, default=None)
    street_street_number = models.CharField(max_length=5)
    street_street_name = models.CharField(max_length=20)
    street_apt_number = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=5)

    class Meta:
        db_table = 'user_address'

class house_location(models.Model):
    house_location_id = models.IntegerField(primary_key=True)
    street_street_number = models.CharField(max_length=5)
    street_street_name = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)

    class Meta:
        db_table = 'house_location'


class apartment_location(models.Model):
    apartment_location_id = models.IntegerField(primary_key=True)
    street_street_number = models.CharField(max_length=5)
    street_street_name = models.CharField(max_length=20)
    street_apt_number = models.CharField(max_length=5)
    zip = models.CharField(max_length=5)

    class Meta:
        db_table = 'apartment_location'



class commercial_building_location(models.Model):
    commercial_building_location_id = models.IntegerField(primary_key=True)
    street_street_number = models.CharField(max_length=5)
    street_street_name = models.CharField(max_length=20)
    street_apt_number = models.CharField(max_length=5)
    zip = models.CharField(max_length=5)

    class Meta:
        db_table = 'commercial_building_location'
