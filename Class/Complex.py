class Complex:
    def __init__(self, re=None, im=None) -> object:
        if re is None:
            self.re = 0
        else:
            self.re = re

        if im is None:
            self.im = 0
        else:
            self.im = im

    def __str__(self):
        re = self.re
        im = self.im

        if 0 <= float(im):
            return f"{re} + {im}i"
        else:
            return f"{re} - {-im}i"

    def __sub__(self, other):
        toRet = Complex(0, 0)
        toRet.re = self.re - other.re
        toRet.im = self.im - other.im
        return toRet

    def __add__(self, other):
        toRet = Complex(0, 0)
        toRet.re = self.re + other.re
        toRet.im = self.im + other.im
        return toRet

    def __mul__(self, other):
        a = self
        b = other
        toRet = Complex(0, 0)
        toRet.re = a.re * b.re - a.im * b.im
        toRet.im = a.re * b.im + a.im * b.re
        return toRet

    def __truediv__(self, other):
        toRet = Complex(0, 0)
        a = self
        b = other
        if other.re == 0 & other.im == 0:
            raise Exception("Don't divide by 0")
        deno = b.re * b.re + b.im * b.im
        toRet.re = (a.re * b.re + a.im * b.im) / deno
        toRet.im = (a.im * b.re - a.re * b.im) / deno
        return toRet

    def __floordiv__(self, other):
        toRet = Complex(0, 0)
        a = self
        b = other
        if other.re == 0 & other.im == 0:
            raise Exception("Don't divide by 0")
        deno = b.re * b.re + b.im * b.im
        toRet.re = int((a.re * b.re + a.im * b.im) / deno)
        toRet.im = int((a.im * b.re - a.re * b.im) / deno)
        return toRet
