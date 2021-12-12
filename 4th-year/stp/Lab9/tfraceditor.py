from tfrac import TFrac


class TFracEditorException:
    pass


class TFracEditor:
    def __init__(self, tfrac: TFrac) -> None:
        self.tfrac = tfrac

    def isZero(self):
        if self.tfrac.a == 0:
            return True
        else:
            return False

    def changeSign(self):
        self.tfrac.sign()
        self.tfrac.a *= -1

        return self.tfrac

    def addNumber(self, number: int):
        other_tfrac = TFrac(number)
        self.tfrac += other_tfrac

        return self.tfrac

    def addZero(self):
        tfrac_str: str = self.tfrac.getStr()
        tfrac_str += '0'

        new_tfrac = TFrac(tfrac_str)
        self.tfrac = new_tfrac

        return self.tfrac

    def removeChar(self):
        tfrac_str: str = self.tfrac.getStr()

        if len(tfrac_str) > 1 and tfrac_str[-1] != '/':
            tfrac_str = tfrac_str[:-1]
        else:
            tfrac_str = '0'

        new_tfrac = TFrac(tfrac_str)
        self.tfrac = new_tfrac

        return self.tfrac

    def clear(self):
        self.tfrac.a = 0
        self.tfrac.b = 1

        return self.tfrac

    def setTFracStr(self, tfrac_str: str):
        self.tfrac = TFrac(tfrac_str)
        return self.tfrac
    
    def getTFracStr(self):
        return self.tfrac.getStr()