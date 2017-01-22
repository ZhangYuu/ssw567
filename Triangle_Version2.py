# -*- coding: utf-8 -*-
"""
Triangle Classification
Created on Fri Jan 20 22:04:37 2017

@author: Zhi Li, Yu Zhang
"""

'''As the square root of a number is always a unlimited dicimal,
    we need round() to make it equal to its square.'''

import unittest    

class Triangle:
    #a,b,c are the three side of a triangle.
    def classify_triangle(self, a, b, c):
        '''
            'e' represent equilateral triangles
            'i' represent isosceles triangles
            'ir' represent isosceles right triangles
            's' represent scalene triangles
            'sr' represent scalene right triangles
        '''
        result = ''
        if(a+b<=c or a+c<=b or b+c<=a):
            answer = "Sorry! It's not a triangle!"
        if(a==b and a==c):
            answer = "It's a equilateral triangle!"
            result = 'e'
        elif(a==b or a==c or b==c):
            if(round((a*a),5) + round((b*b),5) == round((c*c),5)):
                answer = "It's an isosceles right triangle!"
                result = 'ir'
            else:
                answer = "It's an isosceles triangle!"
                result = 'i'
        else:
            if(round((a*a),5) + round((b*b),5) == round((c*c),5)):
                answer = "It's a scalene right triangle!"
                result = 'sr'
            elif(round((a*a),5) + round((c*c),5) == round((b*b),5)):
                answer = "It's a scalene right triangle!"
                result = 'sr'
            elif(round((c*c),5) + round((b*b),5) == round((a*a),5)):
                answer = "It's a scalene right triangle!"
                result = 'sr'
            else:
                answer = "It's a scalene triangle!"
                result = 's'
        
        print (answer)
        return result


class test_Triangle(unittest.TestCase):
    def test_1(self):
        self.test1 = Triangle()
        try:
            self.assertEqual(self.test1.classify_triangle(1, 1, 1.5), 'e')
        except AssertionError:
            print('There is something wrong here.')


            
#three sides named a, b, c
    
test = test_Triangle()
test.test_1()


