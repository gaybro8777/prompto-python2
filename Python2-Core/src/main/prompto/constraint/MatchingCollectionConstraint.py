from prompto.constraint.AttributeConstraint import AttributeConstraint
from prompto.error.InvalidDataError import InvalidDataError
from prompto.value.IContainer import IContainer


class MatchingCollectionConstraint ( AttributeConstraint ):

    def __init__(self, collection):
        super(MatchingCollectionConstraint, self).__init__()
        self.collection = collection

    def checkValue(self, context, value):
        container = self.collection.interpret(context)
        if isinstance(container, IContainer):
            if not container.hasItem(context, value):
                raise InvalidDataError("Value:" + str(value) + " is not in range: " + str(self.collection))
        else:
            raise InvalidDataError("Not a collection: " + self.collection.toString())

    def toDialect(self, writer):
        writer.append(" in ")
        self.collection.toDialect(writer)