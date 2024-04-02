from typing import Union
from visitor import Visitor

class Pricing:
    def calculate_price(self, visitor: Visitor, is_group: bool = False, is_special_event: bool = False) -> float:
        if visitor.age < 18 or visitor.age > 60:
            return 0.0  # Free ticket for children, seniors, and certain groups
            
        base_price = 63.0  # Base price for adults
        
        if is_group:
            base_price *= 0.5  # Apply 50% discount for groups
            
        if is_special_event:
            # Additional logic for special event pricing
            pass
        
        final_price = base_price * (1 + 0.05)  # Adding 5% VAT
        
        return final_price
