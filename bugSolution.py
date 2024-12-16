def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error in another suitable way

result = my_function(10, 0) # This will now return 0 instead of causing an error.