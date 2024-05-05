# Singleton Pattern Example

The Singleton pattern is a design pattern that restricts the instantiation of a class to one "single" instance. This is useful when exactly one object is needed to coordinate actions across the system.

## Description

In this Python example, we demonstrate the implementation of the Singleton pattern using both a class-based approach and a decorator-based approach.

- **Class-based Singleton**: In the `Singleton` class implementation, the `__new__` method is overridden to control the creation of instances. The class maintains a class variable `_instance` to hold the single instance. When an instance is requested, it checks if `_instance` is already set. If not, it creates a new instance and assigns it to `_instance`. Subsequent requests return the existing instance.

- **Decorator-based Singleton**: The `singleton` decorator function takes a class as its argument and returns a closure that manages the instantiation of the class as a singleton. Inside the closure, a dictionary is used to store instances of decorated classes. When an instance is requested, the closure checks if the class instance exists in the dictionary. If not, it creates a new instance and stores it in the dictionary. Subsequent requests return the existing instance.

## Common Examples in Python

Some common examples in Python where the Singleton pattern is used include:

- **Logger**: In many logging frameworks, a Singleton pattern is used to provide a global logging instance accessible from anywhere in the codebase.
- **Database Connection Pool**: In applications that require database connections, a Singleton pattern can be used to manage a pool of database connections, ensuring efficient resource utilization.
- **Configuration Settings**: Singleton pattern can be used to manage application configuration settings, ensuring that there is only one instance of configuration settings loaded into memory.

## Pros and Cons of Singleton Pattern

### Pros:
- **Controlled Access**: Provides a single point of access to the instance, allowing controlled access to the shared resource.
- **Resource Sharing**: Enables resource sharing across multiple parts of the codebase.
- **Lazy Initialization**: Supports lazy initialization, i.e., the instance is created only when it is first requested.

### Cons:
- **Global State**: Can introduce global state, making it harder to reason about the code and potentially leading to tight coupling.
- **Testing Difficulty**: Can make unit testing difficult due to global state and tight coupling.
- **Concurrency Issues**: Not inherently thread-safe, leading to potential concurrency issues if not properly synchronized in a multithreaded environment.

## General Ways to Implement Singleton

- **Class-based Approach**: Use a class with a private constructor and a static method to provide access to the single instance.
- **Metaclass-based Approach**: Define a metaclass that controls the creation of instances and ensures only one instance exists.
- **Decorator-based Approach**: Use a decorator function to wrap the class and manage the instantiation of the single instance.

## Relation to SOLID Principles

- **Single Responsibility Principle (SRP)**: The Singleton pattern doesn't inherently violate SRP, but it can sometimes lead to classes with multiple responsibilities due to the global state it introduces.
- **Open/Closed Principle (OCP)**: The Singleton pattern can violate OCP if the class is tightly coupled with the Singleton instance, making it difficult to extend or modify behavior.
- **Liskov Substitution Principle (LSP)**: The Singleton pattern doesn't directly relate to LSP since it's about object-oriented inheritance and substitutability.
- **Interface Segregation Principle (ISP)**: The Singleton pattern doesn't directly relate to ISP since it's more about defining interfaces and client-specific interfaces.
- **Dependency Inversion Principle (DIP)**: The Singleton pattern can make it difficult to inject dependencies into classes that depend on the Singleton instance, potentially violating DIP.

## Example Usage

```python
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
