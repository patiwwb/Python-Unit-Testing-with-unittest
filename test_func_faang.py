import  unittest 
from unittest import mock, TestCase
import facebook, google, data

class TestApi(TestCase):

    """
    def test_external_api(self):
        self.assertEqual(google.call_google_api(), 'data_1')
        self.assertEqual(facebook.call_facebook_api(), 'data_1')
    """   
    
    
    """
    #to skip some tests 
    @mock.patch('facebook.get_data', return_value='data_3')
    @mock.patch('google.get_data', return_value='data_2')
    def test_external_api(self,googl,fb):
            self.assertEqual(google.call_google_api(), 'data_2')
            self.assertEqual(facebook.call_facebook_api(), 'data_3')
    """
    
    
    """
    def test_external_api(self):
        with mock.patch('google.get_data', return_value = 'data_2'):
            self.assertEqual(google.call_google_api(), 'data_2')
    """       
    
    def test_external_api(self):
        with mock.patch('google.get_data') as mocked_get:
            mocked_get.return_value= 'data_2'
            google_data = google.call_google_api()
            self.assertEqual(google_data, 'data_2')
            
            
if __name__ == '__main__':
    unittest.main()
