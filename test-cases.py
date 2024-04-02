from artwork import Artwork
from exhibition import PermanentGallery, ExhibitionHall, OutdoorSpace
from visitor import Visitor
from ticket import Ticket
from tour import Tour
from pricing import Pricing

def test_add_new_art():
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait")
    artwork2 = Artwork("The Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist masterpiece")

    artwork1.display()
    artwork2.display()
    # Add more artwork objects as needed

def test_open_new_exhibition():
    permanent_gallery = PermanentGallery("Gallery 1", "Permanent")
    exhibition_hall = ExhibitionHall("Hall A", "2 months")
    outdoor_space = OutdoorSpace("Garden", "3 weeks")

    permanent_gallery.display()
    exhibition_hall.display()
    outdoor_space.display()
    # Add more exhibition objects as needed

def test_purchase_tickets():
    visitor1 = Visitor("Alice", 25, "12345")
    visitor2 = Visitor("Bob", 55, "67890")
    tour_guide = "John"
    tour_date = "2024-04-15"
    tour_group_size = 20
    tour = Tour(tour_date, tour_group_size, tour_guide)
    tour_ticket = Ticket("Tour", "Louvre Museum", "2 hours", "2024-04-15", tour=tour)

    special_event_ticket = Ticket("Special Event", "Concert Hall", "3 hours", "2024-05-01", purpose="Musical Concert")

    pricing = Pricing()
    tour_ticket_price = pricing.calculate_price(visitor1)
    special_event_ticket_price = pricing.calculate_price(visitor2, is_special_event=True)

    visitor1.purchase_ticket(tour_ticket)
    visitor2.purchase_ticket(special_event_ticket)


    print(f"{visitor1.name} purchased a tour ticket for {tour_ticket_price} AED")
    print(f"{visitor2.name} purchased a special event ticket for {special_event_ticket_price} AED")

def test_display_payment_receipts():
    visitor1 = Visitor("Alice", 25, "12345")
    visitor2 = Visitor("Bob", 55, "67890")
    tour_guide = "John"
    tour_date = "2024-04-15"
    tour_group_size = 20
    tour = Tour(tour_date, tour_group_size, tour_guide)
    tour_ticket = Ticket("Tour", "Louvre Museum", "2 hours", "2024-04-15", tour=tour)


    special_event_ticket = Ticket("Special Event", "Concert Hall", "3 hours", "2024-05-01", purpose="Musical Concert")

    pricing = Pricing()
    tour_ticket_price = pricing.calculate_price(visitor1)
    special_event_ticket_price = pricing.calculate_price(visitor2, is_special_event=True)

    visitor1.purchase_ticket(tour_ticket)
    visitor2.purchase_ticket(special_event_ticket)

    total_price = tour_ticket_price + special_event_ticket_price
    print(f"Total price for both tickets: {total_price} AED")

# Run test cases
test_add_new_art()
test_open_new_exhibition()
test_purchase_tickets()
test_display_payment_receipts()
