#!/usr/bin/env python3
import ldap3
from ldap3 import Server, Connection, ALL
import warnings
import os, sys
import datetime
from dateutil.relativedelta import relativedelta
import logging
import pytz
from datetime import timedelta, date
import json
# To test:
# currentDT.strftime("%Y%m%d%H%M%SZ"))

# Set logging
logging.basicConfig(format='LDAP Expiration Query: %(asctime)s %(message)s',filename='/Users/clay/debug/ldap.log',level=logging.DEBUG)
# variables:
utcNOW = pytz.utc.localize(datetime.datetime.utcnow())
expDATE = utcNOW + timedelta(days=10)
expDate.strftime("%Y%m%d%H%M%SZ")
ldap_base = "dc=sparkred,dc=com"
dispAttribs = ['cn', 'passwordExpirationTime', 'mail']
f=open("./creds", "r")
lines=f.readlines()
username=lines[0]
password=lines[1]
f.close
# ldap_query = '(passwordExpirationTime <= expDATE ) cn mail passwordExpirationTime'
# test_query1 = ('(&(objectclass=person)(uid=clay))', attributes=['sn', 'passwordExpirationTime', 'objectclass'])
# test_query2 = ('dc=sparkred,dc=com, '(&(objectclass=person)(uid=clay))', attributes=['sn', 'passwordExpirationTime', 'objectclass'])
server = Server('sr-prd-dal09-ldap-01-p.int.sparkred.com', get_info=ALL)
connectMe = Connection(server, username, password, auto_bind=True)
connectMe.search(ldap_base, '(&(objectclass=person)(uid=clay))', attributes = dispAttribs)
print(connectMe.entries)
print(expDATE)
