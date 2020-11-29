
import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
       
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
self.new_article = Article('1','psychology','Utpal Dholakia Ph.D.','Why Are American Shoppers Panic Buying Again?','We have seen this show already once this year, in full CinemaScope no less.','https://www.psychologytoday.com/us/blog/the-science-behind-behavior/202011/why-are-american-shoppers-panic-buying-again?collection=1154000','https://www.google.com/search?q=image&sxsrf=ALeKk01P-gWnceJCIGUwCBCnXsUBt0OW9g:1606659598829&tbm=isch&source=iu&ictx=1&fir=3z9LIUs4ChzUOM%252ChrsXnpNgc3ZwMM%252C_&vet=1&usg=AI4_-kTte39BqlR0dNxrY4KNIZ22wyiq5A&sa=X&ved=2ahUKEwjX3aa1-aftAhV9RxUIHZDoBuMQ9QF6BAgCEFo#imgrc=3z9LIUs4ChzUOM','www.lo.ketsia.jpg')

if __name__ == '__main__':
    unittest.main()