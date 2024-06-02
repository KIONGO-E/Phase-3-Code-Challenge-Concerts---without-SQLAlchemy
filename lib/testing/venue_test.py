# Importing necessary modules for testing
from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue

# Define a test class for testing the Venue class
class TestVenue:
    """Venue in many_to_many.py"""

    # Test case to check if Venue is instantiated with a name
    def test_has_name(self):
        """Venue is instantiated with a name"""
        venue = Venue(name="Ace of Spades", city="SAC")

        assert venue.name == "Ace of Spades"

    # Test case to check if name attribute is mutable string
    def test_name_is_mutable_string(self):
        """names are mutable strings"""
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue_1.name, str)

        venue_1.name = "MoonDust"
        assert isinstance(venue_1.name, str)
        assert venue_1.name == "MoonDust"

        # Attempt to assign integer to name (should maintain previous value)
        venue_1.name = 7
        assert venue_1.name == "MoonDust"

    # Test case to check if name attribute has length longer than 0
    def test_name_has_length(self):
        """names are longer than 0 characters"""
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert len(venue_1.name) > 0

        # Attempt to set name to empty string (should maintain previous value)
        venue_1.name = ""
        assert venue_1.name == "Ace of Spades"

    # Test case to check if Venue is instantiated with a city
    def test_has_city(self):
        """Venue is instantiated with a city"""
        venue = Venue(name="Ace of Spades", city="SAC")

        assert venue.city == "SAC"

    # Test case to check if city attribute is mutable string
    def test_city_is_mutable_string(self):
        """cities are mutable strings"""
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue_1.city, str)

        venue_1.city = "NYC"
        assert isinstance(venue_1.city, str)
        assert venue_1.city == "NYC"

        # Attempt to assign integer to city (should maintain previous value)
        venue_1.city = 7
        assert venue_1.city == "NYC"

    # Test case to check if city attribute has length longer than 0
    def test_city_has_length(self):
        """cities are longer than 0 characters"""
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert len(venue_1.city) > 0

        # Attempt to set city to empty string (should maintain previous value)
        venue_1.city = ""
        assert venue_1.city == "SAC"

    # Test case to check if Venue has many concerts
    def test_concerts(self):
        """venue has many concerts"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band, venue=venue)
        concert_2 = Concert(date="Nov 27", band=band, venue=venue)

        assert len(venue.concerts()) == 2
        assert concert_1 in venue.concerts()
        assert concert_2 in venue.concerts()

    # Test case to check if concerts in Venue are of type Concert
    def test_concerts_of_type_concert(self):
        """concerts must be of type Concert"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        Concert(date="Nov 22", band=band, venue=venue)
        Concert(date="Nov 27", band=band, venue=venue)

        assert all(isinstance(concert, Concert) for concert in venue.concerts())

    # Test case to check if Venue has many bands
    def test_bands(self):
        """venue has many bands"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue_1)
        Concert(date="Nov 27", band=band_2, venue=venue_1)

        assert len(venue_1.bands()) == 2
        assert band_1 in venue_1.bands()
        assert band_2 in venue_1.bands()

    # Test case to check if bands in Venue are of type Band
    def test_bands_of_type_band(self):
        """bands must be of type Band"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue_1)
        Concert(date="Nov 27", band=band_2, venue=venue_1)

        assert all(isinstance(band, Band) for band in venue_1.bands())

    # Test case to check if bands in Venue are unique
    def test_bands_are_unique(self):
        """bands are unique"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue_1)
        Concert(date="Nov 27", band=band_2, venue=venue_1)
        Concert(date="Nov 29", band=band_2, venue=venue_1)

        assert len(set(venue_1.bands())) == len(venue_1.bands())
        assert len(venue_1.bands()) == 2
        assert band_1 in venue_1.bands()
        assert band_2 in venue_1.bands()
