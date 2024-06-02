#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue


if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Initialize objects for debugging
    band1 = Band(name="boygenius", hometown="NYC")
    band2 = Band(name="Triple Genius", hometown="LA")

    venue1 = Venue(name="Theatre", city="NYC")
    venue2 = Venue(name="Ace of Spades", city="Sacramento")

    # Create concerts for debugging
    concert1 = band1.play_in_venue(venue=venue1, date="Nov 3")
    concert2 = band2.play_in_venue(venue=venue2, date="Nov 5")

    # Access various attributes and methods for debugging
    concerts_band1 = band1.concerts()
    concerts_venue1 = venue1.concerts()
    bands_venue1 = venue1.bands()

    introduction1 = concert1.introduction()
    hometown_show1 = concert1.hometown_show()

    # Start interactive debugger session
    ipdb.set_trace()
