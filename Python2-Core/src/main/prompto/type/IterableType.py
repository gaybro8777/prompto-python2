from prompto.type.NativeType import NativeType


class IterableType ( NativeType ) :

    def __init__(self, family, itemType):
        super(IterableType, self).__init__(family)
        self.itemType = itemType

    def getItemType(self):
        return self.itemType

    def checkExists(self, context):
        self.itemType.checkExists(context)

    def isMoreSpecificThan(self, context, other):
        return isinstance(other, IterableType) and \
            self.itemType.isMoreSpecificThan(context, other.itemType)
