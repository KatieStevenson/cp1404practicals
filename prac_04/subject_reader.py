"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        list_parts = line.split(",")
        list_parts[2] = int(list_parts[2])
        print(list_parts, end = ",") # Don't know why 'None' is at the end of the print output.

    input_file.close()


main()

