# Importing necessary modules for testing
from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue

class TestBand:
    """Band in many_to_many.py"""
    
    def test_has_name(self):
        """Band is instantiated with a name"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="spicegurls", hometown="London")

        assert band_1.name == "boygenius"
        assert band_2.name == "spicegurls"

    def test_name_is_mutable_string(self):
        """names are mutable strings"""
        band_1 = Band(name="boygenius", hometown="NYC")
        assert isinstance(band_1.name, str)

        band_1.name = "spicegurls"
        assert isinstance(band_1.name, str)
        assert band_1.name == "spicegurls"

        band_1.name = 7
        assert band_1.name == "spicegurls"

    def test_name_has_length(self):
        """names are longer than 0 characters"""
        band_1 = Band(name="boygenius", hometown="NYC")
        assert len(band_1.name) > 0

        band_1.name = ""
        assert band_1.name == "boygenius"

    def test_has_hometown(self):
        """Band is instantiated with a hometown"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="spicegurls", hometown="London")

        assert band_1.hometown == "NYC"
        assert band_2.hometown == "London"

    def test_hometown_is_immutable_string(self):
        """hometowns are immutable strings"""
        band_1 = Band(name="boygenius", hometown="NYC")
        assert isinstance(band_1.hometown, str)

        band_1.hometown = "Boston"
        assert isinstance(band_1.hometown, str)
        assert band_1.hometown == "NYC"

        band_1.hometown = 7
        assert band_1.hometown == "NYC"

    def test_hometown_has_length(self):
        """hometowns are longer than 0 characters"""
        band_1 = Band(name="boygenius", hometown="NYC")
        assert len(band_1.hometown) > 0

        band_1.hometown = ""
        assert band_1.hometown == "NYC"

    def test_concerts(self):
        """band has many concerts"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert_1 = band.play_in_venue(venue=venue, date="Nov 22")
        concert_2 = band.play_in_venue(venue=venue, date="Nov 27")

        assert len(band.concerts()) == 2
        assert concert_1 in band.concerts()
        assert concert_2 in band.concerts()

    def test_concerts_of_type_concert(self):
        """concerts must be of type Concert"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        band.play_in_venue(venue=venue, date="Nov 22")
        band.play_in_venue(venue=venue, date="Nov 27")

        assert all(isinstance(concert, Concert) for concert in band.concerts())

    def test_venues(self):
        """band has many venues"""
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="Ace of Spades", city="SAC")
        band.play_in_venue(venue=venue_1, date="Nov 22")
        band.play_in_venue(venue=venue_2, date="Nov 27")

        assert len(band.venues()) == 2
        assert venue_1 in band.venues()
        assert venue_2 in band.venues()

    def test_venues_of_type_venue(self):
        """venues must be of type Venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="Ace of Spades", city="SAC")
        band.play_in_venue(venue=venue_1, date="Nov 22")
        band.play_in_venue(venue=venue_2, date="Nov 27")

        assert all(isinstance(venue, Venue) for venue in band.venues())

    def test_venues_are_unique(self):
        """venues are unique"""
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="Ace of Spades", city="SAC")
        band.play_in_venue(venue=venue_1, date="Nov 22")
        band.play_in_venue(venue=venue_2, date="Nov 27")
        band.play_in_venue(venue=venue_2, date="Nov 29")

        assert len(set(band.venues())) == len(band.venues())
        assert len(band.venues()) == 2
        assert venue_1 in band.venues()
        assert venue_2 in band.venues()

    def test_play_in_venue(self):
        """creates and returns a new concert for that band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="SAC")
        concert_1 = band.play_in_venue(venue=venue, date="Nov 22")

        assert len(band.concerts()) == 1
        assert band.concerts()[0].band == band
        assert band.concerts()[0].venue == venue
        assert isinstance(concert_1, Concert)

        concert_2 = band.play_in_venue(venue=venue2, date="Nov 27")
        assert len(band.concerts()) == 2
        assert band.concerts()[1].band == band
        assert band.concerts()[1].venue == venue2
        assert isinstance(concert_2, Concert)

    def test_all_introductions(self):
        """returns all introductions for the band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="SAC")
         band.play_in_venue(venue=venue2, date="Nov 22")

        assert (
            band.all_introductions()[0]
            == "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
        assert (
            band.all_introductions()[1]
            == "Hello SAC!!!!! We are boygenius and we're from NYC"
        )







