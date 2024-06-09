if __name__ == "__main__":
    # Import both implementations implementation
    from functional_solution import tail as functional_tail
    from oop_solution import Tail as OOPTail

    # Define the test file path
    test_file_path = 'test_file.txt'

    # Define the number of lines to display
    num_lines = 3

    # Call the functional implementation and store the result
    functional_result = functional_tail(test_file_path, num_lines)

    # Create an instance of the OOP implementation
    oop_tail = OOPTail(test_file_path)

    # Call the display_last_lines method of the OOP implementation and store the result
    oop_result = oop_tail.display_last_lines(num_lines)

    # Compare the results of both implementations
    if functional_result == oop_result:
        print("Test Passed: Both implementations display the same result.")
    else:
        print("Test Failed: Implementations produce different results.")
        print("Functional Result:")
        print(functional_result)
        print("OOP Result:")
        print(oop_result)