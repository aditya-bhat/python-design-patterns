from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    """
    Abstract base class defining the interface for cloning.
    """

    @abstractmethod
    def clone(self):
        """
        Create and return a clone of the object.

        Returns:
            Prototype: A new instance cloned from the prototype.
        """
        pass

class Document(Prototype):
    """
    Concrete implementation of Prototype representing a document.
    """

    def __init__(self, content, images, formatting, annotations):
        """
        Initialize the Document object.

        Args:
            content (str): The content of the document.
            images (list): A list of images in the document.
            formatting (str): The formatting style of the document.
            annotations (list): A list of annotations in the document.
        """
        self.content = content
        self.images = deepcopy(images)
        self.formatting = formatting
        self.annotations = deepcopy(annotations)

    def clone(self):
        """
        Create and return a clone of the document.

        Returns:
            Document: A new instance cloned from the prototype.
        """
        return Document(self.content, self.images, self.formatting, self.annotations)

    def display(self):
        """
        Display the contents of the document.
        """
        print("Content:", self.content)
        print("Images:", self.images)
        print("Formatting:", self.formatting)
        print("Annotations:", self.annotations)

if __name__ == "__main__":
    # Example usage
    original_doc = Document("Hello, World!", ["Image1.png"], "Basic", ["Annotation1"])
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

    # Displaying the contents of both documents
    print("\n\nOriginal Document:")
    original_doc.display()
    print("\nCopied Document:")
    cloned_doc.display()
