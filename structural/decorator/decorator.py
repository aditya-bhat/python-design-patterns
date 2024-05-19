import time

def timing(func):
    """
    A decorator that prints the time a function takes to execute.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The wrapped function with timing functionality.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that adds timing functionality to the decorated function.

        Parameters:
        *args: Variable length argument list for the decorated function.
        **kwargs: Arbitrary keyword arguments for the decorated function.

        Returns:
        The result of the decorated function.
        """
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function with its arguments
        end_time = time.time()  # Record the end time

        # Calculate the duration and print it
        duration = end_time - start_time
        print(f"Function {func.__name__} took {duration:.4f} seconds to execute")

        return result  # Return the result of the original function

    return wrapper  # Return the wrapper function

# Example usage of the @timing decorator

@timing
def example_function(n):
    """
    A sample function that sleeps for n seconds.

    Parameters:
    n (int): The number of seconds to sleep.

    Returns:
    str: A message indicating the function has completed.
    """
    time.sleep(n)
    return "Function completed"

if __name__ == "__main__":
    # Calling the decorated function
    result = example_function(2)
    print(result)
