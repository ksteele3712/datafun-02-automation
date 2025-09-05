"""
File: kristinesteele_project_setup.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Kristine Steele
"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys
import time
import os

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_kristinesteele

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

import os

# Define folder names
YEARS_FOLDER = 'years'
OUTPUT_FOLDER = 'output'
PERIODIC_FOLDER = 'periodic_folder'
DATA_FOLDER = 'data'
REGIONS_FOLDER = 'regions'

# Define contents for each folder
YEARS = [str(year) for year in range(2020, 2024)]
OUTPUTS = ['output-csv', 'output-excel', 'output-json']
PERIODIC = [f'periodic_folder_{i+1}' for i in range(5)]
DATA = ['data-csv', 'data-excel', 'data-json']
REGIONS = [
    "North America",
    "South America",
    "Europe",
    "Asia",
    "Africa",
    "Oceania",
    "Middle East"
]

def create_main_and_subfolders():
    # Create main folders
    for folder in [YEARS_FOLDER, OUTPUT_FOLDER, PERIODIC_FOLDER, DATA_FOLDER, REGIONS_FOLDER]:
        os.makedirs(folder, exist_ok=True)

    # Create year subfolders
    for year in YEARS:
        os.makedirs(os.path.join(YEARS_FOLDER, year), exist_ok=True)

    # Create output subfolders
    for out in OUTPUTS:
        os.makedirs(os.path.join(OUTPUT_FOLDER, out), exist_ok=True)

    # Create periodic subfolders
    for pf in PERIODIC:
        os.makedirs(os.path.join(PERIODIC_FOLDER, pf), exist_ok=True)

    # Create data subfolders
    for d in DATA:
        os.makedirs(os.path.join(DATA_FOLDER, d), exist_ok=True)

    # Create region files (as empty .txt files with standardized names)
    for region in REGIONS:
        file_name = region.lower().replace(' ', '_') + '.txt'
        file_path = os.path.join(REGIONS_FOLDER, file_name)
        with open(file_path, 'w') as f:
            f.write(f"Region: {region}\n")

    print("All folders and files created as specified.")

def main():
    create_main_and_subfolders()

if __name__ == '__main__':
    main()
REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")

    for year in range(start_year, end_year + 1):
        year_path = ROOT_DIR / str(year)
        year_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {year_path}")


  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")

    for name in folder_list:
        folder_path = ROOT_DIR / name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")


  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")

    prefixed_names = [prefix + name for name in folder_list]
    for folder in prefixed_names:
        folder_path = ROOT_DIR / folder
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")

  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")
    
    num_folders = 5  # You can change this number as needed
    for i in range(num_folders):
        folder_name = f"periodic_folder_{i+1}"
        folder_path = ROOT_DIR / folder_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")
        if i < num_folders - 1:
            logger.info(f"Waiting {duration_seconds} seconds before creating next folder...")
            time.sleep(duration_seconds)


#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################


def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    for folder_name in folder_list:
        name = folder_name
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(' ', '_')
        folder_path = ROOT_DIR / name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''


    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")
    logger.info(f"Byline: {utils_kristinesteele.get_byline()}")

    create_main_and_subfolders()



logger.info("\n#####################################")
logger.info("# Completed execution of main()")
logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()