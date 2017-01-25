# -*- coding: utf-8 -*-
"""
Triangle Classification
Created on Fri Jan 20 22:04:37 2017

@author: Zhi Li, Yu Zhang, Maryam
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
        try:
            lst = [a,b,c]
            lst.sort()
            a = lst[0]
            b = lst[1]
            c = lst[2]
            
            if(a + b <= c or a <= 0 or b <= 0 or c <= 0):
                answer = "Sorry! It's not a triangle!"
                result = 'n'
            else:
                if(a == c):
                    answer = "It's a equilateral triangle!"
                    result = 'e'
                elif(a == b or b == c):
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
                    else:
                        answer = "It's a scalene triangle!"
                        result = 's'
            print (answer)
            return result
        except TypeError:
            print ('Please input valid numbers.')
            return result


class test_Triangle(unittest.TestCase):
    
    def test(self, name, result, a, b, c):
        print('{}:'.format(name))
        self.tri = Triangle()
        try:
            self.assertEqual(self.tri.classify_triangle(a, b, c), result)
            print('{} passed.'.format(name))
        except AssertionError:
            print('{} Failed.'.format(name))
        print()
        
    
    
        


            
#three sides named a, b, c
test = test_Triangle()
#Test Cases

#succeed
name = 'Test1'
test.test(name, 'e', 1, 1, 1)

name = 'Test2'
test.test(name, 'i', 1.5, 1, 1)

name = 'Test3'
test.test(name, 'ir', 1, 1, 2**0.5)

name = 'Test4'
test.test(name, 'sr', 3, 4, 5)

name = 'Test5'
test.test(name, 's', 3, 4, 6)

name = 'Test6'
test.test(name, 'n', 1, 1, 2)

#fail
name = 'Test7'
test.test(name, 'e', 1, 1, 2)

name = 'Test8'
test.test(name, 'i', 1, 1, 1)

name = 'Test9'
test.test(name, 'ir', 1, 2, 2**0.5)

name = 'Test10'
test.test(name, 'sr', 3, 4, 6)

name = 'Test11'
test.test(name, 's', 3, 4, 5)

name = 'Test12'
test.test(name, 'e', 1, 1, 0)

name = 'Test13'
test.test(name, 'e', '1', 1, 1)

name = 'Test14'
test.test(name, 'e', -1, 1, 1)

