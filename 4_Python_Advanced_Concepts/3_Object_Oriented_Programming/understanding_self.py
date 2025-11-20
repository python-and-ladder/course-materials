class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        """self refers to the current instance"""
        self.count += 1
        return self.count

    def reset(self):
        old_count = self.count
        self.count = 0
        return old_count

# self is automatically passed when calling methods
counter1 = Counter()
counter2 = Counter()

print(counter1.increment())  # 1 - counter1 is passed as self
print(counter1.increment())  # 2 - counter1 is passed as self
print(counter2.increment())  # 1 - counter2 is passed as self
