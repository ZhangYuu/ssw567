# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: there may be a bug or two in this code
        
    """
    # require that the input values be > 0 and <= 200    #BUG
    if a > 200 and b > 200 or c > 200:
        return 'InvalidInput'
        
    #if a <= 0 or b <= b or c <= 0:   BUG
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    
    #!!!! This should be checked first. 
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
        
    #if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):    BUG
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
        # it could be right & isoceles      right & scalene
    if a == b and b == a:                   #bug   a==b and b==c
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):    #bug   a*a + b*b = c*c   and should be ordered
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
        
        
def runClassifyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,b),sep="")

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testClassifyTriangle1(self): # test invalid inputs
        self.assertEqual(classifyTriangle(201,3,5),'InvalidInput','should be InvalidInput')
    def testClassifyTriangle2(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,5,201),'InvalidInput','should be InvalidInput') 
    def testClassifyTriangle3(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,201,5),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle4(self): 
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','should be equilateral')
    def testClassifyTriangle5(self): # test invalid inputs
        self.assertEqual(classifyTriangle(-1,3,5),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle6(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,-1,5),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle7(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,5,-1),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle8(self): # test invalid inputs
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle9(self): # test invalid inputs
        self.assertEqual(classifyTriangle(2.5,3,3),'InvalidInput','should be InvalidInput')   
    def testClassifyTriangle10(self): 
        self.assertEqual(classifyTriangle(3,6,3),'Isoceles','should be Isoceles')   
    def testClassifyTriangle11(self): 
        self.assertEqual(classifyTriangle(7,3,3),'NotATriangle','should be NotATriangle')   
    def testClassifyTriangle12(self): 
        self.assertEqual(classifyTriangle(3,3,7),'NotATriangle','should be NotATriangle')   
    def testClassifyTriangle13(self): 
        self.assertEqual(classifyTriangle(3,7,3),'NotATriangle','should be NotATriangle')   
    def testClassifyTriangle14(self): 
        self.assertEqual(classifyTriangle(3,3,5),'Isoceles','should be Isoceles')   
    def testClassifyTriangle15(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','should be Right')   
    def testClassifyTriangle16(self): 
        self.assertEqual(classifyTriangle(3,5,4),'Right','should be Right')
    def testClassifyTriangle17(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','should be Right')
    def testClassifyTriangle18(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','should be Scalene')
    def testClassifyTriangle19(self): 
        self.assertEqual(classifyTriangle(5,3,3),'Isoceles','should be Isoceles')
'''    def testClassifyTriangle(self): 
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
    def testClassifyTriangle(self):         
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be Isoceles')
   '''     

if __name__ == '__main__':
    # examples of running the  code
  #  runClassifyTriangle(1,2,3)
   # runClassifyTriangle(1,1,1)
    #runClassifyTriangle(3,4,5)
    
    print('Begin UnitTest')
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
