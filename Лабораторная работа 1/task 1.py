from typing import Union

class Furniture:
    """
    Абстрактный класс, описывающий мебель.

    Attributes:
        name (str): Название мебели.
        material (str): Материал, из которого изготовлена мебель.
        weight (float): Вес мебели в килограммах.

    Methods:
        move(self, new_location: str) -> None:
            Перемещает мебель в новое место.

        clean(self, cleaning_agent: str) -> str:
            Очищает мебель с использованием указанного средства для чистки.

        assemble(self) -> None:
            Собирает разборчивую мебель.
    """
    def __init__(self, name: str, material: str, weight: float):
        self.name = name
        self.material = material
        self.weight = weight

    def move(self, new_location: str) -> None:
        """
        Перемещает мебель в новое место.

        Args:
            new_location (str): Новое местоположение мебели.

        Returns:
            None
        """
        ...

    def clean(self, cleaning_agent: str) -> str:
        """
        Очищает мебель с использованием указанного средства для чистки.

        Args:
            cleaning_agent (str): Средство для чистки.

        Returns:
            str: Результат чистки.
        """
        ...

    def assemble(self) -> None:
        """
        Собирает разборчивую мебель.

        Returns:
            None
        """
        ...


class Tree:
    """
    Абстрактный класс, описывающий дерево.

    Attributes:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.

    Methods:
        grow(self, growth_rate: float) -> None:
            Позволяет дереву расти с указанной скоростью.

        produce_oxygen(self) -> None:
            Производит кислород в результате фотосинтеза.

        shed_leaves(self) -> None:
            Опростоволосивается, сбрасывая листья.
    """
    def __init__(self, species: str, height: float, age: int):
        self.species = species
        self.height = height
        self.age = age

    def grow(self, growth_rate: float) -> None:
        """
        Позволяет дереву расти с указанной скоростью.

        Args:
            growth_rate (float): Скорость роста дерева.

        Returns:
            None
        """
        ...

    def produce_oxygen(self) -> None:
        """
        Производит кислород в результате фотосинтеза.

        Returns:
            None
        """
        ...

    def shed_leaves(self) -> None:
        """
        Опростоволосивается, сбрасывая листья.

        Returns:
            None
        """
        ...

