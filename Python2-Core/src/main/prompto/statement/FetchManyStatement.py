from prompto.expression.FetchManyExpression import FetchManyExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.CursorType import CursorType
from prompto.type.VoidType import VoidType


class FetchManyStatement(FetchManyExpression):

    def __init__(self, typ, predicate, first, last, orderBy, name, stmts):
        super(FetchManyStatement, self).__init__(typ,predicate, first, last, orderBy)
        self.name = name
        self.stmts = stmts


    def canReturn(self):
        return False

    def isSimple(self):
        return False


    def check(self, context):
        super(FetchManyStatement, self).check(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, CursorType(self.typ)))
        self.stmts.check(context, None)
        return VoidType.instance


    def interpret(self, context):
        record = super(FetchManyStatement, self).interpret(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, CursorType(self.typ)))
        context.setValue(self.name, record)
        self.stmts.interpret(context)
        return None


    def toDialect(self, writer):
        super(FetchManyStatement, self).toDialect(writer)
        writer.append(" then with ").append(self.name)
        if writer.dialect is Dialect.O:
            writer.append(" {")
        else:
            writer.append(":")
        writer = writer.newChildWriter()
        writer.context.registerValue(Variable(self.name, CursorType(self.typ)))
        writer.newLine().indent()
        self.stmts.toDialect(writer)
        writer.dedent()
        if writer.dialect is Dialect.O:
            writer.append("}")

