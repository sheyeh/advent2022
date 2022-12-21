class Monkey:
    def __init__(self, number, queue, operation, test):
        self.inspections = 0
        self.number = number
        self.queue = queue
        self.operation = operation
        self.test = test
        self.if_true = None
        self.if_false = None

    def set_if_true(self, if_true):
        self.if_true = if_true

    def set_if_false(self, if_false):
        self.if_false = if_false

    def process(self):
        while self.queue:
            self.inspections += 1
            item_value = self.queue.pop(0)
            new_item_value = int(self.operation.next_value(item_value) / 3)
            next_monkey = self.if_false if new_item_value % self.test else self.if_true
            next_monkey.queue.append(new_item_value)


class Operation:
    def __init__(self, text: str):
        if text == "* old":
            self.power = True
        else:
            self.power = False
            self.add_or_multiply = text.startswith("+")
            self.value = int(text[1:])

    def next_value(self, value):
        if self.power:
            return value * value
        elif self.add_or_multiply:
            return value + self.value
        else:
            return value * self.value
