from django import template
from jalali_date import date2jalali

register = template.Library()

# https://github.com/DaniDiazTech/Django-photo-app/tree/main/config
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

def show_jalali_date(value):
    return date2jalali(value)


register.filter('cut', cut)
register.filter('show_jalali_date', show_jalali_date)