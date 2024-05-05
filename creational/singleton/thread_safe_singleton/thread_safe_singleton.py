import threading

def singleton(cls):
    """
    Decorator function to implement the Singleton pattern for a class with thread-safe locking.

    Args:
        cls: The class to be decorated as a Singleton.

    Returns:
        The closure `get_instance` which manages the instantiation of the class as a singleton.
    """
    instances = {}  # Dictionary to store instances of decorated classes
    lock = threading.Lock()  # Thread-safe lock for synchronization

    def get_instance(*args, **kwargs):
        """
        Closure to instantiate the decorated class as a singleton with thread-safe locking.

        If an instance of the decorated class does not exist, it creates a new instance and stores it in
        the `instances` dictionary. Otherwise, it returns the existing instance.

        Args:
            *args: Positional arguments for class initialization.
            **kwargs: Keyword arguments for class initialization.

        Returns:
            The single instance of the decorated class.
        """
        if cls not in instances:
            with lock:  # Acquire lock for thread-safe access
                if cls not in instances:  # Double check to prevent race conditions
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
    singleton_initial = Singleton()
    singleton_initial.set_data("Data -1")
    print(singleton_initial.get_data()) # Output: Data -1
    threads = []
    for i in range(5):
        thread = threading.Thread(target=lambda i=i: Singleton().set_data(f"Data {i}"))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(singleton_initial.get_data()) # Output: 'Data <0-4>'
    
    singleton_end = Singleton()
    singleton_end.set_data("Data INF")

    # Both instances are the same
    print(singleton_initial is singleton_end)  # Output: True
    print(singleton_initial.get_data())  # Output: 'Data INF'
    print(singleton_end.get_data())  # Output: 'Data INF'
