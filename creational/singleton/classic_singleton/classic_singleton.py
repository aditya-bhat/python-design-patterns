class Singleton:
    """
    Class implementing the Singleton pattern.
    """
    # Class variable to store the single instance of the class.
    _instance = None

    def __new__(cls):
        """
        Create a new instance of the class or return the existing instance if it already exists.

        This method is overridden to control the creation of instances. 
        It checks if the _instance attribute is None. 
        If it is, a new instance is created using super().__new__(cls). 
        This is where the Singleton’s uniqueness is enforced. 
        If an instance already exists, it is returned.

        Returns:
            The single instance of the class.
        """
        if not cls._instance:
            # If _instance is None, create a new instance
            cls._instance = super().__new__(cls)
            # Initialize the data attribute
            cls._instance.data = None
        return cls._instance
        
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
