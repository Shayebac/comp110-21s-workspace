"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730309878"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    call_one: int = int(days_to_target(population, doses, doses_per_day, target))
    call_two: str = str(future_date(days_to_target))
    print("We will reach", (target), "% vaccination in", (days_to_target), "days, which falls on", (future_date.strftime("%B %d, %Y")), "." )


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int: 
    """Define days to target function."""
    people_vaccinated: float = (doses / 2)
    people_per_day: float = (doses_per_day / 2)
    percent_complete: float = (people_vaccinated / population)
    percent_remaining: float = ((target) - (percent_complete * 100))
    people_remaining: float = ((percent_remaining / 100) * population)
    doses_needed: float = (people_remaining * 2)
    days_to_target: float = (doses_needed / doses_per_day)
    days_to_target = round(days_to_target)
    return days_to_target
    

def future_date(days_to_target: int) -> str:
    """Return date."""
    today: datetime = datetime.today()
    today.strftime("%B %d, %Y")
    one_day: timedelta = timedelta(1)
    tomorrow: datetime = today + one_day
    tomorrow.strftime("%B %d, %Y")
    fortnight: timedelta = timedelta(7 + 7)
    future: datetime = today + fortnight
    future_date = datetime.now() + timedelta(days_to_target=str(days_to_target))
    return future_date


if __name__ == "__main__":
    main()
