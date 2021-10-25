import unittest
import mainfile as m
class TestingMainfile(unittest.TestCase):

    def setUp(self):
        self.testingObj = m.MainFileCode()

    def test_isPrime(self):
        self.assertTrue(self.testingObj.isPrime(7)[0])
        self.assertFalse(self.testingObj.isPrime(4)[0])
        self.assertEqual(self.testingObj.isPrime(7)[1],'Prime')
        self.assertEqual(self.testingObj.isPrime(4)[1],'Prime')

    def test_isPalindrome(self):
        self.assertTrue(self.testingObj.isPalindrome('ara')[0])
        self.assertFalse(self.testingObj.isPalindrome('arunav')[0])
        self.assertEqual(self.testingObj.isPalindrome('ara')[1],'Palin')
        self.assertEqual(self.testingObj.isPalindrome('arunav')[1],'Palin')

    def test_isDecide(self):
        self.assertEqual(self.testingObj.isDecide('ara'),(True,'Palin'))
        self.assertEqual(self.testingObj.isDecide('arunav'),(False,'Palin'))
        self.assertEqual(self.testingObj.isDecide('7'),(True,'Prime'))
        self.assertEqual(self.testingObj.isDecide('8'),(False,'Prime'))

if __name__ == '__main__':
    unittest.main()