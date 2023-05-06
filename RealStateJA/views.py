from django.shortcuts import render, redirect
from .models import person_user, user_address, agent, perspective_renter, email_address_telephone, credit_card, property, apartment, house, commercial_building, booking
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages


def home(request):
    return render(request, 'RealStateJA/home.html')

def renter(request):
    return render(request, 'RealStateJA/renter.html')

def agentview(request):
    return render(request, 'RealStateJA/agentview.html')

def success_view(request):
    return render(request, 'RealStateJA/success.html')

def billingsuccess(request):
    return render(request, 'RealStateJA/billingsuccess.html')

def addsuccess(request):
    return render(request, 'RealStateJA/addsuccess.html')

def propertysuccess(request):
    return render(request, 'RealStateJA/propertysuccess.html')

def propertyselection(request):
    return render(request, 'RealStateJA/propertyselection.html')

def housesearch(request):
    return render(request, 'RealStateJA/housesearch.html')

def apartmentsearch(request):
    return render(request, 'RealStateJA/apartmentsearch.html') 

def commercialsearch(request):
    return render(request, 'RealStateJA/commercialsearch.html')

def bookagent(request):
    return render(request, 'RealStateJA/bookagent.html')       



def custom_user_creation_view(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email_address = request.POST.get('email_address')
        telephone = request.POST.get('telephone')
        street_street_number = request.POST.get('street_street_number')
        street_street_name = request.POST.get('street_street_name')
        street_apt_number = request.POST.get('street_apt_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        user_type = request.POST.get('user_type')

        # Check if the user already exists
        existing_user = person_user.objects.filter(email_address=email_address).first()
        if existing_user:
            # Handle existing user error
            error_message = 'User already exists.'
            return render(request, 'RealStateJA/signup.html', {'error_message': error_message})


        new_user = person_user.objects.create(
            email_address=email_address,
            name=name
        )

        new_user_address = user_address.objects.create(
            street_street_number=street_street_number,
            street_street_name=street_street_name,
            street_apt_number=street_apt_number,
            city=city,
            state=state,
            zip=zip,
            email_address=new_user.email_address
        )

        new_user_telephone = email_address_telephone.objects.create(
            email_address=new_user.email_address,
            telephone=telephone,)


        # Create a new Agent or Renter object, depending on user_type
        if user_type == 'agent':
            new_agent = agent.objects.create(
                email_address=new_user.email_address,
                agency=request.POST.get('agency'),
                license_number=request.POST.get('license_number'),
                commission_rate=request.POST.get('commission_rate'),
            )
        elif user_type == 'renter':
            new_perspective_renter = perspective_renter.objects.create(
                email_address=new_user.email_address,
                desired_move_in_date=request.POST.get('desired_move_in_date'),
                preferred_location_city=request.POST.get('preferred_location_city'),
                preferred_location_state=request.POST.get('preferred_location_state'),
                budget=request.POST.get('budget'),
            )
            new_credit_card = credit_card.objects.create(
                email_address=new_user.email_address,
                card_number=request.POST.get('card_number'),
                billing_address=request.POST.get('billing_address'),
                cardholder_name=request.POST.get('cardholder_name'),
            )
        return redirect(reverse_lazy('success'))

    return render(request, 'RealStateJA/signup.html')


def payinfomod(request):
    if request.method == 'POST':
        email_address = request.POST['email_address']
        card_number = request.POST['card_number']
        billing_address = request.POST['billing_address']
        cardholder_name = request.POST['cardholder_name']

        # Check if the email exists in person_user table
        try:
            user = person_user.objects.get(email_address=email_address)
        except person_user.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, 'RealStateJA/payinfomod.html', {'error_message': error_message})

        # Check if the credit card exists in the credit_card table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM credit_card WHERE email_address=%s", [email_address])
            row = cursor.fetchone()
            if row:
                # Update the row with new information
                cursor.execute("UPDATE credit_card SET card_number=%s, billing_address=%s, cardholder_name=%s WHERE email_address=%s", [card_number, billing_address, cardholder_name, email_address])
                return redirect(reverse_lazy('billingsuccess'))
            else:
                # Insert new row
                cursor.execute("INSERT INTO credit_card (email_address, card_number, billing_address, cardholder_name) VALUES (%s, %s, %s, %s)", [email_address, card_number, billing_address, cardholder_name])
                return redirect(reverse_lazy('billingsuccess'))

        return redirect('payinfomod')

    return render(request, 'RealStateJA/payinfomod.html')


def addinfomod(request):
    if request.method == 'POST':
        email_address = request.POST['email_address']
        street_street_number = request.POST['street_street_number']
        street_street_name = request.POST['street_street_name']
        street_apt_number = request.POST['street_apt_number']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']

        # Check if the email exists in person_user table
        try:
            user = person_user.objects.get(email_address=email_address)
        except person_user.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, 'RealStateJA/addinfomod.html', {'error_message': error_message})

        # Check if the credit card exists in the credit_card table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_address WHERE email_address=%s", [email_address])
            row = cursor.fetchone()
            if row:
                # Update the row with new information
                cursor.execute("UPDATE user_address SET street_street_number=%s, street_street_name=%s, street_apt_number=%s, city=%s, state=%s, zip=%s WHERE email_address=%s", [street_street_number, street_street_name, street_apt_number, city, state, zip, email_address])
                return redirect(reverse_lazy('addsuccess'))
            else:
                # Insert new row
                cursor.execute("INSERT INTO credit_card (email_address, street_street_number, street_street_name, street_apt_number, city, state, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)", [email_address, street_street_number, street_street_name, street_apt_number, city, state, zip])
                return redirect(reverse_lazy('addsuccess'))

        return redirect('addinfomod')

    return render(request, 'RealStateJA/addinfomod.html')


def add_property(request):
    if request.method == 'POST':
        # Get the form data
        agency = request.POST.get('agency')
        location_address = request.POST.get('location_address')
        location_city = request.POST.get('location_city')
        location_state = request.POST.get('location_state')
        listing_type = request.POST.get('listing_type')
        availability = request.POST.get('availability')
        building_type = request.POST.get('building_type')
        square_footage = request.POST.get('square_footage')
        description = request.POST.get('description')
        price= request.POST.get('price')
        number_of_rooms = request.POST.get('number_of_rooms')


        new_property = property.objects.create(
            agency = agency,
            location_address = location_address,
            location_city = location_city,
            location_state = location_state,
            availability = availability,
            listing_type=listing_type,
            building_type=building_type,
        )

        # Create a new House, Apartment or Commercial object, depending on building_type
        if building_type == 'House':
            new_house = house.objects.create(
                property_id=new_property.property_id,
                number_of_rooms=number_of_rooms,
                square_footage=square_footage,
                description=description,
                price=price,
            )
        elif building_type == 'Apartment':
            new_apartment = apartment.objects.create(
                property_id=new_property.property_id,
                number_of_rooms=request.POST.get('number_of_rooms'),
                square_footage=square_footage,
                description=description,
                price=price
            )
        elif building_type == 'Commercial':
            new_commercial = commercial_building.objects.create(
                property_id=new_property.property_id,
                square_footage=square_footage,
                type_of_business=request.POST.get('type_of_business'),
                description=description,
                price=price
            )

        return redirect(reverse_lazy('propertysuccess'))

    return render(request, 'RealStateJA/propertyview.html')


from django.shortcuts import render
from django.db.models import Q
import datetime

from django.db import connection
from django.shortcuts import render

def housesearch(request):
    location = request.GET.get('location')
    agency = request.GET.get('agency')
    num_rooms = request.GET.get('num_rooms')
    price = request.GET.get('price')
    availability = request.GET.get('availability')
    listing_type = request.GET.get('listing_type')

    with connection.cursor() as cursor:
        query = '''
            SELECT p.property_id, p.agency, p.location_address, p.location_city, p.location_state,
                   p.availability, p.listing_type, p.building_type,
                   h.number_of_rooms, h.square_footage, h.description, h.price
            FROM property p
            INNER JOIN house h ON p.property_id = h.property_id
            WHERE 1=1
        '''
        params = []
        if location:
            query += ' AND p.location_city LIKE %s'
            params.append(f'%{location}%')
        if agency:
            query += ' AND p.agency LIKE %s'
            params.append(f'%{agency}%')
        if num_rooms:
            query += ' AND h.number_of_rooms = %s'
            params.append(num_rooms)
        if price:
            query += ' AND h.price <= %s'
            params.append(price)
        if availability:
            query += ' AND p.availability <= %s'
            params.append(availability)
        if listing_type:
            query += ' AND p.listing_type = %s'
            params.append(listing_type)

        cursor.execute(query, params)
        results = cursor.fetchall()

    context = {'houses': results}
    return render(request, 'RealStateJA/housesearch.html', context)


def apartmentsearch(request):
    location = request.GET.get('location')
    agency = request.GET.get('agency')
    num_rooms = request.GET.get('num_rooms')
    price = request.GET.get('price')
    availability = request.GET.get('availability')
    listing_type = request.GET.get('listing_type')

    with connection.cursor() as cursor:
        query = '''
            SELECT p.property_id, p.agency, p.location_address, p.location_city, p.location_state,
                   p.availability, p.listing_type, p.building_type,
                   h.number_of_rooms, h.square_footage, h.description, h.price
            FROM property p
            INNER JOIN apartment h ON p.property_id = h.property_id
            WHERE 1=1
        '''
        params = []
        if location:
            query += ' AND p.location_city LIKE %s'
            params.append(f'%{location}%')
        if agency:
            query += ' AND p.agency LIKE %s'
            params.append(f'%{agency}%')
        if num_rooms:
            query += ' AND h.number_of_rooms = %s'
            params.append(num_rooms)
        if price:
            query += ' AND h.price <= %s'
            params.append(price)
        if availability:
            query += ' AND p.availability <= %s'
            params.append(availability)
        if listing_type:
            query += ' AND p.listing_type = %s'
            params.append(listing_type)

        cursor.execute(query, params)
        results = cursor.fetchall()

    context = {'apartments': results}
    return render(request, 'RealStateJA/apartmentsearch.html', context)


def commercialsearch(request):
    location = request.GET.get('location')
    agency = request.GET.get('agency')
    type_of_business = request.GET.get('type_of_business')
    price = request.GET.get('price')
    availability = request.GET.get('availability')
    listing_type = request.GET.get('listing_type')

    with connection.cursor() as cursor:
        query = '''
            SELECT p.property_id, p.agency, p.location_address, p.location_city, p.location_state,
                   p.availability, p.listing_type, p.building_type,
                   h.square_footage, h.type_of_business, h.description, h.price
            FROM property p
            INNER JOIN commercial_building h ON p.property_id = h.property_id
            WHERE 1=1
        '''
        params = []
        if location:
            query += ' AND p.location_city LIKE %s'
            params.append(f'%{location}%')
        if agency:
            query += ' AND p.agency LIKE %s'
            params.append(f'%{agency}%')
        if type_of_business:
            query += ' AND h.type_of_business = %s'
            params.append(type_of_business)
        if price:
            query += ' AND h.price <= %s'
            params.append(price)
        if availability:
            query += ' AND p.availability <= %s'
            params.append(availability)
        if listing_type:
            query += ' AND p.listing_type = %s'
            params.append(listing_type)

        cursor.execute(query, params)
        results = cursor.fetchall()

    context = {'commercials': results}
    return render(request, 'RealStateJA/commercialsearch.html', context)

def book(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        email_address = request.POST['email_address']
        start_booking_date = request.POST['start_booking_date']
        end_booking_date = request.POST['end_booking_date']
        card_number_user = credit_card.objects.get(email_address=email_address)
        card_number = card_number_user.card_number
        
        # Check if the email exists in person_user table
        try:
            user = person_user.objects.get(email_address=email_address)
        except person_user.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, 'RealStateJA/book.html', {'error_message': error_message})

        try:
            propertyexist = property.objects.get(property_id=property_id)
        except property.DoesNotExist:
            error_message1 = 'Property does not exist'
            return render(request, 'RealStateJA/book.html', {'error_message': error_message1})

        # Check if the property is already booked
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM booking WHERE property_id=%s", [property_id])
            row = cursor.fetchone()
            if row:
                error_message = 'Property not available'
                return render(request, 'RealStateJA/book.html', {'error_message': error_message})
            else:
                # Insert new row
                cursor.execute("INSERT INTO booking (property_id, start_booking_date, end_booking_date, card_number, email_address) VALUES (%s, %s, %s, %s, %s)", [property_id, start_booking_date, end_booking_date, card_number, email_address])
                return redirect(reverse_lazy('successfulbooking'))

        return redirect('book')

    return render(request, 'RealStateJA/book.html')

def successfulbooking(request):
    last_booking = booking.objects.last()
    context = {'booking': last_booking}
    return render(request, 'RealStateJA/successfulbooking.html', context)

def propertymanage(request):
    last_booking = booking.objects.last()
    context = {'booking': last_booking}
    return render(request, 'successfulbooking.html', context)

def bookrent(request):
    return render(request, 'RealStateJA/bookrent.html')

def managebookingsr(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        email_address = request.POST['email_address']
        try:
            user = booking.objects.get(email_address=email_address)
        except booking.DoesNotExist:
            error_message = 'No reservation under this email address'
            return render(request, 'RealStateJA/managebookingsr.html', {'error_message': error_message})
        try:
            prop = booking.objects.get(property_id=property_id)
        except booking.DoesNotExist:
            error_message1 = 'No reservation for thi property'
            return render(request, 'RealStateJA/managebookingsr.html', {'error_message': error_message1})
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM booking WHERE email_address = %s AND property_id = %s", [email_address, property_id])
            return redirect(reverse_lazy('bookdeleter'))
    return render(request, 'RealStateJA/managebookingsr.html')

def bookdeleter(request):
    return render(request, 'RealStateJA/bookdeleter.html')

def bookview(request):
    
    email_address = request.GET.get('email_address')
    property_id = request.GET.get('property_id')
    with connection.cursor() as cursor:
        cursor.execute("SELECT property_id, email_address, start_booking_date, end_booking_date, card_number FROM booking WHERE email_address = %s and property_id=%s", [email_address, property_id])
        results = cursor.fetchall()

    context = {'bookinglist': results}
    return render(request, 'RealStateJA/bookview.html', context)


def managebookinga(request):
    agency = request.GET.get('agency')
    with connection.cursor() as cursor:
        cursor.execute("SELECT b.property_id, b.email_address, b.start_booking_date, b.end_booking_date, b.card_number, p.agency, p.location_city, p.building_type FROM booking b INNER JOIN property p ON b.property_id = p.property_id WHERE p.agency=%s", [agency])
        results = cursor.fetchall()

    context = {'properties': results}
    return render(request, 'RealStateJA/managebookinga.html', context)


def agentcancel(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        agency = request.POST['agency']
        try:
            user = booking.objects.get(property_id=property_id)
        except booking.DoesNotExist:
            error_message = 'No existing bookings'
            return render(request, 'RealStateJA/agentcancel.html', {'error_message': error_message})
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM booking WHERE property_id = %s", [property_id])
            return redirect(reverse_lazy('bookdeleter'))
    return render(request, 'RealStateJA/agentcancel.html')