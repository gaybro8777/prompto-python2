from io import StringIO
from prompto.literal.Literal import Literal
from prompto.type.TupleType import TupleType
from prompto.value.BaseValueList import BaseValueList

class TupleValue ( BaseValueList ):

    def __init__(self, items=None, item = None):
        super(TupleValue, self).__init__(TupleType(), items)
        if item is not None:
            self.items.append(item)

    def newInstance(self, items):
        return TupleValue(items)

    def Add(self, context, value):
        if isinstance(value, BaseValueList):
            return self.merge(value)
        else:
            raise SyntaxError("Illegal: Tuple + " + type(value).__name__)

    def __str__(self):
        with StringIO() as sb:
            sb.write(u"(")
            for v in self.items:
                sb.write(unicode(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len-2)
                sb.truncate(len-2)
            sb.write(u")")
            return sb.getvalue()

    def toDialect(self, writer):
        writer.append('(')
        if self.size()>0:
            for o in self.items:
                if isinstance(o, Literal):
                    o.toDialect(writer)
                else:
                    writer.append(str(o))
                writer.append(", ")
            writer.trimLast(2)
        writer.append(')')

    def __hash__(self):
        return hash(frozenset(self.items))

    def filter(self, context, itemName, filter):
        result = TupleValue()
        for o in self.getIterator(context):
            context.setValue(itemName, o)
            test = filter.interpret(context)
            from prompto.value.Boolean import Boolean
            if not isinstance(test, Boolean):
                raise InternalError("Illegal test result: " + test)
            if test.getValue():
                result.append(o)
        return result
