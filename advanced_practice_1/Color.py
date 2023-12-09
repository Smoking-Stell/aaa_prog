from abc import ABC


class ComputerColor(ABC):
    def __repr__(self):
        pass

    def __mul__(self, other: float):
        pass

    def __rmul__(self, other: float):
        pass


class Color(ComputerColor):
    START = '\033[1;38;2'
    END = '\033[0'
    MOD = 'm'
    BARIER = 255

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def _init_limited(cls, red, green, blue):
        return cls(min(int(red), cls.BARIER), min(int(green), cls.BARIER),
                   min(int(blue), cls.BARIER))

    def __str__(self):
        return f'{self.START};{self.r};{self.g};{self.b}' \
               f'{self.MOD}◆{self.END}{self.MOD}'

    def __repr__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b})"

    def rgb(self):
        return (self.r, self.g, self.b)

    def __eq__(self, other):
        if not isinstance(other, Color):
            return False
        return self.rgb() == other.rgb()

    def __hash__(self):
        return hash(self.rgb())

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError("we need two colors")

        ans = Color._init_limited(self.r + other.r,
                                  self.g + other.g,
                                  self.b + other.b)

        return ans

    def __mul__(self, other):
        if not isinstance(other, float):
            raise TypeError("we need color and float")

        if other < 0 or other > 1:
            raise RuntimeError("can be sharnk only by value >0 and <1")

        cl = -256 * (1 - other)
        coef = (259 * (cl + 255)) / (255 * (259 - cl))

        new_colors = map(lambda color: coef * (color - 128) + 128, self.rgb())

        return Color._init_limited(*new_colors)

    def __rmul__(self, other):
        return self.__mul__(other)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))



def main():
    red = Color(255, 10, 10)
    red2 = Color(255, 10, 10)
    green = Color(10, 250, 10)
    orange = Color(255, 166, 0)
    violet = Color(75, 0, 130)
    violet2 = Color(75, 0, 130)
    print(red)
    print(red == red2)
    print(red == green)

    print(red + green)
    print(red + violet)

    print(set([red, red2, orange, violet, violet2]))

    print(red * 0.9)
    print(0.5 * red)

    print_a(red)


if __name__ == '__main__':
    main()
