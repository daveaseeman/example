# /usr/bin/env python
import os
from twilio.rest import Client

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)
building_phone = os.environ['PHONE']


def Person(self):
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone


def notify(tenant, visitor):
    notify = "{} {} is here to see you".format(visitor.fname, visitor.lname)
    client.api.account.messages.create(to=tenant.phone,
                                       from_=building_phone,
                                       body=notify)
    confirmation = "{} {} has been notified".format(tenant.fname, tenant.lname)
    return confirmation
