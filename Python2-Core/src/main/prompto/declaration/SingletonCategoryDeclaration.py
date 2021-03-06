from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration

class SingletonCategoryDeclaration(ConcreteCategoryDeclaration):

    def __init__(self, name, attributes, methods):
        super(SingletonCategoryDeclaration, self).__init__(name, attributes)
        self.setMethods(methods)

    def categoryTypeToEDialect(self, writer):
        writer.append("singleton")

    def categoryTypeToODialect(self, writer):
        writer.append("singleton")

    def categoryTypeToMDialect(self, writer):
        writer.append("singleton")
