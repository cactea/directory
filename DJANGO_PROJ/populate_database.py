import os
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DIRECTORY.settings')

import django
django.setup()


from CACTEA.models import cactea


'''
Populate database:
Note that the database am populating here is the heroku database.
You would have to change the credentials in setting.py to
populate an online database of your own.
'''
def populate_database():
    CSV_FILE = 'D:\\FREELANCER\\DjangoProjectGamma\\DIRECTORY\\CACTEA\\data\\new_storage.csv'
    CSV_FILE = 'CACTEA/templates/new_storage.csv'
    cnt = 0
    with open(CSV_FILE) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = cactea(id_IT = row['id'], SERIAL_NUMBER = row['SERIAL_NUMBER'], MANUFACTURER = row['MANUFACTURER'],
            NAME = row['NAME'], MODEL = row['MODEL'], LOCATION = row['LOCATION'], ROOM = row['ROOM'],
            ENERGY_CONSUMPTION = row['ENERGY_CONSUMPTION'], BTU = row['BTU'], MICROCODE = row['MICROCODE'],
            PATCH_LEVEL = row['PATCH_LEVEL'], CUSTOMER_ID = row['CUSTOMER_ID'], HOSTS_APPLICATION = row['HOSTS_APPLICATION'],
            TCPADDR1 = row['TCPADDR1'], TCPADDR2 = row['TCPADDR2'], TCPADDR3 = row['TCPADDR3'],
            SW_GUI = row['SW_GUI'], INVESTMENT_DATE = row['INVESTMENT_DATE'],
            MAINTENANCE_EXPIRATION_DATE = row['MAINTENANCE_EXPIRATION_DATE'], MAINTENANCE_PROVIDER = row['MAINTENANCE_PROVIDER'],
            MAINTENANCE_CONTRACT = row['MAINTENANCE_CONTRACT'], IS_EXTENSION_REQUIRED = row['IS_EXTENSION_REQUIRED'],
            IS_MIGRATION_REQUIRED = row['IS_MIGRATION_REQUIRED'], RAID_CONFIG = row['RAID_CONFIG'],
            USABLE_CAPACITY_GB = row['USABLE_CAPACITY_GB'], CAPACITY_IN_USE_GB = row['CAPACITY_IN_USE_GB'],
            FREE_CAPACITY_GB = row['FREE_CAPACITY_GB'], EXTENSION = row['EXTENSION'], COMMENT_1 = row['COMMENT_1'],
            STORAGE_TYPE = row['STORAGE_TYPE'], READADMIN = row['READADMIN'], RACK = row['RACK'],
            COST_CENTER = row['COST_CENTER'], CO2_KG = row['CO2_KG'], SECOND_INVESTMENT_DATE = row['SECOND_INVESTMENT_DATE'])
            p.save()
            cnt += 1
    print('Created {} records'.format(cnt))


populate_database()
