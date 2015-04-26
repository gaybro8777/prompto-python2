from presto.grammar.IDialectElement import IDialectElement
from presto.utils.ObjectList import ObjectList


class NativeCategoryBindingList ( ObjectList, IDialectElement ):

    def __init__(self, binding = None):
        super(NativeCategoryBindingList, self).__init__()
        if binding is not None:
            self.append(binding)

    def toSDialect(self, writer):
        writer.append("def category bindings:\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.newLine()
        writer.dedent()

    def toODialect(self, writer):
        writer.append("category bindings {\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.append(';')
            writer.newLine()
        writer.dedent()
        writer.append("}")

    def toEDialect(self, writer):
        writer.append("define category bindings as:\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.newLine()
        writer.dedent()

