"""A vaccination calculator."""

__author__ = "730309878"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population = int(input("Population: "))
doses_administered = int(input("Doses administered: "))
doses_per_day = int(input("Doses per day: "))
target_percent_vaccinated = int(input("Target percent vacinated: "))

people_vaccinated: float = (doses_administered / 2)
people_per_day: float = (doses_per_day / 2)
percent_complete: float = (people_vaccinated / population)
percent_remaining: int = ((target_percent_vaccinated) - (percent_complete * 100))
people_remaining: float = ((percent_remaining / 100) * population)
doses_needed: int = (people_remaining * 2 )
days_to_target: float = (doses_needed / doses_per_day)
days_to_target = round(days_to_target)
target_percent_vaccinated: str 
days_to_target: str
print("We will reach",(target_percent_vaccinated),"% vaccination in", (days_to_target),"days, which falls on ()")

today: datetime = datetime.today()
today.strftime("%B %d, %Y")
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
tomorrow.strftime("%B %d, %Y")
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight 

