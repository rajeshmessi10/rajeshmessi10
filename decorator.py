def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function
        result = func(*args, **kwargs)

        print(result)
        # Convert the result to uppercase
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

# Using the decorator
@uppercase_decorator
def say_hello(name):
    return f"Hello, {name}!"

@uppercase_decorator
def get_greeting():
    return "Good morning!"

# Test the functions
print(say_hello(2))  # Output: HELLO, ALICE!
print(get_greeting())      # Output: GOOD MORNING!
