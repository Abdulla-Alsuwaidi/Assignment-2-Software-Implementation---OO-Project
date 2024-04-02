class Artwork:
    def __init__(self, title: str, artist: str, date_of_creation: str, historical_significance: str):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
    
    def display(self) -> None:
        print(f"Title: {self.title}, Artist: {self.artist}, Date of Creation: {self.date_of_creation}, Historical Significance: {self.historical_significance}")
