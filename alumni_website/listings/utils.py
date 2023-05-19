import datetime

from .models import DiplomaNumber


def get_current_year():
    """return the current year"""
    return datetime.date.today().year


def generate_diploma_number(year) -> int:
    """return a diploma number"""
    diplomes_of_year = DiplomaNumber.objects.filter(year=year)
    nb_dip = len(diplomes_of_year)
    diploma_number = f"{str(year)[-2:]}{str(nb_dip).zfill(5)}"
    return diploma_number
