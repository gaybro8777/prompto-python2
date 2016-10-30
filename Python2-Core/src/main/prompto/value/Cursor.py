from prompto.value.BaseValue import BaseValue
from prompto.type.CursorType import CursorType
from prompto.value.IIterable import IIterable
from prompto.value.Integer import Integer
from prompto.error.InvalidDataError import InvalidDataError

class Cursor(BaseValue, IIterable):

    def __init__(self, context, itemType, stored):
        super(Cursor, self).__init__(CursorType(itemType))
        self.context = context
        self.stored = stored

    def isEmpty(self):
        return len(self.stored)==0

    def __len__(self):
        return len(self.stored)

    def getIterator(self, context):
        for stored in self.stored:
            val = self.type.itemType.newInstanceFromStored(context, stored)
            yield val

    def getMember(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self))
        else:
            raise InvalidDataError("No such member:" + name)


