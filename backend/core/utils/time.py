from datetime import date, timedelta

def get_default_checkin():
    return date.today() + timedelta(days=1)

def get_default_checkout():
    from core.models import Hotel
    max_staying = Hotel.objects.all()[0].max_staying_duration
    return get_default_checkin() + max_staying

def get_human_default_checkin():
    return str(get_default_checkin())

def get_human_check_out():
    return str(get_default_checkout())
