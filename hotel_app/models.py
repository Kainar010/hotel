from django.db import models

class Rooms(models.Model):
    room_id = models.IntegerField()
    room_type = models.CharField(max_length=12)
    room_size = models.CharField(max_length=12)
    room_price = models.IntegerField()
    is_aviable = models.CharField(max_length=12)

    def __self__(self):
        return self.is_aviable


class Guests(models.Model):
    guest_id = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __self__(self):
        return self.fisrt_name+' '+self.last_name


class Reservations(models.Model):
    guest_id = models.ForeignKey('Guests', on_delete=models.CASCADE, null=True)
    room_id = models.ForeignKey('Rooms', on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    service_group = models.ForeignKey('Service_group', on_delete=models.CASCADE, null=True)
    total_cost = models.IntegerField()


class Service(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=255)
    service_price = models.IntegerField()


class Service_group(models.Model):
    service_group_id = models.IntegerField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True)
