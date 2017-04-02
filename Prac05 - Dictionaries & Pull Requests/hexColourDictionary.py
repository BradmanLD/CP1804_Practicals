"""
Use a constant dictionary of about 10 names and write a program that allows a user to enter a name and get
the code, e.g. entering AliceBlue should show #f0f8ff.
"""


HEX_COLOURS = {"AliceBlue": "#f0f8ff", "Black": "#000000", "LightBlue": "#add8e6", "Magenta": "#ff00ff",
               "Violet" : "#ee82ee", "White": "#ffffff", "Aquamarine1": "#7fffd4", "Azure1": "#f0ffff",
               "Beige": "#f5f5dc", "BurlyWood": "#deb887"}


hex_colour = input("Enter the name of a colour: ")
print(HEX_COLOURS[hex_colour])
