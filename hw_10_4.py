import copy


class Document:
    def __init__(self, title: str, author: str, content: str, sections=None, metadata=None):
        """
        Initializes a document object.

        Args:
            title (str): Title of the document.
            author (str): Author of the document.
            content (str): Main content of the document.
            sections (list): List of document sections.
            metadata (dict): Additional document information.

        Returns:
            None: Initializes document attributes.
        """
        self.title = title
        self.author = author
        self.content = content
        self.sections = sections if sections is not None else []
        self.metadata = metadata if metadata is not None else {}

    def clone(self):
        """
        Creates a deep copy of the current document.

        Args:
            None.

        Returns:
            Document: A completely independent copy of the document.
        """
        return copy.deepcopy(self)

    def __repr__(self):
        """
        Returns a string representation of the document.

        Args:
            None.

        Returns:
            str: Document title, author, sections and metadata.
        """
        return (
            f"Document(title={self.title!r}, author={self.author!r}, "
            f"sections={self.sections}, metadata={self.metadata})"
        )


class PrototypeRegistry:
    def __init__(self):
        """
        Initializes an empty prototype registry.

        Args:
            None.

        Returns:
            None: Creates an empty dictionary for templates.
        """
        self._templates = {}

    def register(self, name: str, prototype: Document):
        """
        Registers a document prototype in the registry.

        Args:
            name (str): Name used to identify the template.
            prototype (Document): Document object used as a prototype.

        Returns:
            None: Adds the prototype to the registry.
        """
        self._templates[name] = prototype

    def unregister(self, name: str):
        """
        Removes a document prototype from the registry.

        Args:
            name (str): Name of the template to remove.

        Returns:
            None: Deletes the specified template.

        Raises:
            KeyError: If the template does not exist.
        """
        if name not in self._templates:
            raise KeyError(f"Шаблон '{name}' не знайдено")
        del self._templates[name]

    def clone(self, name: str):
        """
        Creates a copy of a registered document prototype.

        Args:
            name (str): Name of the template to clone.

        Returns:
            Document: An independent copy of the selected document.

        Raises:
            KeyError: If the template does not exist.
        """
        if name not in self._templates:
            raise KeyError(f"Шаблон '{name}' не знайдено")
        return self._templates[name].clone()

    def get_templates(self):
        """
        Returns names of all registered templates.

        Args:
            None.

        Returns:
            list: List of registered template names.
        """
        return list(self._templates.keys())


registry = PrototypeRegistry()

registry.register("technical_report", Document(
    title="Технічний звіт",
    author="Технічний відділ",
    content="Опис технічного рішення",
    sections=["Вступ", "Архітектура", "Тестування", "Висновки"],
    metadata={
        "type": "report",
        "tags": ["tech", "report"],
        "version": {"major": 1, "minor": 0}
    },
))

registry.register("study_document", Document(
    title="Навчальний документ",
    author="Кафедра",
    content="Навчальний матеріал",
    sections=["Мета", "Теорія", "Практика", "Контрольні питання"],
    metadata={
        "type": "study",
        "tags": ["education"],
        "version": {"major": 1, "minor": 0}
    },
))

registry.register("commercial_offer", Document(
    title="Комерційна пропозиція",
    author="Відділ продажів",
    content="Умови співпраці",
    sections=["Про компанію", "Пропозиція", "Вартість", "Контакти"],
    metadata={
        "type": "offer",
        "tags": ["sales"],
        "version": {"major": 1, "minor": 0}
    },
))

print("Доступні шаблони:", registry.get_templates())

copies = {}

for name in registry.get_templates():
    copies[name] = [registry.clone(name) for _ in range(3)]

for name, docs in copies.items():
    first = docs[0]

    first.title = f"ЗМІНЕНО: {first.title}"
    first.sections.append("Новий розділ")
    first.metadata["version"]["major"] = 99
    first.metadata["tags"].append("changed")

for name, docs in copies.items():
    prototype = registry._templates[name]
    original_title = prototype.title

    assert docs[0].title != original_title
    assert "Новий розділ" in docs[0].sections
    assert docs[0].metadata["version"]["major"] == 99

    for other in docs[1:]:
        assert other.title == original_title
        assert "Новий розділ" not in other.sections
        assert other.metadata["version"]["major"] == 1
        assert "changed" not in other.metadata["tags"]

    assert "Новий розділ" not in prototype.sections
    assert prototype.metadata["version"]["major"] == 1
    assert "changed" not in prototype.metadata["tags"]

    print(f"[OK] {name}: зміни копії не вплинули на прототип та інші копії")

registry.unregister("study_document")

print("Після видалення:", registry.get_templates())
