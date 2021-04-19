from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BookaTable(models.Model):

    name = models.CharField(max_length=100, null=True, help_text="Enter your name")
    email = models.EmailField(max_length=100,null=True, help_text="Enter your email")
    phone = models.CharField(max_length=10, null=True,help_text="Enter your phone number")
    Date = models.DateField(auto_now_add=True, help_text="Date")
    Time = models.TimeField(auto_now_add=True, help_text="Time")
    number_of_people = models.IntegerField(null=True, help_text="Enter number of people")
    message = models.TextField(max_length=100, null=True, help_text="Description")

    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(max_length=100, null=True, help_text="Enter your name")
    email = models.EmailField(max_length=100, null=True, help_text="Enter your email")
    subject = models.CharField(max_length=200, null=True, help_text="Subject")
    message = models.TextField(max_length=1000, null=True, help_text="Description")

    def __str__(self):
        return self.name

    

class Drop_Down(models.Model):

    dropdown_status = (
        ('Drop Down 1',_('Drop Down 1')),
        ('Deep Drop Down',(
            ('Deep Drop Down 1',_('Deep Drop Down 1')),
            ('Deep Drop Down 2',_('Deep Drop Down 2')),
            ('Deep Drop Down 3',_('Deep Drop Down 3')),
            ('Deep Drop Down 4',_('Deep Drop Down 4')),
            ('Deep Drop Down 5',_('Deep Drop Down 5')),
            )
        ),
        ('Drop Down 2',_('Drop Down 2')),
        ('Drop Down 3',_('Drop Down 3')),
        ('Drop Down 4',_('Drop Down 4')),
    )

    DropDown = models.CharField(max_length=60, choices=dropdown_status)
    
    def is_upperclass(self):
        '''Method to retrieve the human-readable name for the field’s current value'''
        return self.dropdown_status



    