if __name__ == "__main__":
    # Write your solution here
    pass
class Car:
    """Базовый класс для автомобилей."""
    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация объекта класса Car.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Строковое представление объекта класса Car.
        :return: Строковое представление автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Представление объекта класса Car для вывода в интерпретаторе Python.
        :return: Представление объекта класса Car.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

class PassengerCar(Car):
    """Дочерний класс, представляющий легковой автомобиль."""
    def __init__(self, brand: str, model: str, year: int, num_seats: int):
        """
        Инициализация объекта класса PassengerCar.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param num_seats: Количество мест в автомобиле.
        """
        super().__init__(brand, model, year)
        self.num_seats = num_seats

    def __str__(self) -> str:
        """
        Строковое представление объекта класса PassengerCar.
        :return: Строковое представление легкового автомобиля.
        """
        return f"{super().__str__()} - Легковой автомобиль с {self.num_seats} местами"

    # Перегрузка метода для демонстрации расширения функциональности
    def __repr__(self) -> str:
        """
        Представление объекта класса PassengerCar для вывода в интерпретаторе Python.
        :return: Представление объекта класса PassengerCar.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, num_seats={self.num_seats!r})"
