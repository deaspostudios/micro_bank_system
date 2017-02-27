from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from loan.models import Economic

# Create your models here.

class Addresse(models.Model):
    postal_address = models.TextField(max_length=1000)
    email = models.EmailField()
    phone_no = models.IntegerField()
    tel_no = models.IntegerField(blank=True)
    resident_town = models.CharField(max_length=20)
    estate = models.CharField(max_length=20)
    house_no = models.IntegerField(blank=True)

    def __str__(self):
        return "Address details for: %s" % self.phone_no

        ########################################################################################################################


class SavingAccount(models.Model):
    account_number = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    reg_date = models.DateTimeField(default=now)

    ########################################################################################################################


class CurrentAccount(models.Model):
    account_number = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    reg_date = models.DateTimeField(default=now)


########################################################################################################################
class ATMCard(models.Model):
    number = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    expiry_date = models.DateTimeField()
    csv = models.IntegerField()
    reg_date = models.DateTimeField(default=now)
    atm_saving = models.ForeignKey(SavingAccount, blank=True)
    atm_current = models.ForeignKey(CurrentAccount)


class Personal_Information(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    id_number = models.IntegerField(primary_key=True)
    passport = models.BooleanField(default=False)
    passport_no = models.IntegerField(blank=True)
    pin_no = models.IntegerField()
    ########################################################################################################################
    address = models.ForeignKey(Addresse)
    ########################################################################################################################
    current_ac = models.ForeignKey(CurrentAccount)
    ########################################################################################################################
    economic = models.ForeignKey(Economic)
    ########################################################################################################################
    saving_ac = models.ForeignKey(SavingAccount, blank=True)
    ########################################################################################################################
    register_atm = models.BooleanField(default=True)
    atm_card = models.ForeignKey(ATMCard)
    ########################################################################################################################
    loan_ac = models.ForeignKey(Loan, blank=True)
    ########################################################################################################################
    date_registered = models.DateTimeField(default=now)

    ########################################################################################################################

    def __str__(self):
        return "%s:%s" % (str(self.id_number), self.surname)
