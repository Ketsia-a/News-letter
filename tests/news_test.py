import unittest
from app.models import News

class NewsTest(unittest.TestCase):
        
    '''
    Test class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("one","Abraham","THe dollar bill currency", "","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()