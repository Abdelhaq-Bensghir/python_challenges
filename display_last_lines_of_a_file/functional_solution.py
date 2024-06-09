def tail(file_path, x):
    """
    Objective: Display the last x lines of a text file.

    :param file_path: Path to the text file
    :param x: Number of lines to display from the end of the file
    :return: A string containing the last x lines
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Get the last x lines
            last_x_lines = lines[-x:]
            return ''.join(last_x_lines)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Get file path input
    file_path = input("Enter the path to the text file: ")

    # Get number of lines input
    num_lines = int(input("Enter the number of lines to display: "))

    # Call the tail function with inputs
    print(tail(file_path, num_lines))
