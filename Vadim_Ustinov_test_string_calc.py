import unittest
from unittest.mock import patch, mock_open
import string_calc

class Test_string_calc(unittest.TestCase):
    def test_mul(self):
           self.assertEqual(string_calc.mul(25,5),125)
           self.assertEqual(string_calc.mul(25,0),0)
    def test_div(self):
           self.assertEqual(string_calc.div(25,5),5)
           self.assertEqual(string_calc.div(25,0.1),250)
           self.assertRaises(Exception, string_calc.div, 0, 0)
    def test_sum(self):
           self.assertEqual(string_calc.sum(25,5),30)
           self.assertEqual(string_calc.sum(-5,5),0)
    def test_sub(self):
           self.assertEqual(string_calc.sub(25,5),20)
           self.assertEqual(string_calc.sub(-5,5),-10)
    def test_divmod(self):
           self.assertEqual(string_calc.divmod(25,4),6)
           self.assertEqual(string_calc.divmod(-5,5),-1)
    def test_divrem(self):
           self.assertEqual(string_calc.divrem(25,5),0)
           self.assertEqual(string_calc.divrem(24,5),4)
    def test_pow(self):
           self.assertEqual(string_calc.pow(25,2),625)
           self.assertEqual(string_calc.pow(2,8),256)
    def test_parse_formula(self):
           self.assertEqual(string_calc.parse_formula("2+4*5"),["2", "+", "4", "*", "5"])
    def test_validate_expression(self):
           self.assertEqual(string_calc.validate_expression(["2", "+", "4", "*", "5"]),[2, "+", 4, "*", 5])
    def test_evaluate_expression(self):
           self.assertEqual( string_calc.evaluate_expression( [2, "+", 4, "*", 5] ),22) 

    def test_load_logfiles(self):
            with patch('os.path.isfile') as mocked_isfile:
                mocked_isfile.return_value = False
                self.assertEqual(string_calc.load_log_file("/var/log/messages"), [])
            with patch('builtins.open', mock_open(read_data="Sample Log")) as mocked_log:
                self.assertEqual(string_calc.load_log_file('/var/log/messages'), ['Sample Log'])

           

if __name__ == "__main__":
    unittest.main()