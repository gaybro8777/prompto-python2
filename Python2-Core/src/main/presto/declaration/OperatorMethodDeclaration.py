from presto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from presto.grammar.ArgumentList import ArgumentList
from presto.expression.IExpression import IExpression
from presto.type.VoidType import VoidType

class OperatorMethodDeclaration(ConcreteMethodDeclaration, IExpression):

    def __init__(self, operator, arg, returnType, stmts):
        super(OperatorMethodDeclaration, self).__init__("operator_" + operator.name, ArgumentList(arg), returnType, stmts)
        self.operator = operator

    def checkMember(self, declaration, context):
        # TODO Auto-generated method stub
        pass

    def toSDialect(self, writer):
        writer.append("def operator ")
        writer.append(self.operator.token)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.operator.token)
        writer.append(" as: operator ")
        self.arguments.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning: ")
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("operator ")
        writer.append(self.operator.token)
        writer.append(" (")
        self.arguments.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")
