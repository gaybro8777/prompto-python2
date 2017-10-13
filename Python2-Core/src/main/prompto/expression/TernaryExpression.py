from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class TernaryExpression ( IExpression ):

    def __init__(self, condition, ifTrue, ifFalse):
        self.condition = condition
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse

    def __str__(self):
        # TODO Auto-generated method stub
        return None

    def toDialect(self, writer):
        if writer.dialect is Dialect.O:
            self.condition.toDialect(writer)
            writer.append(" ? ")
            self.ifTrue.toDialect(writer)
            writer.append(" : ")
            self.ifFalse.toDialect(writer)
        else:
            self.ifTrue.toDialect(writer)
            writer.append(" if ")
            self.condition.toDialect(writer)
            writer.append(" else ")
            self.ifFalse.toDialect(writer)

    def check(self, context):
        itype = self.condition.check(context)
        if not isinstance(itype, BooleanType):
            raise SyntaxError("Cannot test condition on " +  itype.getName() )
        trueType = self.ifTrue.check(context)
        # Type falseType = ifFalse.check(context)
        # TODO check compatibility
        return trueType

    def interpret(self, context):
        test = self.condition.interpret(context)
        if test is Boolean.TRUE:
            return self.ifTrue.interpret(context)
        else:
            return self.ifFalse.interpret(context)
