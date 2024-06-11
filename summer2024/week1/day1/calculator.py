class Calculator:
# Methods
    # Display Menu options and Input Validation
    def menu(self):
        valid_inputs = {"1", "2", "3", "4", "5"}    # Valid inputs
        while True: # Menu
            print("-------- Menu --------\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Quit")
            menu_input = input("----------------------\nPlease choose an option (1-5): ")   # Get menu option choice
            if menu_input in valid_inputs:  # Check for valid input
                return int(menu_input)  # Return menu option choice
            else:   # Incorrect input, error message and loop to show menu options again
                print("\n*************************************\n ERROR: PLEASE TYPE 1, 2, 3, 4, or 5\n*************************************\n")

    # Helper function that checks input is a number or not
    def is_number(self, num):
        try:
            float(num)
            return True # Is a number
        except ValueError:
            return False    # Not a number

    # Get values for operations
    def get_input(self):
        while True:
            input_num = input("Please enter a number: ")    # Get input number
            if self.is_number(input_num):   # Check if input is a number
                return float(input_num)   # Is a number, return input number as float since it is a string by default
            else:   # Not a number, error message and loop to get input again
                print("\n*************************************\n ERROR: NOT A NUMBER\n*************************************\n")
            
    # Run program
    def run(self):
        while True:
            choice = self.menu()    # Get menu choice
            if choice == 1: # Addition
                print("\nYou have chosen addition!")
                first_input = self.get_input()  # Get first input
                second_input = self.get_input() # Get second input
                print(first_input, "+", second_input, "=", self.add(first_input, second_input), "\n")   # Print result
            elif choice == 2:   # Subtraction
                print("\nYou have chosen subtraction!")
                first_input = self.get_input()  # Get first input
                second_input = self.get_input() # Get second input
                print(first_input, "-", second_input, "=", self.subtract(first_input, second_input), "\n")  # Print result
            elif choice == 3:   # Multiplication
                print("\nYou have chosen multiplication!")
                first_input = self.get_input()  # Get first input
                second_input = self.get_input() # Get second input
                print(first_input, "*", second_input, "=", self.multiply(first_input, second_input), "\n")  # Print result
            elif choice == 4:   # Division
                print("\nYou have chosen division!")
                first_input = self.get_input()  # Get first input
                second_input = self.get_input() # Get second input
                if self.divide(first_input, second_input) != None:  # If None, divided by zero
                    print(first_input, "/", second_input, "=", self.divide(first_input, second_input), "\n")    # Else, print result
            elif choice == 5:   # Quit
                print("\nGoodbye!\n")
                break   # Break out of loop to exit program


# Operations
    # Add
    def add(self, a, b):
        return a + b
        
    # Subtract
    def subtract(self, a, b):
        return a - b
        
    # Multiply
    def multiply(self, a, b):
        return a * b
        
    # Divide
    def divide(self, a, b):
        if b == 0:
            print("ERROR: CANNOT DIVIDE BY 0\n")    # Cannot divide by zero
            return None
        else:
            return a / b



# Run the calculator
test = Calculator()
test.run()