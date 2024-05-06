# Creational Design Patterns

Creational design patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. They aim to make a system independent of how its objects are created, composed, and represented.

## Use Case

Creational design patterns are used when a system needs to be independent of how its objects are created, composed, and represented. They provide flexibility and reuse by encapsulating object creation mechanisms.

## Types of Creational Design Patterns

### 1. Singleton Pattern

- **Use Case**: When you want to ensure that a class has only one instance and provides a global point of access to that instance.
- **Common Use Case**: Logging, Database Connection Managers.

### 2. Factory Method Pattern

- **Use Case**: When you want to delegate the responsibility of instantiation to subclasses.
- **Common Use Case**: Frameworks for UI controls, Database drivers.

### 3. Abstract Factory Pattern

- **Use Case**: When you want to provide an interface for creating families of related or dependent objects without specifying their concrete classes.
- **Common Use Case**: GUI toolkits, Cross-platform libraries.

### 4. Builder Pattern

- **Use Case**: When you want to separate the construction of a complex object from its representation so that the same construction process can create different representations.
- **Common Use Case**: Construction of complex objects like documents, emails.

### 5. Prototype Pattern

- **Use Case**: When you want to create new objects by copying an existing object, known as the prototype, instead of creating new instances from scratch.
- **Common Use Case**: Graphic design software, Game development.

## Similarities and Differences

### Similarities:

1. **Object Creation Control**: All five patterns involve controlling the instantiation process of objects, albeit in different ways.

2. **Encapsulation of Creation Logic**: They encapsulate the object creation logic, hiding the details of object creation from the client code.

3. **Flexibility and Reusability**: They promote flexibility and reusability by providing standardized ways to create objects, allowing developers to extend or modify the system without impacting existing code.

### Differences:

1. **Scope of Responsibility**:
   - **Singleton**: Ensures that a class has only one instance and provides a global point of access to that instance.
   - **Factory Method**: Defines an interface for creating objects, but allows subclasses to alter the type of objects that will be created.
   - **Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
   - **Builder**: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
   - **Prototype**: Creates new objects by copying an existing object, known as the prototype.

2. **Usage and Intent**:
   - **Singleton**: Used when exactly one instance of a class is needed, such as managing shared resources or controlling access to a resource.
   - **Factory Method**: Used when a class cannot anticipate the class of objects it must create, or when subclasses should specify the objects to be created.
   - **Abstract Factory**: Used when a system should be independent of how its objects are created, composed, and represented, and when families of related objects must be created.
   - **Builder**: Used when constructing complex objects step by step is required, allowing different representations of an object to be constructed using the same construction process.
   - **Prototype**: Used when creating new objects by copying an existing object is more efficient than creating new instances from scratch.

3. **Granularity of Object Creation**:
   - **Singleton**: Manages the creation of a single instance of a class.
   - **Factory Method**: Delegates the creation of objects to subclasses, allowing different subclasses to instantiate different types of objects.
   - **Abstract Factory**: Creates families of related or dependent objects, providing multiple factory methods for creating different types of related objects.
   - **Builder**: Constructs complex objects by breaking down the construction process into multiple steps, providing a director to coordinate the construction process.
   - **Prototype**: Creates new objects by copying an existing object, allowing for fine-grained control over object creation.

4. **Relationship to Other Patterns**:
   - **Singleton**: Often used in conjunction with other patterns, such as Factory Method, Abstract Factory, and Builder, to control object creation and manage dependencies.
   - **Factory Method**: Can be combined with other patterns like Singleton and Abstract Factory to provide more flexible object creation mechanisms.
   - **Abstract Factory**: Can use Factory Methods to create individual objects within a family of related objects.
   - **Builder**: Can be used with Factory Methods to create complex objects step by step, or with Singleton to ensure the builder instance is unique.
   - **Prototype**: Can be used alongside other patterns to create new objects by copying existing ones, providing a flexible approach to object creation.

# Examples of how Creational Design Patterns can be used together

Creational design patterns provide flexible and reusable solutions for object creation in software systems. They can be used together to address complex design challenges and promote maintainability and extensibility. Here are examples of how different creational design patterns can be combined:

## 1. Singleton with Factory Method

- **Scenario**: Implementing a logging system where different types of loggers need to be created based on the context.
- **Usage**: Implement the logger as a Singleton to ensure only one instance exists. Use the Factory Method pattern to provide different types of loggers (e.g., FileLogger, ConsoleLogger) based on the context.

## 2. Abstract Factory with Builder

- **Scenario**: Developing a UI framework for different platforms (e.g., desktop, mobile) with varying UI components.
- **Usage**: Implement the UI component creation as an Abstract Factory to provide families of related objects (e.g., DesktopUIFactory, MobileUIFactory). Use the Builder pattern to construct complex UI components step by step, ensuring consistency and flexibility across different platforms.

## 3. Singleton with Abstract Factory

- **Scenario**: Managing database connections where different types of database connections need to be provided.
- **Usage**: Implement the database connection manager as a Singleton to ensure only one instance exists. Use the Abstract Factory pattern to provide families of related objects (e.g., MySQLConnectionFactory, PostgreSQLConnectionFactory) for creating database connections.

## 4. Factory Method with Builder

- **Scenario**: Developing a document generation system with different types of documents (e.g., reports, invoices) with varying complexity.
- **Usage**: Implement the document creation as a Factory Method to delegate the creation of specific document types to subclasses. Use the Builder pattern to construct complex documents step by step, allowing different representations of documents to be created using the same construction process.

## 5. Singleton with Prototype

- **Scenario**: Managing game objects in a game development environment with unique properties.
- **Usage**: Implement the game object manager as a Singleton to ensure only one instance exists. Use the Prototype pattern to create new game objects by copying existing ones, allowing for efficient creation of objects with customized properties.

## 6. Abstract Factory with Prototype

- **Scenario**: Designing a graphic design software where users can create custom graphic objects (e.g., shapes, icons) based on predefined templates.
- **Usage**: Implement the graphic object creation as an Abstract Factory to provide families of related objects (e.g., ShapeFactory, IconFactory) for creating graphic objects. Integrate the Prototype pattern to allow users to clone existing graphic objects (e.g., predefined templates) and customize them to create new graphic objects efficiently.

## 7. Builder with Prototype

- **Scenario**: Creating complex configurations for virtual machines where users can customize various parameters (e.g., CPU, memory, storage) based on predefined configurations.
- **Usage**: Implement the configuration creation as a Builder to construct complex virtual machine configurations step by step, allowing users to specify different parameters. Integrate the Prototype pattern to allow users to clone existing configurations and modify them to create new configurations efficiently.

These examples demonstrate how creational design patterns can be combined to address various design challenges, providing flexibility, reusability, and maintainability in software development.

By understanding the use cases, types, similarities, and how they are used together, you can choose the appropriate creational design patterns to design flexible, reusable, and maintainable systems.
