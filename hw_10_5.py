from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from pathlib import Path


class DataProcessor(ABC):
    def process(self, source: str):
        """method for process algorithm"""
        print("Початок обробки")
        data = self.load(source)
        self.validate(data)
        transformed = self.transform(data)
        self.save(transformed)
        print("Обробку завершено")

    @abstractmethod
    def load(self, source):
        pass

    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def save(self, data):
        pass


class CSVImporter(DataProcessor):
    def load(self, source: str):
        """method for load"""
        print(f"Завантаження CSV: {source}")
        return [
            "100",
            "200",
            "300"
        ]

    def validate(self, data: str):
        """method for validation"""
        print("Перевірка CSV")
        if not data:
            raise ValueError("Порожні дані")

    def transform(self, data: str):
        """method for transform"""
        print("Трансформація CSV")
        return [int(value) for value in data]

    def save(self, data: str):
        """method for save"""
        print(f"Збереження CSV: {data}")


class JSONImporter(DataProcessor):
    def load(self, source: str):
        """method for load"""
        print(f"Завантаження JSON: {source}")
        return {
            "values": [100, 200, 300]
        }

    def validate(self, data: str):
        """method for validation"""
        print("Перевірка JSON")
        if "values" not in data:
            raise ValueError(
                "Відсутнє поле values"
            )

    def transform(self, data: str):
        """method for transform"""
        print("Трансформація JSON")
        return {
            "total": sum(data["values"])
        }

    def save(self, data: str):
        """method for save"""
        print(f"Збереження JSON: {data}")


class XMLImporter(DataProcessor):
    def __init__(self, output_path="output.xml"):
        """method for initialization"""
        self.output_path = output_path

    def load(self, source: str):
        """method for load"""
        print(f"Завантаження XML: {source}")
        try:
            return ET.parse(source).getroot()
        except ET.ParseError as e:
            raise ValueError(f"Некоректний XML: {e}")

    def validate(self, data: str):
        """method for validation"""
        print("Перевірка XML")
        if data is None:
            raise ValueError("Порожні дані")
        if data.tag != "root":
            raise ValueError("Кореневий елемент має бути <root>")
        if not data.findall("item"):
            raise ValueError("Не знайдено жодного елемента <item>")

    def transform(self, data: str):
        """method for transform"""
        print("Трансформація XML")
        result = []
        for item in data.findall("item"):
            text = (item.text or "").strip()
            if text:
                result.append(int(text))
        return result

    def save(self, data: str):
        """method for save"""
        print(f"Збереження XML: {data}")
        root = ET.Element("root")
        for value in data:
            item = ET.SubElement(root, "item")
            item.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")  # Python 3.9+
        tree.write(self.output_path, encoding="utf-8", xml_declaration=True)


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
