class CustomList:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер списка должен быть положительным числом.")
        self._list = [0] * size
        self.size = size
        self.write_count = 0
        self.read_count = 0

    def get_counters(self):
        return {"write_count": self.write_count, "read_count": self.read_count}

    def __getitem__(self, index):
        if 0 <= index < self.size:
            self.read_count += 1
            return self._list[index]
        else:
            raise IndexError("Индекс выходит за границы списка.")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            if -100 <= value <= 100:
                self._list[index] = value
                self.write_count += 1
            else:
                raise ValueError("Значение должно быть в диапазоне от -100 до 100.")
        else:
            raise IndexError("Индекс выходит за границы списка.")

    def append(self, value):
        if -100 <= value <= 100:
            self._list.append(value)
            self.size += 1
            self.write_count += 1
        else:
            raise ValueError("Значение должно быть в диапазоне от -100 до 100.")

    def display(self):
        """Выводит все значения списка."""
        print(self._list)