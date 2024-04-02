from tour import Tour
from typing import Union

class Ticket:
    def __init__(self, event_type: str, location: str, duration: str, event_date: str, tour: Union[None, Tour] = None, purpose: Union[None, str] = None):
        self.event_type = event_type
        self.location = location
        self.duration = duration
        self.event_date = event_date
        self.tour = tour
        self.purpose = purpose

    def display_details(self) -> None:
        print("Ticket Details:")
        print(f"Event Type: {self.event_type}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration}")
        print(f"Event Date: {self.event_date}")
        if self.event_type == 'Tour':
            print(f"Tour Date: {self.tour.date}")
            print(f"Group Size: {self.tour.group_size}")
            print(f"Guide: {self.tour.guide}")
        elif self.event_type == 'Special Event':
            print(f"Purpose: {self.purpose}")
