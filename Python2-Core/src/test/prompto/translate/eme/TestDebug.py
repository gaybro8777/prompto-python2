from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDebug(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testStack(self):
        self.compareResourceEME("debug/stack.pec")

    def testVariables(self):
        self.compareResourceEME("debug/variables.pec")


