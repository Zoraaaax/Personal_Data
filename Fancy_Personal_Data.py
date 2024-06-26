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
# Get user input for address
address = input("Enter your address: ")
# Get user input for contact number
contact_number = input("Enter your contact number: ")

# Create an output string with formatted text
output = ["My name is " + name + ", and my dream job is " + dream_job + "."
          + "I live in " + address + ", and my contact number is" + contact_number]

# Iterate through each line in the output
for line in output:
    fancy_line = fancy_text(line)
    for c in fancy_line:
        print(c, end='', flush=True)
        sleep(0.001)
    print('')
