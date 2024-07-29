import re

def extract_numbers(text):
    # \d+ matches one or more digits
    numbers = re.findall(r'-?\d+', text)
    print(numbers)
    # Convert the extracted numbers from strings to integers
    numbers = [int(num) for num in numbers]
    return numbers

# Example usage
text = "The 2 little -12 kids -567have 345 toys in total."
numbers = extract_numbers(text)
print(numbers)  # Output: [2, 12, 345]
