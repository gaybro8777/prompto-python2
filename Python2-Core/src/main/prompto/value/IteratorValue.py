from prompto.type.IteratorType import IteratorType
from prompto.value.BaseValue import BaseValue
from prompto.value.IIterable import IIterable

# a light generator wrapper exposed as an IValue
class IteratorValue(BaseValue, IIterable):

    def __init__(self, itemType, value):
        super(IteratorValue, self).__init__(IteratorType(itemType))
        self.value = value

    def check(self, context):
        return self.type

    def interpret(self, context):
        return self.value

    def __str__(self):
        return str(self.value)

    def getIterator(self, context):
        return self.value