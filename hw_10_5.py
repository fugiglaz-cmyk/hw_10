from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from pathlib import Path


class DataProcessor(ABC):
    def process(self, source: str) -> None:
        """
        Executes the complete data processing algorithm.

        Args:
            source (str): Path or name of the source file.

        Returns:
            None: Loads, validates, transforms and saves data.
        """
        print("Початок обробки")
        data = self.load(source)
        self.validate(data)
        transformed = self.transform(data)
        self.save(transformed)
        print("Обробку завершено")

    @abstractmethod
    def load(self, source) -> None:
        """
        Loads data from a source.

        Args:
            source (str): Path or name of the source file.

        Returns:
            Any: Loaded data.

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        pass

    @abstractmethod
    def validate(self, data) -> None:
        """
        Validates loaded data.

        Args:
            data (Any): Data that needs validation.

        Returns:
            None: Confirms that data is valid.

        Raises:
            ValueError: If data is invalid.
        """
        pass

    @abstractmethod
    def transform(self, data) -> None:
        """
        Transforms data into the required format.

        Args:
            data (Any): Validated source data.

        Returns:
            Any: Transformed data.
        """
        pass

    @abstractmethod
    def save(self, data) -> None:
        """
        Saves transformed data.

        Args:
            data (Any): Data to save.

        Returns:
            None: Saves the processed data.
        """
        pass


class CSVImporter(DataProcessor):
    def load(self, source: str) -> None:
        """
        Loads CSV data.

        Args:
            source (str): Name or path of the CSV file.

        Returns:
            list: List of loaded values as strings.
        """
        print(f"Завантаження CSV: {source}")
        return [
            "100",
            "200",
            "300"
        ]

    def validate(self, data: list) -> None:
        """
        Checks whether CSV data is not empty.

        Args:
            data (list): Loaded CSV data.

        Returns:
            None: Confirms that the data is not empty.

        Raises:
            ValueError: If the data is empty.
        """
        print("Перевірка CSV")
        if not data:
            raise ValueError("Порожні дані")

    def transform(self, data: list) -> None:
        """
        Converts CSV string values into integers.

        Args:
            data (list): List of string values.

        Returns:
            list: List of integer values.
        """
        print("Трансформація CSV")
        return [int(value) for value in data]

    def save(self, data: list) -> None:
        """
        Displays the processed CSV data.

        Args:
            data (list): Transformed integer values.

        Returns:
            None: Prints the saved data.
        """
        print(f"Збереження CSV: {data}")


class JSONImporter(DataProcessor):
    def load(self, source: str) -> None:
        """
        Loads JSON data.

        Args:
            source (str): Name or path of the JSON file.

        Returns:
            dict: Dictionary containing loaded values.
        """
        print(f"Завантаження JSON: {source}")
        return {
            "values": [100, 200, 300]
        }

    def validate(self, data: dict) -> None:
        """
        Checks whether the JSON data contains the required field.

        Args:
            data (dict): Loaded JSON dictionary.

        Returns:
            None: Confirms that the required field exists.

        Raises:
            ValueError: If the values field is missing.
        """
        print("Перевірка JSON")
        if "values" not in data:
            raise ValueError("Відсутнє поле values")

    def transform(self, data: dict) -> None:
        """
        Calculates the sum of JSON values.

        Args:
            data (dict): Dictionary containing a list of values.

        Returns:
            dict: Dictionary containing the calculated total.
        """
        print("Трансформація JSON")
        return {
            "total": sum(data["values"])
        }

    def save(self, data: dict) -> None:
        """
        Displays the processed JSON data.

        Args:
            data (dict): Transformed JSON data.

        Returns:
            None: Prints the saved data.
        """
        print(f"Збереження JSON: {data}")


class XMLImporter(DataProcessor):
    def __init__(self, output_path: str = "output.xml") -> None:
        """
        Initializes the XML importer.

        Args:
            output_path (str): Path where the processed XML file
                               will be saved.

        Returns:
            None: Initializes the output file path.
        """
        self.output_path = output_path

    def load(self, source: str) -> None:
        """
        Loads and parses an XML file.

        Args:
            source (str): Path to the source XML file.

        Returns:
            Element: Root element of the XML document.

        Raises:
            ValueError: If the XML file contains invalid syntax.
        """
        print(f"Завантаження XML: {source}")
        try:
            return ET.parse(source).getroot()
        except ET.ParseError as e:
            raise ValueError(f"Некоректний XML: {e}")

    def validate(self, data: ET.Element) -> None:
        """
        Validates the structure of the XML document.

        Args:
            data (ET.Element): Root element of the XML document.

        Returns:
            None: Confirms that the XML structure is valid.

        Raises:
            ValueError: If the root element is incorrect,
                        data is empty or item elements are missing.
        """
        print("Перевірка XML")

        if data is None:
            raise ValueError("Порожні дані")

        if data.tag != "root":
            raise ValueError("Кореневий елемент має бути <root>")

        if not data.findall("item"):
            raise ValueError("Не знайдено жодного елемента <item>")

    def transform(self, data: ET.Element) -> None:
        """
        Extracts XML item values and converts them into integers.

        Args:
            data (ET.Element): Root element of the XML document.

        Returns:
            list: List of extracted integer values.
        """
        print("Трансформація XML")
        result = []

        for item in data.findall("item"):
            text = (item.text or "").strip()
            if text:
                result.append(int(text))

        return result

    def save(self, data: list) -> None:
        """
        Creates and saves a new XML file.

        Args:
            data (list): List of integer values to save.

        Returns:
            None: Creates and writes the XML file.
        """
        print(f"Збереження XML: {data}")

        root = ET.Element("root")

        for value in data:
            item = ET.SubElement(root, "item")
            item.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")
        tree.write(
            self.output_path,
            encoding="utf-8",
            xml_declaration=True
        )


csv_processor = CSVImporter()
json_processor = JSONImporter()
xml_processor = XMLImporter()

csv_processor.process("sales.csv")

print("-" * 40)

json_processor.process("sales.json")

print("-" * 10)

Path("sales.xml").write_text(
    "<root><item>100</item><item>200</item><item>300</item></root>",
    encoding="utf-8",
)

xml_processor.process("sales.xml")
