from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.error.SyntaxError import SyntaxError

class NativeCategoryDeclaration(CategoryDeclaration):

    def __init__(self, name, attributes, categoryBindings, attributebindings):
        super(NativeCategoryDeclaration, self).__init__(name, attributes)
        self.categoryBindings = categoryBindings
        self.attributebindings = attributebindings
        self.boundedClass = None

    def __str__(self):
        return self.getName() + (":" + str(self.attributes)) if self.attributes is not None else ""

    def register(self, context):
        context.registerDeclaration(self)
        bounded = self.getBoundedClass(False)
        if bounded is not None:
            context.registerNativeBinding(bounded, self)

    def newInstance(self):
        from presto.value.NativeInstance import NativeInstance
        return NativeInstance(self)

    def getBoundedClass(self, fail):
        if self.boundedClass is None:
            binding = self.getBinding(fail)
            if binding is not None:
                self.boundedClass = binding.interpret()
                if fail and self.boundedClass is None:
                    raise SyntaxError("No Python class:" + str(binding))
        return self.boundedClass

    def getBinding(self, fail):
        for binding in self.categoryBindings:
            from presto.python.PythonNativeCategoryBinding import Python2NativeCategoryBinding
            if isinstance(binding, Python2NativeCategoryBinding):
                return binding
        if fail:
            raise SyntaxError("Missing PYTHON2 binding !")
        else:
            return None

    def toEDialect(self, writer):
        self.protoToEDialect(writer, False, True)
        self.bindingsToEDialect(writer)


    def categoryTypeToEDialect(self, writer):
        writer.append("native category")

    def bindingsToEDialect(self, writer):
        writer.indent()
        self.categoryBindings.toDialect(writer)
        writer.dedent()
        writer.newLine()

    def toODialect(self, writer):
        self.allToODialect(writer, True) # always has body;

    def categoryTypeToODialect(self, writer):
        writer.append("native category")

    def bodyToODialect(self, writer):
        self.categoryBindings.toDialect(writer)

    def toPDialect(self, writer):
        self.protoToPDialect(writer, None)
        writer.indent()
        writer.newLine()
        self.categoryBindings.toDialect(writer)
        writer.dedent()
        writer.newLine()

    def categoryTypeToPDialect(self, writer):
        writer.append("native category")
