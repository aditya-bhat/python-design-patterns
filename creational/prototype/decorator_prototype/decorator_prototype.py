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
    # Create a prototype document
    original_doc = Document("Prototype Document", ["Image1.png"], "Basic", ["Annotation1"])

    # Clone the prototype document
    cloned_doc = original_doc.clone()

    # Display the contents of the original document
    print("Original Document:")
    original_doc.display()

    # Display the contents of the cloned document
    print("\nCloned Document:")
    cloned_doc.display()

    # Making changes to the original document
    original_doc.images.append("Image2.png")
    original_doc.annotations.append("Annotation2")
    original_doc.content = "Updated Content"

    # Displaying the contents of both documents
    print("\nOriginal Document:")
    original_doc.display()
    print("\nCopied Document:")
    cloned_doc.display()
