from prompto.type.BaseType import BaseType
from prompto.type.TypeFamily import TypeFamily



class NullType(BaseType):

    instance = None

    def __init__(self):
        super(NullType, self).__init__(TypeFamily.NULL)

    def isAssignableTo (self, context,  other):
        return True

    def isMoreSpecificThan (self, context, other):
        return False

NullType.instance = NullType()
