"""
    Author: Dan Shaw
    Title: CustomMath
    Desc: Contains custom math and validation functions
"""

class Validation:

    # Validates whether inputQuery is a valid number by trying to convert to a float
    # Returns the converted float if successfull and None if fails
    def validateFloat(inputQuery):
        try:
            return float(inputQuery)
        except:
            return None

    def validateInt(inputQuery):
        try:
            return int(inputQuery)
        except:
            return None
