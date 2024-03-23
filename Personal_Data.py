# Import the pyfiglet
import pyfiglet
# Import the sleep function from the time module
from time import sleep


# Define a function to create fancy text using pyfiglet
def fancy_text(text):
    return '\033[94;1m' + pyfiglet.figlet_format(text, font='isometric1') + '\033[=0m'


# Get user input for name
name = input("Enter your name: ")

# Get user input for dream job
dream_job = input("Enter your dream job: ")

# Get user input for civil status
civil_status = input("Enter your civil status: ")

# Get user input for address
address = input("Enter your address")

# Get user input for contact number
contact_number = input("Enter your contact number: ")

# Iterate through each line in the output
