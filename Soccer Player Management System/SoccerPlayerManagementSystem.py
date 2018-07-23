# Soccer Player Management and Visualisation System
# Author: Paul Jr Fernandez


import matplotlib.pyplot as plotter

# Display player details
def print_player(p_id, p_name, p_age, p_height, p_weight):
    print ("Player ID:", p_id)
    print("Player name:", p_name)
    print("Age:", p_age)
    print("Height:", p_height)
    print("Weight:", p_weight)
    return

# Read all player records from the file into a dictionary
def build_player_db():
    search_file = open('Players.txt', 'r')
    # Initialize dictionary
    player_database = {}
    # Read all lines of the file into players_txt
    players_txt = search_file.readlines()
    search_file.close()
    first_record = True         # Flag to ignore first record - title row
    for record in players_txt:
        # Ignore first record - title row
        if first_record:
            first_record = False
        # Extract player information 
        else:
            record.rstrip('\n')
            player_record = record.split()
            record_length = len(player_record)
            player_age = player_record.pop(record_length - 3)
            player_height = player_record.pop(record_length - 3)
            player_weight = player_record.pop(record_length - 3)
            player_id = player_record.pop(0)
            player_name = " ".join(player_record)
            player_database [ player_id ] = [ player_name, player_age, player_height, player_weight ]
    return player_database


# Get Player ID: contains negative and NaN checks
def get_player_id():    
    p_id = 0
    # Repeats while player ID is negative or 0
    while p_id <= 0:
        try:
            p_id = 0 # Resetting ID
            p_id = int (input ("Please enter the player ID:"))
        # Following except handles NaN values
        except ValueError:
            print ("Player ID should be an integer. Try again!")
            pass
        if p_id < 0:
            print ("Player ID should be greater than 0. Try again!")
    # Adding buffer zeroes to the left of the player ID
    p_id = format (p_id, '0>9')
    # Check if Player ID is unique
    player_db = build_player_db()
    if p_id in player_db.keys():
        print ("Player ID exists!!!")
        print_player (p_id, player_db[p_id][0], player_db[p_id][1], player_db[p_id][2], player_db[p_id][3])
        print ("Please enter a unique Player ID.")
        # Rinse and repeat. Call the function again.
        p_id = get_player_id()
    return p_id

# Get Player Name: contains check for length of the name
def get_player_name():
    p_name = ""
    # Repeats while name is empty or greater than 32 characters
    while len(p_name) == 0 or len(p_name) >=33:
        p_name = "" # Resetting name
        p_name = input ("Please enter the player name(max 32 charcters):")
        if len(p_name) == 0:
            print ("Name cannot be an empty string")
        elif len(p_name) >= 33:
            print ("Apologies! Because of space constraints, name cannot be more than 32 characters")
    return p_name

# Get Player age: contains negative and NaN checks
def get_player_age():
    p_age=0
    # Repeats while player age is negative or 0
    while p_age <= 0:
        try:
            p_age = 0 # Resetting age
            p_age = int (input ("Please enter the age:"))
        # Following except handles NaN values
        except ValueError:
            print ("Age should be an integer. Try again!")
            pass
        if p_age < 0:
            print ("Age should not be negative. Try again!")
        # Add search check
    return p_age

# Get Player height: contains negative and NaN checks
def get_player_height():
    p_height = 0
    # Repeats while player height is negative or 0
    while p_height <= 0:
        try:
            p_height = 0 # Resetting height
            p_height = int (input ("Please enter the height(cm):"))
        # Following except handles NaN values
        except ValueError:
            print ("Height should be an integer. Try again!")
            pass
        if p_height < 0:
            print ("Height should not be negative. Try again!")
    return p_height

# Get Player weight: contains negative and NaN checks
def get_player_weight():
    p_weight = 0
    # Repeats while player weight is negative or 0
    while p_weight <= 0:
        try:
            p_weight = 0 # Resetting weight
            p_weight = float (input ("Please enter the weight(cm):"))
        # Following except handles NaN values
        except ValueError:
            print ("Weight should be an integer. Try again!")
            pass
        if p_weight < 0:
            print ("Weight should not be negative. Try again!")
    return p_weight

# Add player details to the file
def add_player():
    continue_to_add = 'Y'       # Variable to control adding multiple players into the file
    while continue_to_add == 'Y':
        print ("=== <A>dd a player ===")
        # Receiving player details from user
        player_id = get_player_id()
        player_name  = get_player_name()
        player_age  = get_player_age()
        player_height  = get_player_height()
        player_weight  = get_player_weight()
        # Displaying input details to user
        print ("\nThank You!\n")
        print ("The details of the player you entered are as follows:")
        print_player (player_id, player_name, player_age, player_height, player_weight)
        # Writing entered values to file
        append_file = open ('Players.txt', 'a')
        append_file.write ('\n' + format (player_id, '>12') + format (player_name, '>33') \
                           + format (player_age, '>13') + format (player_height, '>9') + format(player_weight, '>13'))
        append_file.close()
        print("The record has been successfully added to the Player.txt file.")
        continue_to_add = input("\nDo you want to enter details for another player (Y|Any other key for exit)?").upper()
    return 'N'          # This return will ensure that main menu loop continues

# Get Player ID: contains negative and NaN checks
def search_player_id():    
    p_id = 0
    # Repeats while player ID is negative or 0
    while p_id <= 0:
        try:
            p_id = 0 # Resetting ID
            p_id = int (input ("Please enter the player ID you want to search:"))
        # Following except handles NaN values
        except ValueError:
            print ("Player ID should be an integer. Try again!")
            pass
        if p_id < 0:
            print ("Player ID should be greater than 0. Try again!")
    print ("\nThank You!\n")
    # Adding buffer zeroes to the left of the player ID
    p_id = format (p_id, '0>9')
    # Search for Player ID
    player_db = build_player_db()
    if p_id in player_db.keys():
        print ("One player has been found:")
        print_player (p_id, player_db[p_id][0], player_db[p_id][1], player_db[p_id][2], player_db[p_id][3])
    else:
        print ("Player ID:" + p_id + " does not exist in database.")
    return     
            
def search_player():
    continue_to_search = 'Y'       # Variable to control searching multiple players from the db
    while continue_to_search == 'Y':
        print ("=== <S>earch for existing player ===")
        search_player_id()
        continue_to_search = input ("\nDo you want to search for another player (Y|Any other key for exit)?").upper()            
    return 'N'          # This return will ensure that main menu loop continues

def visualize_attribute(mode):
    player_db = build_player_db()       # Populate player db
    attribute_distribution = []         # Intialize list of values for histogram 
    if mode == 'Age':
        index = 1                       # Position of age values in dictionary of lists
        plotter.xlabel(mode)            # Histogram x-axis name
    elif mode == 'Height':
        index = 2                       # Position of height values in dictionary of lists
        plotter.xlabel(mode + '(cm)')   # Histogram x-axis name
    elif mode == 'Weight':
        index = 3                       # Position of weight values in dictionary of lists
        plotter.xlabel(mode + '(kg)')   # Histogram x-axis name
    for p_id in player_db:
        attribute_distribution.append(float(player_db[p_id][index]))    # Populate list for histogram
    no_of_players = len(attribute_distribution)                         # No of players for Histogram title
    attribute_distribution.sort()                                       # Sort list to get sequential values
    attr_min = int(min (attribute_distribution))                        # Minimum attribute value
    attr_max = int(max (attribute_distribution))                        # Maximum attribute value
    attr_step = 1                                                       # Steps by which subsequent bins will vary
    bins = [ bin_item for bin_item in range (attr_min, attr_max, attr_step) ]    # Populate list of bins
    plotter.hist(attribute_distribution, bins, rwidth=0.8)              # rwidth ensure a gap between subsequent bars
    plotter.ylabel('Frequency')                                         # Y-axis name
    plotter.title('Histogram for ' + mode + ' of ' + str(no_of_players) + ' soccer players')    # Histogram Title
    plotter.show()

def visualize_player():
    # Visualize Menu Option
    visualize_options = { '1': 'Age',
                          '2': 'Height',
                          '3': 'Weight'}
    continue_to_visualize = 'Y'             # Variable to control generating subsequent visualizations
    while continue_to_visualize == 'Y':
        print ("=== <V>isualize player details ===")
        print ("1. Age    2. Height    3. Weight")
        choice = input ("Please select the attribute you want to visualise:")
        try:
            visualize_attribute (visualize_options[choice]) # Call the visualize_attribute function and pass the mode as argument
        except KeyError:
            print ("Invalid option")
        continue_to_visualize = input ("Do you want to visualize for another attribute (Y|Any other key for exit)?").upper() 
    return 'N'          # This return will ensure that main menu loop continues

def quit_menu():
    print ("Thank you and have a nice day")
    return 'Y'


# Function that displays the menu
def print_menu():
    # Display menu
    print ("=======================================================")
    print ("Welcome to the Soccer Player Management and Visualisation System")
    print ("<A>dd details of a player.")
    print ("<S>earch player details for a player.")
    print ("<V>isualize player details.")
    print ("<Q>uit.")
    print ("=======================================================")

# Main Function definition
def main():
    quit_program = 'N'          # Variable to control exit from main menu loop
    while quit_program != 'Y':   
        # Print the menu
        print_menu()
        # Read user choice and convert it to uppercase
        choice = input ("Please select an option from the above:").upper()
        # Dictionary to hold menu options
        menu_options = { 'A': add_player,
                         'S': search_player,
                         'V': visualize_player,
                         'Q': quit_menu}
        try:
            quit_program = menu_options[choice]()
        except KeyError:
            print ("Invalid option")

# Call the main function
main()
