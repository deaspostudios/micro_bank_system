from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from bank.models import Addresse

# Create your models here.

########################################################################################################################
class Expenses(models.Model):
    rent = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    electricity = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    water = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    transport = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    phone = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    entertainment = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    school_fees_desc = models.CharField(max_length=500,
                                        help_text="Are you schooling yourself or someone? Tell us how this expense applies to you.")
    school_fees = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    others = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
########################################################################################################################
class Saving(models.Model):
    savings_plan = models.BooleanField(default=True, blank=True)
    saving_detail = models.TextField(max_length=1000)
    monthly_saving = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)


########################################################################################################################
class Economic(models.Model):
    status = (
        ('employed', 'employed'),
        ('self-employed', 'self-employed'),
        ('not working', 'not working'),
    )

    employment_status = models.CharField(choices=status, default="employed", max_length=50)
    employer_name = models.CharField(max_length=50, blank=True)
    employer_address = models.CharField(max_length=50, blank=True)
    monthly_income = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    economic_activities = (
        ('Farming', 'Farming'),
        ('SMEs', 'SMEs'),
        ('Others', 'Others'),
    )
    other_economic = models.CharField(max_length=50, choices=economic_activities, blank=True)
    econ_life = models.IntegerField()
    other_econ = models.CharField(max_length=50, blank=True)
    gen_income = models.DecimalField(decimal_places=2, max_digits=7, default=0, blank=True)
    ########################################################################################################################
    savings = models.ForeignKey(Saving, blank=True)
    ########################################################################################################################
    monthly_expenses = models.ForeignKey(Expenses)
########################################################################################################################
class Guarantor(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    id_number = models.IntegerField(primary_key=True)
    passport = models.BooleanField(default=False)
    passport_no = models.IntegerField(blank=True)
    pin_no = models.IntegerField()
    address = models.ForeignKey(Addresse)
########################################################################################################################
class Other_Borrower(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    id_number = models.IntegerField(primary_key=True)
    passport = models.BooleanField(default=False)
    passport_no = models.IntegerField(blank=True)
    pin_no = models.IntegerField()
    address = models.ForeignKey(Addresse)
########################################################################################################################
class Loan(models.Model):
    new_customer = models.BooleanField(default=True)
    loan_application_number = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    loan_type_choices = (
        ('Instant', 'Instant'),
        ('Mjengo', 'Mjengo'),
        ('Mkulima', 'Mkulima'),
        ('Salary Advance', 'Salary Advance'),
        ('School Fees', 'School Fees'),
        ('Funeral', 'Funeral'),
    )
    loan_tyoe = models.CharField(max_length=50, choices=loan_type_choices)
    loan_period = models.IntegerField()
    status = (
        ('Awarded', 'Awarded'),
        ('Denied', 'Denied'),
    )
    loan_status = models.CharField(max_length=20, choices=status)
    reg_date = models.DateTimeField(default=now)

    people = (
        ('Only me', 'Only me'),
        ('Group', 'Group'),
    )
    participanting = models.CharField(max_length=20, choices=people, default="Only me")
    participant_no = models.IntegerField(blank=True)
    participant_details = models.ForeignKey(Other_Borrower)

    loan_purpose = models.TextField(max_length=1000)
    guarantee = models.ForeignKey(Guarantor)

    criminal_offence = models.BooleanField(default=False)
    bankruptcy = models.BooleanField(default=False)
    defaults_payments = models.BooleanField(default=False)
    defaults_description = models.CharField(max_length=1000, blank=True)
    child_support = models.BooleanField(default=False)
    child_support_description = models.CharField(max_length=1000, blank=True)
########################################################################################################################

    # creddit scoring syatem function will be wriiten here
    # Analyzes loan worthiness and limits amount available to be borrowed

########################################################################################################################

#     Loan awarding system
#     Awards a loan and credits the loanee account and also calculates days remaining to repayment
