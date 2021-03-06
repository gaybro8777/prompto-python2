from prompto.error.ExecutionError import ExecutionError
from prompto.literal.TextLiteral import TextLiteral


class InvalidValueError(ExecutionError):

    def __init__(self, message):
        super(InvalidValueError, self).__init__(message)

    def getExpression(self, context):
        s = self.message.replace('"',"'") # ensure TextLiteral interprets the full string
        return TextLiteral('"' + s + '"')
