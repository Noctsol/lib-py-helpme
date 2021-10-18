"""
Owner: Kevin B
Contributors: N/A
Date Created: 20210824

Summary:
    Class containing convenience methods.

"""



# Default Python Packages
from uuid import uuid4              # Universally unique identifier
from datetime import datetime       # Datetime lib

import os                           # Provides ways of using OS dependent functionality

import csv                          # For reading/writing csv files


####################################### PATH FUNC #######################################

# Generates a directory only when it doesn't exist
def mkdir(folder_path, exist_ok=True):
    """Creates a directory ONLY when it doesn't exist

    Args:
        folder_path (string): Indicates where new folder will be created (Ex. C:/Users/you/Documents/Repository)
        exist_ok (bool, optional): Decides how to handle pre-existing directory. Defaults to True.

    Returns:
        bool: for confirmation
    """
    # Must be a valid path string
    assert os.path.isdir(folder_path) is True

    # Genewrate dir
    os.makedirs(folder_path, exist_ok=exist_ok)

    return True

# Deletes a directory
def deletedir(dir_path, not_exist_ok=True):
    """Deletes a directory

    Args:
        dir_path (string): Specifies what directory to delete
        not_exist_ok (bool, optional): Decides how to handle non-existent directory. Defaults to True.

    Returns:
        bool: Just here so that something is returned.
    """

    # Must be a valid path string
    assert os.path.isdir(dir_path) is True

    os.rmdir(dir_path, not_exist_ok=not_exist_ok)

    return True

# Deletes a file
def delete(file_path, not_exist_ok=True):
    """Delete a given file path

    Args:
        file_path (string): Absolute path of the file
        not_exist_ok (bool, optional): Decides how to handle non-existent file. Defaults to True.

    Returns:
        bool: Just here so that something is returned .
    """
    # Must be a valid path string
    assert os.path.isfile(file_path) is True

    # Do nothing if file doesn't exist
    if not os.path.exists(file_path) and not_exist_ok is True:
        return False

    os.remove(file_path)

    return True

# Gets the datetime a file was created - only works on Windows OS
def file_creation_date(file_path):
    """Gets the datetime a file was created - only works on Windows OS

    Args:
        file_path (string): Absolute path of the file

    Returns:
        datetime: create datetime of file
    """
    # Must be a valid path string
    assert os.path.isfile(file_path) is True
    return os.path.getctime(file_path)


####################################### CONVERSION FUNC #######################################

# Converts a list-of-lists to a list-of-dicts
def listdict(list_list):
    """Converts a list-of-lists to a list-of-dicts.

    Ex: [["a","b"],[1, 2],[3, 4]] ---> [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]

    Args:
        list_list (<list<list>>): A 2d list with a header row. Ex. [['a','b'], [1, 2], [3, 4]]

    Returns:
        <list<dict>>: list-of-dicts. Ex: [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    """
    # Fastest way to this is cycle through every row but the first
    # and use zip with the first row and subsequent rows
    return [dict(zip(list_list[0], i)) for i in list_list[1:]]

# Converts a list-of-dicts to lists-of-lists
def listlist(list_dict):
    """Converts a list-of-dicts to a list-of-lists.

    Ex: [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}] ---> [["a","b"],[1, 2],[3, 4]]

    Args:
        list_dict (<list<dict>>): A list of dictionaries. Ex: [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]

    Returns:
        <list<list>>: list-of-lists. Ex: [['a','b'], [1, 2], [3, 4]]
    """

    # Get headers
    headers = [key for key in list_dict[0]]
    table = [headers]   # append headers

    # Get data
    for dct in list_dict:
        # Store values in temporary list
        temp_lst = []

        # Fetch values inside dictionary
        for ikey in dct:
            temp_lst.append(dct[ikey])

        # Add tempt list to table container
        table.append(temp_lst)

    return table


####################################### STAMP FUNC #######################################

# Generate a string datetime stamp
def timestamp(formatting="%Y%m%d_%H%M%S"):
    """Returns a string indicate a current datetime(Ex. 20150106_012259).
    Generally used to put a timestamp on file names.

    Args:
        formatting (str, optional): Sets the format of datetime stamp that is returned.
        Defaults to "%Y%m%d_%H%M%S".

    Returns:
        string: Returns a string indicate a current datetime(Ex. 20150106_012259)
    """
    now = datetime.now()
    return now.strftime(formatting)

# Generate a globally unique identifier
def guid():
    """Generates a uuid4 (Example: 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0') using the Python
    uuid module.

    Returns:
        string: a unique universal ID of type 4. (Example: 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0')
    """
    return str(uuid4())


####################################### READ/WRITE filetype FUNC #######################################

# Read a csv file
def read_csv(file_path, delimiter=",", quotechar='"'):
    """Read a csv file and returns a nested list with the header/data

    Args:
        file_path (string): Absolute path of the file. Example:"C:/Users/Noctsol/Documents/somefile.csv"
        delimiter (str, optional): Delimiter of the the csv file. Default is a comma.. Defaults to ",".
        quotechar (str, optional): Character use to enclose values. Default is quotations.. Defaults to '"'.

    Returns:
        <list<list>>: List containing lists representing all rows
    """
    # Opening file
    with open(file_path, newline='') as csvfile:
        # Will be used to store content
        lsts = []

        # Loading and reading csv
        csv_data = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)

        # Adding data to container
        for row in csv_data:
            lsts.append(row)

        return lsts

# Outputs a 2d list to a csv file
def write_to_csv(file_path, data, delimiter=","):
    """Writes a nested list to a csv file

    Args:
        file_path (string): Absolute path of the file. Example:"C:/Users/Noctsol/Documents/somefile.csv"
        data (<list<list>>): Nested list of data. Example: [["header1", "header2"], ["val1", "val2"]]
        delimiter (str, optional): Delimiter of the the csv file. Defaults to ",".

    Returns:
        [type]: [description]
    """
    with open(file_path, 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)

        # write multiple rows
        writer.writerows(data)

        return True
