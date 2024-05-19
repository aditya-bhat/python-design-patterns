import time
from functools import wraps

def timing_method(method):
    """
    A method decorator that prints the time a method takes to execute.

    Parameters:
    method (function): The method to be decorated.

    Returns:
    function: The wrapped method with timing functionality.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that adds timing functionality to the decorated method.

        Parameters:
        *args: Variable length argument list for the decorated method.
        **kwargs: Arbitrary keyword arguments for the decorated method.

        Returns:
        The result of the decorated method.
        """
        start_time = time.time()  # Record the start time
        result = method(*args, **kwargs)  # Call the original method with its arguments
        end_time = time.time()  # Record the end time

        # Calculate the duration and print it
        duration = end_time - start_time
        print(f"Method {method.__name__} took {duration:.4f} seconds to execute")

        return result  # Return the result of the original method

    return wrapper  # Return the wrapper function

def timing_class(cls):
    """
    A class decorator that applies the timing_method decorator to all methods of a class.

    Parameters:
    cls (class): The class to be decorated.

    Returns:
    class: The decorated class with timing functionality added to its methods.
    """
    for attr in dir(cls):
        if callable(getattr(cls, attr)) and not attr.startswith("__"):
            original_method = getattr(cls, attr)
            decorated_method = timing_method(original_method)
            setattr(cls, attr, decorated_method)
    return cls

@timing_class
class ExampleClass:
    """
    A sample class to demonstrate the timing class decorator.

    Methods:
    example_method(n): Sleeps for n seconds.
    another_method(n): Sleeps for n/2 seconds.
    """

    def example_method(self, n):
        """
        A sample method that sleeps for n seconds.

        Parameters:
        n (int): The number of seconds to sleep.

        Returns:
        str: A message indicating the method has completed.
        """
        time.sleep(n)
        return "example_method completed"

    def another_method(self, n):
        """
        Another sample method that sleeps for n/2 seconds.

        Parameters:
        n (int): The number of seconds to sleep divided by 2.

        Returns:
        str: A message indicating the method has completed.
        """
        time.sleep(n / 2)
        return "another_method completed"

if __name__ == "__main__":
    # Create an instance of the decorated class
    example_instance = ExampleClass()

    # Call the decorated methods
    result1 = example_instance.example_method(2)
    print(result1)

    result2 = example_instance.another_method(4)
    print(result2)
