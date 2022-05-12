from multiprocessing.dummy import current_process
from os import curdir
import re
import django
from django.db import connection
from django.shortcuts import redirect, render
import cx_Oracle
from .models import *

def index(request):
    return render(request, 'hotel_app/index.html')

def reserve(request):
    return render(request, 'hotel_app/reserve.html')

def show_room(request):
    r_type = request.POST['type']
    r_size = request.POST['p_number']
    cursor = connection.cursor()
    sql="""SELECT * FROM HOTEL_APP_ROOMS
            WHERE room_type = '%s' AND 
            room_size = '%s' AND is_aviable = 'yes'
            AND ROWNUM < 2
        """ % (r_type, r_size)

    cursor.execute(sql)
    rooms = []
    for room in cursor:
        rooms.append(room)
    title = "Aviable rooms"
    if len(rooms) == 0 :
        title = "No aviable rooms"

    return render(request, 'hotel_app/show_room.html', context={'rooms':rooms, 'title':title})


def add_reserve(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    rid = request.POST['rid']
    result = 'Added reserve!'
    if fname == '':
        result = "Your name is empty"
    else:
        ik = Guests.objects.count()+1
        g = Guests(guest_id=ik ,first_name=fname, last_name=lname)
        g.save()

        rms = Rooms.objects.get(room_id=rid)
        ir = Reservations.objects.count()+1
        serv = Service.objects.get(service_name='Food')
        srg = Service_group(service_group_id = 1, service = serv)
        srg.save()
        r = Reservations(guest_id=g, room_id = rms, start_date = '2022-05-12', end_date='2022-05-13', service_group=srg, total_cost = 0)
        r.save()
        cursor = connection.cursor()
        t_cost = cursor.callfunc("get_cost", int, [rid,5])
        r.total_cost = t_cost
        r.save()
    
    return render(request, 'hotel_app/result.html', context={'result':result})


def reserves(request):
    cursor = connection.cursor()
    sql ="""
        SELECT first_name, last_name, room_type, room_size
        FROM hotel_app_reservations JOIN hotel_app_guests
        ON hotel_app_reservations.guest_id_id = hotel_app_guests.guest_id
        JOIN hotel_app_rooms ON hotel_app_reservations.room_id_id = hotel_app_rooms.room_id
    """

    sql2="""
        SELECT * FROM hotel_app_rooms
        where is_aviavle = 'no';
    """

    cursor.execute(sql)
    reserves = []
    for row in cursor:
        reserves.append(row)
    
    return render(request, 'hotel_app/reserves.html',context={'reserves':reserves})