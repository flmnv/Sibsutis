import typing
import math


class TComplex:
    def __init__(self) -> None:
        self.a: float
        self.b: float


class TComplex:
    def __init__(self, a: typing.Union[int, float, str], b: typing.Union[int, float] = None) -> None:
        if isinstance(a, (int, float)):
            self.a: float = float(a)

            if b is None:
                self.b: float = 0.0
            elif isinstance(b, (int, float)):
                self.b: float = float(b)
            else:
                raise ValueError
        elif isinstance(a, str) and b is None:
            ab = a.replace(" ", "")

            if "+" in ab:
                ab = ab.split("+")
            elif "-" in ab:
                ab = ab.split("-")
            else:
                raise ValueError

            if len(ab) == 2 and ab[1].startswith("i*"):
                self.a: float = float(ab[0])
                ab[1] = ab[1].replace("i*", "")
                self.b: float = float(ab[1])
            else:
                raise ValueError
        else:
            raise ValueError

    
    # copy
    def copy(self):
        copy: TComplex = TComplex(self.a, self.b)
        return copy


    # add function
    def add(self, other: TComplex):
        if isinstance(other, TComplex):
            a: float = self.a + other.a
            b: float = self.b + other.b

            return TComplex(a, b)
        else:
            raise ValueError

    
    # add
    def __add__(self, other: TComplex):
        if isinstance(other, TComplex):
            a: float = self.a + other.a
            b: float = self.b + other.b
            
            return TComplex(a, b)
        else:
            raise ValueError


    # multiply
    def __mul__(self, other: TComplex):
        if isinstance(other, TComplex):
            a: float = self.a * other.a - self.b * other.b
            b: float = self.a * other.b + self.b * other.a
            return TComplex(a, b)
        else:
            raise ValueError

    
    # squaring
    def sq(self):
        a: float = self.a * self.a - self.b * self.b
        b: float = self.a * self.b + self.a * self.b

        return TComplex(a, b)


    # inverse number
    def inverse(self):
        a: float = self.a / (self.a ** 2 + self.b ** 2)
        b: float = - self.b / (self.a ** 2 + self.b ** 2)

        return TComplex(a, b)


    # subtraction function
    def sub(self, other: TComplex):
        if isinstance(other, TComplex):
            a: float = self.a - other.a
            b: float = self.b - other.b

            return TComplex(a, b)
        else:
            raise NotImplementedError


    # subtraction
    def __sub__(self, other: TComplex):
        if isinstance(other, TComplex):
            a = self.a - other.a
            b = self.b - other.b

            return TComplex(a, b)
        else:
            raise NotImplementedError


    # division
    def __truediv__(self, other: TComplex):
        if isinstance(other, TComplex):
            a: float = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
            b: float = (other.a * self.b - self.a * other.b) / (other.a ** 2 + other.b ** 2)

            return TComplex(a, b)
        else:
            raise NotImplementedError


    # the number module
    def module(self):
        return (self.a * self.a + self.b * self.b) ** 0.5


    # returns the argument fi in radians
    def radian(self):
        fi: float = 0

        if self.a > 0:
            fi = math.atan(self.b / self.a)
        elif self.a == 0 and self.b > 0:
            fi = math.pi/2
        elif self.a == 0 and self.b < 0: 
            fi = -math.pi/2
        elif self.a < 0:
            fi = math.atan(self.b / self.a) + math.pi

        return fi


    # returns the argument fi in degrees
    def degrees(self):
        return self.radian() * 180 / math.pi


    # exponentiation
    def pow(self, n: int):
        a: float = (self.module() ** n) * math.cos(n * self.radian())
        b: float = (self.module() ** n) * math.sin(n * self.radian())

        return TComplex(a, b)


    # the root of the number
    def root(self, n: int):
        a: float = (self.module() ** (1/n)) * math.cos((self.radian() + 2 * n * math.pi) / n)
        b: float = (self.module() ** (1/n)) * math.sin((self.radian() + 2 * n * math.pi) / n)

        return TComplex(a, b)


    # equal
    def __eq__(self, other: TComplex):
        if isinstance(other, TComplex):
            if self.a == other.a and self.b == other.b:
                return True


    # not equal
    def __ne__(self, other: TComplex):
        if isinstance(other, TComplex):
            if self.a != other.a or self.b != other.b:
                return True


    # get real as float
    def getRealNum(self):
        return self.a


    # get imaginary as float
    def getImNum(self):
        return self.b


    # get real as string
    def getRealStr(self):
        return str(self.a)


    # get imaginary as string
    def getImStr(self):
        return str(self.b)


    # get complex number as string
    def getComplexStr(self):
        if self.b >= 0:
            return f"{self.a}+i*{self.b}"
        else:
            return f"{self.a}-i*{self.b * -1}"


def main():
    pass


if __name__ == "__main__":
    main()
