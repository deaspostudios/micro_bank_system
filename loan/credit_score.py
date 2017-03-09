# coding=utf-8
from django.shortcuts import get_object_or_404

from bank.models import Personal_Information
from loan.models import Loan


########################################################################################################################

# credit scoring system function will be written here
# Analyzes loan worthiness and limits amount available to be borrowed

########################################################################################################################
class Person(object):
    pass


class Account(object):
    def __init__(self, acc_no):
        self.account_no = acc_no
        # an account number has to belong to a person
        self.holder = get_object_or_404(Personal_Information, pk=acc_no)
        # an account has the following
        self.current = None
        self.saving = None
        self.loan = None
        self.atm = None
        self.registrationdate = None
        self.creditscore = None

        # am not sure if the below functions are required

    def personal_detail(self, *args, **kwargs):
        self.registrationdate = self.holder.date_registered
        return self.registrationdate

    def personloan(self):
        self.loan = self.holder.loan_ac
        return self.loan

    def personsaving(self):
        self.saving = self.holder.saving_ac
        return self.saving

    def personcurrent(self):
        self.current = self.holder.current_ac
        return self.current


# Objects inheriting from Class Account

class Current(Account):
    def __init__(self, acc_no, amount, reg_date):
        # applies the same mro as the parent
        super(Current, self).__init__(acc_no)
        # other items that make up the current account
        self.amount = amount
        self.reg_date = reg_date
        # a current accounts may be registered with an ATM
        self.atm = None

        # ToAdd functions for evaluating credit score

        def balance(*args, **kwargs):
            if self.amount < 0:
                score = -1
            elif self.amount < self.saving:
                score = -0.5
            elif self.amount == self.saving:
                score = 0
            elif self.amount > self.saving:
                score = 0.5
            return score

        def loanCompbalance(*args, **kwargs):
            if self.amount < self.loan.loan_amount:
                score = -1
            elif self.amount == self.loan.loan_amount:
                score = 0
            elif self.amount > self.loan.loan_amount:
                score = 1

                # To find out, how does having an ATM affect one credibily
                # Tasked Shem to define how active the account has been, suggest this be defined at account level


class Saving(Account):
    def __init__(self, acc_no, amount, reg_date):
        # applies the same mro as the parent
        super(Saving, self).__init__(acc_no)
        # other items that make up the current account
        self.amount = amount
        self.reg_date = reg_date

    # The savings has to exist for a person tobe given  a loan
    def savingexist(self):
        if self.saving:
            return 0
            # Other rules like the minimu amount deposited etc.

            # Tasked Shem to define how active the account has been, suggest this be defined at account level

            # ToAdd functions for evaluating credit score


class Atm(Current):
    def __init__(self, number, expiry, attached):
        self.atm = attached
        self.number = number
        self.expity = expiry

        # ToAdd functions for evaluating credit score


class Loan(Account):
    # this class will super alot from other class functions+
    def __init__(self, acc_no, type, amount):
        super(Loan, self).__init__(acc_no)
        self.type = type
        self.amount = amount
        self.loanee = None
        self.status = None
        # def status(self, *args, **kwargs):

# Sample function of how the code is supposedly going to function
# polycarp = Account(11840)
# check if Polycarp has registered a current account
# Logic is that Having an account does not imply having current account
# We register a current account and if the same a/c number matches the a/c no for polycarp it's assigned to him
# p_current.current = Current(11840, 5000, 09/03/2017)   #Also from this object it's where we shall get checks related
# A person can have more than one current/savings/loans account
