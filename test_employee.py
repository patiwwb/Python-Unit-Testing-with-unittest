import unittest
from unittest.mock import patch
from employee import Employee
import sys

class TestEmployee(unittest.TestCase):

    a = 1 
    b = 2 

    """setUpClass run once at the beginning of all tests"""
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    """tearDownClass run once at the end of all tests"""
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    """setUp run before every test"""
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    """tearDown run after every test """
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

    """we can skip a test"""
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(b>a, "Skip over this routine")
    def test_1(self):
        print('test_1')
        self.assertTrue(self.emp_1.pay == 50000)
    
    @unittest.skipUnless(b == 0, "Skip over this routine")
    def test_2(self):
      print('test_2')
      result = self.emp_1.pay
      self.assertTrue(result == 50000)
      
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        print('test_windows')
        # windows specific testing code
        pass
    
    @unittest.expectedFailure
    def test_3(self):
      print('test_3')
      result = 1*2
      self.assertEqual(1, 0, "broken")
    
if __name__ == '__main__':
    #unittest.main()
    unittest.main(verbosity=2)