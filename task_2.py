# Две реализации буфера FIFO

# В первой реализации более быстрое добавление элемента,
# т.к. элемент добавляется в конец, и программе не нужно каждый раз пересчитывать список.
# Минус - более медленное удаление элемента, 
# т.к. удаляется первый элемент списка, соответственно все другие элемента сдвигаются.
class Queue:
    """Class of queue."""
    def __init__(self) -> None:
        self.queue: list = []

    def append(self, value) -> None:
        self.queue.append(value)

    def get_element(self) -> any:
        if self.empty_queue():
            return 'Queue is empty.'
        return self.queue.pop(0)

    def empty_queue(self) -> bool:
        if not self.size():
            return True
        return False

    def size(self) -> int:
        return len(self.queue)


# Во второй реализации все строго наоборот,
# Медленнное добавление элементов т.к. элемент добавляется в начало, 
# и нужно смещать все другие элементы списка.
# Более быстрое удаление элемента, 
# т.к. удаляется последний элемент.
class Queue_2:
    """Class of queue too."""
    def __init__(self) -> None:
        self.queue: list = []

    def append(self, value) -> None:
        self.queue.insert(0, value)

    def get_element(self) -> any:
        if self.empty_queue():
            return 'Queue is empty.'
        return self.queue.pop()
    
    def empty_queue(self) -> bool:
        if not self.size():
            return True
        return False

    def size(self) -> int:
        return len(self.queue)
