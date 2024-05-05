class SingletonMeta(type):
    """
    Metaclass to implement the Singleton pattern.
    """
    _instances = {}  # Dictionary to store instances of classes using this metaclass

    def __call__(cls, *args, **kwargs):
        """
        Override the call method to intercept class instantiation.

        Args:
            cls: The class being instantiated.
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            The existing instance if it exists, otherwise creates a new instance and returns it.
        """
        if cls not in cls._instances:
            # If the class instance does not exist in _instances dictionary, create a new instance
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
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
