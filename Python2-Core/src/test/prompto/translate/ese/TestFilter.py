from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestFilter(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFilterFromList(self):
        self.compareResourceESE("filter/filterFromList.pec")

    def testFilterFromSet(self):
        self.compareResourceESE("filter/filterFromSet.pec")

