# Property assim como encapsulamento é uma convenção, uma forma de trabalhar com a variavel de forma indireta

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property   # x definido como propriedade
    def x(self):
        return self._x or 0

    @x.setter   # setter de x para modificar de forma indireta a variavel
    def x(self, value):
        self._x += value

    @x.deleter  # deleter para x caso seja necessário zerar a property
    def x(self):
        self._x = 0

#   Uma vantagem de usar property é gerar segurança para a variável original, de forma que tenha que passar primeiro pelas property para alteração

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)