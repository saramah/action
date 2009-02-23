from action.tests import *

class TestTaskController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='task'))
        # Test response...
