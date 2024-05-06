from copy import deepcopy

def prototype(cls):
    """
    Decorator function to add prototype functionality to a class.

    Args:
        cls: The class to be decorated as a prototype.

    Returns:
        The decorated class with prototype functionality.
    """
    # Add a clone method to the class
    cls.clone = lambda self: deepcopy(self)
    return cls

class PrototypeRegistry:
    def __init__(self):
        """Initialize the prototype registry."""
        self.prototypes = {}

    def register(self, name, prototype):
        """
        Register a prototype with a given name.

        Args:
            name (str): The name of the prototype.
            prototype: The prototype object to register.
        """
        self.prototypes[name] = prototype

    def get(self, name):
        """
        Retrieve a prototype by name.

        Args:
            name (str): The name of the prototype to retrieve.

        Returns:
            The cloned instance of the prototype.
        """
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise KeyError(f"Prototype '{name}' not found.")

@prototype
class Document:
    def __init__(self, content, images, formatting, annotations):
        """
        Initialize a document object.

        Args:
            content (str): The content of the document.
            images (list): List of images in the document.
            formatting (str): The formatting style of the document.
            annotations (list): List of annotations in the document.
        """
        self.content = content
        self.images = images
        self.formatting = formatting
        self.annotations = annotations

    def display(self):
        """Display the contents of the document."""
        print("Content:", self.content)
        print("Images:", self.images)
        print("Formatting:", self.formatting)
        print("Annotations:", self.annotations)

if __name__ == "__main__":
    # Create a prototype registry
    registry = PrototypeRegistry()

    # Register prototype documents
    registry.register("basic", Document("Basic Document", [], "Basic", []))
    registry.register("advanced", Document("Advanced Document", ["Image1.png"], "Advanced", ["Annotation1"]))

    # Retrieve and display prototype documents
    basic_doc = registry.get("basic")
    advanced_doc = registry.get("advanced")

    print("Basic Document:")
    basic_doc.display()

    print("\nAdvanced Document:")
    advanced_doc.display()

    # Clone a prototype document from the registry
    cloned_doc = registry.get("basic").clone()

    # Modify the cloned document
    cloned_doc.content = "Cloned Basic Document"
    cloned_doc.images.append("Image2.png")

    print("\nCloned Basic Document:")
    cloned_doc.display()

    print("\nOriginal Basic Document:")
    basic_doc.display()
