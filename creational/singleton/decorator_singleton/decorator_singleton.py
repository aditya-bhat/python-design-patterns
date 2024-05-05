def singleton(cls):
    """
    Decorator function to implement the Singleton pattern for a class.

    Args:
        cls: The class to be decorated as a Singleton.

    Returns:
        The closure `get_instance` which manages the instantiation of the class as a singleton.
    """
    instances = {}  # Dictionary to store instances of decorated classes

    def get_instance(*args, **kwargs):
        """
        Closure to instantiate the decorated class as a singleton.

        If an instance of the decorated class does not exist, it creates a new instance and stores it in
        the `instances` dictionary. Otherwise, it returns the existing instance.

        Args:
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            The single instance of the decorated class.
        """
        if cls not in instances:
            # If the class instance does not exist in instances dictionary, create a new instance
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    """
    Class implementing the Singleton pattern.
    """

    def __init__(self, data=None):
        """
        Initialize the Singleton instance.

        Args:
            data: Initial data for the Singleton instance.
        """
        self.data = data

    def set_data(self, data: str) -> None:
        """
        Set the data for the Singleton instance.

        Args:
            data: Data to be set.
        """
        self.data = data

    def get_data(self) -> str:
        """
        Get the data of the Singleton instance.

        Returns:
            The data of the Singleton instance.
        """
        return self.data


if __name__ == "__main__":
    # Creating an instance of the Classic Singleton
    singleton1 = Singleton()
    singleton1.set_data("Data 1")

    # Accessing the same instance
    singleton2 = Singleton()

    # Both instances are the same
    print(singleton1 is singleton2)  # Output: True
    
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    singleton2.set_data("Data 2")
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'
