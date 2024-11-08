from podcast_data import themes  # Importing a list of podcast themes from an external file
from podcast_data import data    # Importing podcast data from an external file

def start_recomendation():
    """Display the welcome message."""
    print(("#" * 46))  # Print a line of 46 hash symbols
    print("WELCOME TO THE PODCAST RECOMMENDATION PLATFORM!")  # Display the welcome message
    print("#" * 46)  # Print another line of hash symbols

def select_option():
    """Prompt the user to select how they want to search for podcasts."""
    # List of options to display to the user
    option_list = [
        "Select 'n' if you want to choose your podcast by NAME.",
        "Select 't' if you want to choose your podcast by THEME.",
        "Select 'v' if you want to choose your podcast by RATING."
    ]
    
    # Join the list into a single string for display
    options = "\n".join(option_list)
    option = input(options + "\n")  # Prompt the user to select an option
    
    # Check the user's input and call the corresponding function
    if option == "n":
        select_name()  # Search by name
    elif option == "t":
        select_tematica()  # Search by theme
    elif option == "v":
        select_rating()  # Search by rating
    else:
        print("Invalid letter! Please enter 'n', 't' or 'v'.")  # Handle invalid input
        select_option()  # Restart the selection if input is invalid

def select_name():
    """Prompt the user to search for a podcast by name."""
    # Ask the user to input the initial letters of the podcast name
    name_prefix = input("Enter the first letters or word of the podcast name you are looking for:\n").lower()
    found = False  # Flag to track if a match is found

    # Loop through the podcast data to find matches
    for item in data:
        # Check if the podcast name starts with the given prefix
        if item[0].lower().startswith(name_prefix):
            print(f"Podcast found: {item[0].upper()}")
            print(f"- Category: {item[3]}")
            print(f"- Seasons: {item[1]}")
            print(f"- Rating: {item[2]}/5")
            print(f"- Description: {item[4]}\n")
            found = True  # Set the flag to True if a match is found

    # If no matches were found, prompt the user to try again
    if not found:
        print("Podcast not found. Try again.")
        select_name()

def select_tematica():
    """Prompt the user to search for podcasts by theme."""
    # List of available themes to display to the user
    tematica_list = [
        f"Select 'a' for {themes[0]}.",
        f"Select 'c' for {themes[1]}.",
        f"Select 'd' for {themes[2]}.",
        f"Select 'e' for {themes[3]}.",
        f"Select 'f' for {themes[4]}.",
        f"Select 'hi' for {themes[5]}.",
        f"Select 'hu' for {themes[6]}.",
        f"Select 'na' for {themes[7]}.",
        f"Select 'no' for {themes[8]}.",
        f"Select 'p' for {themes[9]}.",
        f"Select 's' for {themes[10]}.",
        f"Select 'te' for {themes[11]}.",
        f"Select 'tv' for {themes[12]}."
    ]
    
    # Display the list of themes and prompt the user to choose one
    tematicas = "\n".join(tematica_list)
    tematica = input(tematicas + "\n")
    
    # Map user input to the corresponding category
    category_map = {
        "a": "Astronomy",
        "c": "Culture",
        "d": "Documentary",
        "e": "Education",
        "f": "Philosophy",
        "hi": "History",
        "hu": "Humor",
        "na": "Nature",
        "no": "News",
        "p": "Politics",
        "s": "Self-Improvement",
        "te": "Technology",
        "tv": "TV & Film"
    }
    
    # Check if the user's input is in the category map
    if tematica in category_map:
        selected_category = category_map[tematica]
        # Loop through the podcast data to find matches in the selected category
        for item in data:
            if item[3] == selected_category:
                print(f"In the category {selected_category} you have: {item[0].upper()}")
                print(f"- Seasons: {item[1]}")
                print(f"- Rating: {item[2]}/5")
                print(f"- Description: {item[4]}")
    else:
        print("Invalid letter! Please enter one of the above.")  # Handle invalid input
        select_tematica()

def select_rating():
    """Prompt the user to search for podcasts by rating."""
    # Ask the user to input a rating from 1 to 5
    rating = input("Select a rating from 1 to 5:\n")
    
    # Check if the input is a valid rating
    if rating in ["1", "2", "3", "4", "5"]:
        found = False  # Flag to track if a match is found

        # Loop through the podcast data to find matches
        for item in data:
            if item[2] == rating:
                print(f"With rating {rating} you have: {item[0].upper()}")
                print(f"- Seasons: {item[1]}")
                print(f"- Rating: {item[2]}/5")
                print(f"- Description: {item[4]}\n")
                found = True  # Set the flag to True if a match is found

        # If no matches were found, inform the user
        if not found:
            print(f"No podcasts found with rating {rating}.")
    else:
        print("Invalid rating! Please enter a number from 1 to 5.")  # Handle invalid input
        select_rating()

# Start the program by displaying the welcome message
start_recomendation()

# Begin the podcast search based on user's choice
select_option()

# Note: This is a useless comment for the Git course
