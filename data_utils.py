import datetime
import pytz 

utc = pytz.utc
# 2.2: 13th october 2021 at 6am UTC+8, 10pm at UTC -> (2021, 10, 12 , 22)
# 2.4: 5th Jan 2022 at 6am UTC+8, 10pm at UTC -> (2022, 1, 4, 22)
MAINTENANCE_DT = datetime.datetime(2022,1,4,22, tzinfo=utc)

def date_time_formatter(local_maintenance_datetime):
    format_datemonth = '%d %b'
    format_time = '%H : %M'

    formatted_datemonth = local_maintenance_datetime.strftime(format_datemonth)
    formatted_time = local_maintenance_datetime.strftime(format_time)
    return formatted_datemonth, formatted_time

def get_country_names():
    COUNTRY_LIST = pytz.common_timezones
    return COUNTRY_LIST

def get_utc_timezones():
    UTC_TIMEZONE_LIST = []
    for x in range(-12,0):
        UTC_TIMEZONE_LIST.append(x)
    for x in range(0,15):
        UTC_TIMEZONE_LIST.append("+"+ str(x))

    return  UTC_TIMEZONE_LIST

def get_time_information_by_country_name(country):
    country_timezone = pytz.timezone(country)
    local_maintenance_datetime = MAINTENANCE_DT.astimezone(country_timezone)
    return local_maintenance_datetime

def get_time_information_by_UTC_offset(offset):
    local_maintenance_datetime = MAINTENANCE_DT + datetime.timedelta(hours=int(offset))
    return local_maintenance_datetime