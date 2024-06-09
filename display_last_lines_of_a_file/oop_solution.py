class Tail:
    def __init__(self, file_path):
        """
        Initialize the Tail object with the file path.

        :param file_path: Path to the text file
        """
        # 'self' refers to the instance of the class being created
        # It allows access to the instance's attributes and methods within the class
        # 'file_path' is a parameter passed to the __init__ method, assigned to the instance variable 'self.file_path'
        self.file_path = file_path

    def display_last_lines(self, x):
        """
        Display the last x lines of the text file.

        :param x: Number of lines to display from the end of the file
        :return: A string containing the last x lines
        """
        try:
            # 'self.file_path' accesses the file path attribute of the instance
            # Open the file with UTF-8 encoding to handle a wide range of characters
            with open(self.file_path, 'r', encoding='utf-8') as file:
                # Read all lines from the file
                lines = file.readlines()
                # Get the last x lines
                last_x_lines = lines[-x:]
                # Join the lines into a single string
                return ''.join(last_x_lines)
        except Exception as e:
            # If an error occurs, return the error message
            return str(e)

if __name__ == "__main__":
    # Get file path input from the user
    file_path = input("Enter the path to the text file: ")

    # Get the number of lines to display from the user
    num_lines = int(input("Enter the number of lines to display: "))

    # Create an instance of the Tail class with the specified file path
    # 'tail' is an instance of the Tail class, with 'file_path' set to the value entered by the user
    tail = Tail(file_path)

    # Call the display_last_lines method with the specified number of lines
    # 'tail.display_last_lines(num_lines)' calls the display_last_lines method of the 'tail' instance
    # 'num_lines' is passed as an argument to the method
    print(tail.display_last_lines(num_lines))