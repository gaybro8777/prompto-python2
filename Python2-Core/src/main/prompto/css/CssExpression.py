from prompto.expression.IExpression import IExpression
from prompto.type.CssType import CssType
from prompto.value.CssValue import CssValue


class CssExpression(IExpression):

    def __init__(self):
        self.fields = []

    def check(self, context):
        return CssType.instance


    def interpret(self, context):
        return CssValue(self)


    def toDialect(self, writer):
        writer.append("{")
        [ field.toDialect(writer) for field in self.fields ]
        writer.append("}")


    def addField(self, field):
        self.fields.append(field)
