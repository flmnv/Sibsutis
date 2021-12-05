import typing


class TPNumber:
    def __init__(self,
                 a: typing.Union[float, str],
                 b: typing.Union[int, str],
                 c: typing.Union[int, str]) -> None:
        pass


class TPNumber:
    def __init__(self,
                 a: typing.Union[float, str],
                 b: typing.Union[int, str],
                 c: typing.Union[int, str]) -> None:
        if isinstance(a, (str, int)):
            a: float = float(a)
        if isinstance(b, str):
            b = int(b)
        if isinstance(c, str):
            c = int(c)

        if b < 2 or b > 16:
            raise ValueError("The number b must be in the range [2; 16]")
        elif c < 0:
            raise ValueError("The number c must be >= 0")
        else:
            self.n: float = a
            self.b: int = b
            self.c: int = c

    def copy(self):
        return TPNumber(
            a=self.n,
            b=self.b,
            c=self.c)

    def __add__(self, other: TPNumber):
        if isinstance(other, TPNumber):
            if self.b == other.b and self.c == other.c:
                n = self.n + other.n

                return TPNumber(
                    a=n,
                    b=self.b,
                    c=self.c)
            else:
                raise ValueError("The values of variables b and c differ")
        else:
            raise ValueError(
                "One of the variables does not belong to the TPNumber class")

    def __mul__(self, other: TPNumber):
        if isinstance(other, TPNumber):
            if self.b == other.b and self.c == other.c:
                n: float = self.n * other.n

                return TPNumber(
                    a=n,
                    b=self.b,
                    c=self.c)
            else:
                raise ValueError("The values of variables b and c differ")
        else:
            raise ValueError(
                "One of the variables does not belong to the TPNumber class")

    def __sub__(self, other: TPNumber):
        if isinstance(other, TPNumber):
            if self.b == other.b and self.c == other.c:
                n = self.n - other.n

                return TPNumber(
                    a=n,
                    b=self.b,
                    c=self.c)
            else:
                raise ValueError("The values of variables b and c differ")
        else:
            raise ValueError(
                "One of the variables does not belong to the TPNumber class")

    def __truediv__(self, other: TPNumber):
        if isinstance(other, TPNumber):
            if self.b == other.b and self.c == other.c:
                if other.n != 0:
                    n = self.n / other.n

                    return TPNumber(
                        a=n,
                        b=self.b,
                        c=self.c)
                else:
                    raise ZeroDivisionError()
            else:
                raise ValueError("The values of variables b and c differ")
        else:
            raise ValueError(
                "One of the variables does not belong to the TPNumber class")

    def reverse(self):
        if self.n != 0:
            n = 1 / self.n

            return TPNumber(
                a=n,
                b=self.b,
                c=self.c)
        else:
            raise ZeroDivisionError()

    def sq(self):
        return TPNumber(
            a=self.n * self.n,
            b=self.b,
            c=self.c)

    def __convert(self):
        return

    def getPNum(self):
        return self.n

    def getPStr(self):
        return f"{self.n}"

    def getBaseNum(self):
        return self.b

    def getBaseStr(self):
        return str(self.b)

    def getCommaNum(self):
        return self.c

    def getCommaStr(self):
        return str(self.c)

    def setBase(self, b: typing.Union[int, str]):
        if isinstance(b, str):
            b = int(b)

        if b < 2 or b > 16:
            raise ValueError("The number b must be in the range [2; 16]")
        else:
            self.b = b

    def setComma(self, c: typing.Union[int, str]):
        if isinstance(c, str):
            c = int(c)

        if c < 0:
            raise ValueError("The number c must be >= 0")
        else:
            self.c = c


def main():
    pass


if __name__ == "__main__":
    main()
