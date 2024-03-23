# Unit test for all error checking functions

# Unit test for interger---------------------------------------------------------------------

def integer_input():                                                           # Will ask for users input and convert it into an integer
    x = input("Enter for interger test: ")                                     # If unable to convert into an integer the test will fail
    return int(x)                                                              # If able it will be the same class as expected result int and test will pass

def test_integer_input():
    # Arrange
    expected = int
    
    # Act
    result = type(integer_input())
    
    # Assert
    assert result == expected
        
# Unit test for String-----------------------------------------------------------------------------

def string_input():                                                            # Will ask for users input and convert it into a string
    x = input("Enter for string test: ")                                       # If unable to convert into a string the test will fail
    return x                                                                   # If able it will be the same class as expected result str and test will pass

def test_string_input():
    # Arrange
    expected = str
    
    # Act
    result = type(string_input())
    
    # Assert
    assert result == expected


# Unit test for float--------------------------------------------------------------------------------


def float_input():                                                            # Will ask for users input and convert it into a float
    x = input("Enter for a float test: ")                                     # If unable to convert into a float the test will fail
    return float(x)                                                           # If able it will be the same class as expected result float and test will pass

def test_float_input():
    # Arrange
    expected = float
    
    # Act
    result = type(float_input())
    
    # Assert
    assert result == expected


# To run pytest -s (filename) in the right directory