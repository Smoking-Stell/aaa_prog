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

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError("we need two colors")

        new_red = min(self.r + other.r, 255)
        new_green = min(self.g + other.g, 255)
        new_blue = min(self.b + other.b, 255)

        ans = Color(new_red, new_green, new_blue)
        return ans


def main():
    red = Color(255, 10, 10)
    red2 = Color(255, 10, 10)
    green = Color(10, 250, 10)
    print(red)
    print(red == red2)
    print(red == green)

    print(red + green)


if __name__ == '__main__':
    main()
