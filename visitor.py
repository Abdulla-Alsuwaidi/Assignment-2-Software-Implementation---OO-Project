from typing import List
from ticket import Ticket

class Visitor:
    def __init__(self, name: str, age: int, national_id: str):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.tickets_purchased: List[Ticket] = []

    def purchase_ticket(self, ticket: Ticket) -> None:
        self.tickets_purchased.append(ticket)

    def display(self) -> None:
        print("Visitor Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"National ID: {self.national_id}")
        print("Tickets Purchased:", self.tickets_purchased)
