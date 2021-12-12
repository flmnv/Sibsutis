import typing


class TFrac():
    def __init__(self) -> None:
        self.a: int
        self.b: int
        
    def short(): pass
    def sign(): pass
    def print(): pass


class TFrac():
    # initialization
    def __init__(self, a_or_f: typing.Union[int, str], b: int = None) -> None:
        if a_or_f is not None:
            if type(a_or_f) is int:
                self.a: int = a_or_f

                if b is None:
                    self.b: int = 1
                else:
                    if type(b) is not int:
                        raise ValueError

                    self.b: int = b
            elif type(a_or_f) is str and b is None:
                ab = a_or_f.split("/")
                if len(ab) == 1 and ab[0].isdigit():
                    self.a: int = int(ab[0])
                    self.b: int = 1
                elif len(ab) == 2:
                    self.a: int = int(ab[0])
                    self.b: int = int(ab[1])
            else:
                raise ValueError
        else:
            raise ValueError

        if self.b == 0:
            raise ZeroDivisionError

        if self.a != 0:
            self.short()
        else:
            self.sign()


    # copy
    def copy(self, other: TFrac):
        self.a = other.a
        self.b = other.b


    # add
    def __add__(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.b + other.a * self.b
            b = self.b * other.b
            return TFrac(a, b)
        if isinstance(other, int):
            a = self.a + other * self.b
            b = self.b
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # multiply
    def __mul__(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.a
            b = self.b * other.b
            return TFrac(a, b)
        elif isinstance(other, int):
            a = self.a * other
            b = self.b
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # subtraction
    def __sub__(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.b - other.a * self.b
            b = self.b * other.b
            return TFrac(a, b)
        if isinstance(other, int):
            a = self.a - other * self.b
            b = self.b
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # true division
    def __truediv__(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.b
            b = other.a * self.b
            return TFrac(a, b)
        elif isinstance(other, int):
            a = self.a
            b = self.b * other
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # exponentiation
    def __pow__(self, other) -> TFrac:
        tf_pow = TFrac(self.a, self.b)

        for i in range(other - 1):
            tf_pow *= tf_pow

        return tf_pow


    # reverse true division
    def __rtruediv__(self, other: int) -> TFrac:
        if isinstance(other, int):
            return TFrac(other) / self


    # equate
    def __eq__(self, other: TFrac) -> bool:
        temp_self = self
        temp_other = other

        temp_self.short()
        temp_other.short()

        if temp_self.a == temp_other.a and temp_self.b == temp_other.b:
            return True
        else:
            return False

    
    # great
    def __gt__(self, other: TFrac) -> bool:
        temp_self = self
        temp_other = other

        temp_self.short()
        temp_other.short()

        if temp_self.a * temp_other.b > temp_other.a * temp_self.b:
            return True
        else:
            return False


    # add function
    def add(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.b + other.a * self.b
            b = self.b * other.b
            return TFrac(a, b)
        if isinstance(other, int):
            a = self.a + other * self.b
            b = self.b
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # subtraction function
    def sub(self, other: typing.Union[TFrac, int]):
        if isinstance(other, TFrac):
            a = self.a * other.b - other.a * self.b
            b = self.b * other.b
            return TFrac(a, b)
        if isinstance(other, int):
            a = self.a - other * self.b
            b = self.b
            return TFrac(a, b)
        else:
            raise NotImplementedError


    # get numerator as number
    def getNumeratorNum(self):
        return self.a


    # get denomerator as number
    def getDenomiratorNum(self):
        return self.b

    
    # get numerator as string
    def getNumeratorStr(self):
        return str(self.a)


    # get denomerator as string
    def getDenomiratorStr(self):
        return str(self.b)


    # get as string
    def getStr(self):
        return f"{self.a}/{self.b}"


    # short num - euclidean algorithm
    def short(self):
        if self.a > self.b:
            a = self.a
            b = self.b
        else:
            a = self.b
            b = self.a

        while a % b != 0:
            temp_b: int = b
            b = a % b
            a = temp_b

        self.a //= b
        self.b //= b

        self.sign()


    # short sign
    def sign(self):
        if self.b < 0:
            self.a *= -1
            self.b *= -1


    # print
    def print(self):
        if self.b != 1:
            print(f"{self.a}/{self.b}")
        else:
            print(f"{self.a}")


if __name__ == "__main__":
    pass
