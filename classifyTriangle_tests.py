import unittest
from classifyTriangle import classifyTriangle
from math import sqrt

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(1,1,1), "equilateral triangle")
        self.assertEqual(classifyTriangle("3.1415928","3.1415928","3.1415928"), "equilateral triangle")
        self.assertEqual(classifyTriangle(-0.1,-0.1,-0.1), "equilateral triangle")
        self.assertEqual(classifyTriangle(0,0,0), "equilateral triangle")

    def test_isosceles(self):
        self.assertEqual(classifyTriangle(1,1,3), "isosceles triangle")
        self.assertEqual(classifyTriangle("1.1415928","3.1415928","3.1415928"), "isosceles triangle")
        self.assertEqual(classifyTriangle(-0.1,-0.6,-0.1), "isosceles triangle")
        self.assertEqual(classifyTriangle(0.0000001,0,0), "isosceles triangle")

    def test_right_isosceles(self):
        v1 = 1
        v2 = 3.1415928
        v3 = -0.1
        self.assertEqual(classifyTriangle(v1,v1,sqrt(2*v1**2)), "right isosceles triangle")
        self.assertEqual(classifyTriangle(str(sqrt(2*v2**2)),str(v2),str(v2)), "right isosceles triangle")
        self.assertEqual(classifyTriangle(v3,sqrt(2*v3**2),v3), "right isosceles triangle")

    def test_scalene(self):
        self.assertEqual(classifyTriangle(1,2,3), "scalene triangle")
        self.assertEqual(classifyTriangle("1.1415928","3.1415928","2.1415928"), "scalene triangle")
        self.assertEqual(classifyTriangle(-0.6,-0.4,-0.1), "scalene triangle")
        self.assertEqual(classifyTriangle(0.0000001,0,-0.0000002), "scalene triangle")

    def test_right_scalene(self):
        v11 = 1
        v12 = 2
        v21 = 3.1415928
        v22 = 2.1415928
        v31 = -0.1
        v32 = -0.2
        self.assertEqual(classifyTriangle(v11,v12,sqrt(v11**2+v12**2)), "right scalene triangle")
        self.assertEqual(classifyTriangle(str(sqrt(v21**2+v22**2)),str(v21),str(v22)), "right scalene triangle")
        self.assertEqual(classifyTriangle(v31,sqrt(v31**2+v32**2),v32), "right scalene triangle")

if __name__ == '__main__':
    unittest.main()