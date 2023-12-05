class Color():
    START = '\033[1;38;2'
    END = '\033[0'
    MOD = 'm'


    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'{self.START};{self.r};{self.g};{self.b}' \
               f'{self.MOD}◆{self.END}{self.MOD}'

    def __eq__(self, other):
        if not isinstance(other, Color):
            return False
        return self.r == other.r and self.g == other.g and self.b == other.b

def main():
    red = Color(255, 10, 10)
    red2 = Color(255, 10, 10)
    green = Color(10, 250, 10)
    print(red)
    print(red == red2)
    print(red == green)


if __name__ == '__main__':
    main()