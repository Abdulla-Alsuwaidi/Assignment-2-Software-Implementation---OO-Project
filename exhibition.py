# exhibition.py

class Exhibition:
    def __init__(self, location: str, duration: str):
        self.location = location
        self.duration = duration
    
    def display(self) -> None:
        print(f"Location: {self.location}, Duration: {self.duration}")

class PermanentGallery(Exhibition):
    def __init__(self, location: str, duration: str):
        super().__init__(location, duration)

class ExhibitionHall(Exhibition):
    def __init__(self, location: str, duration: str):
        super().__init__(location, duration)

class OutdoorSpace(Exhibition):
    def __init__(self, location: str, duration: str):
        super().__init__(location, duration)
