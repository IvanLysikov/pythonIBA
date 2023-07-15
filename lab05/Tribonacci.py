class Tribonacci:
    def __init__(self):
        self.a, self.b, self.c = 0, 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 35:
            if self.count == 0 or self.count == 1:
                self.count += 1
                return 0
            elif self.count == 2:
                self.count += 1
                return 1
            else:
                result = self.a + self.b + self.c
                self.a, self.b, self.c = self.b, self.c, result
            self.count += 1
            return result
        else:
            raise StopIteration


tribonacci_sequence = Tribonacci()

for number in tribonacci_sequence:
    print(number)
