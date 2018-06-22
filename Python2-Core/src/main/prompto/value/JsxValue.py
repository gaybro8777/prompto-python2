from prompto.value.BaseValue import BaseValue
from prompto.type.JsxType import JsxType


class JsxValue(BaseValue):

	def __init__(self, expression):
		super(JsxValue, self).__init__(JsxType.instance)
		self.expression = expression
