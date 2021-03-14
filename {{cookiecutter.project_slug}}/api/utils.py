import json
import logging
import random
import time
from hashlib import sha256

import boto3
import psycopg2
import requests
from botocore.exceptions import ClientError
from django.conf import settings
from django.core.exceptions import ValidationError


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def month_to_number(month_name):
    month = normalize(month_name.lower())
    value = 'null'
    if month == 'enero':
        value = 1
    elif month == 'febrero':
        value = 2
    elif month == 'marzo':
        value = 3
    elif month == 'abril':
        value = 4
    elif month == 'mayo':
        value = 5
    elif month == 'junio':
        value = 6
    elif month == 'julio':
        value = 7
    elif month == 'agosto':
        value = 8
    elif month == 'septiembre':
        value = 9
    elif month == 'octubre':
        value = 10
    elif month == 'noviembre':
        value = 11
    elif month == 'diciembre':
        value = 12

    return value


def day_to_number(day_name):
    day = normalize(day_name.lower())
    value = 'null'
    if day == 'lunes':
        value = 1
    elif day == 'martes':
        value = 2
    elif day == 'miercoles':
        value = 3
    elif day == 'jueves':
        value = 4
    elif day == 'viernes':
        value = 5
    elif day == 'sabado':
        value = 6
    elif day == 'domingo':
        value = 7

    return value


def get_random_api_key():
    timestr = int(time.time())
    randomValue = ''.join(random.choices('0123456789abcdefABCDEF', k=54))
    key = '{time}{random_key}'.format(time=timestr, random_key=randomValue)

    return sha256(key.encode()).hexdigest()



def upload_file_to_s3(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
