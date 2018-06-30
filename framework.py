#!/usr/bin/python -tt

# Python string assignments

# Fill in the code for the functions defined below.
# The main() function is defined to call the other
# functions with few different inputs. The program
# will print 'OK' when the functions are coded
# correctly. The placeholder for your code is clearly
# marked for the function

# Exercise 1-E. IngLy
# Given a string, if its length is at least 3,
# add 'ing' to its end. If it already ends in 'ing'
# then add 'ly' instead. If the string is less than 3,
# leave it unchanged. Return the resulting string.
def ingly(s):

        var =len(s)
        if (var>3):
	 if (s[-3:]=="ing"):
	  got=s+"ly"
	 else:
	  got=s+"ing"
	else:
	 got= s
	return got

# Simple test() function used in main to check and print
# what each function returns vs. what it is supposed to
# return.

def test(got, expected):
 if got == expected:
  prefix = ' OK '
 else:
  prefix = '  X '
 print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
# The repr() function returns the canonical string representation of
# the object.

# main() function which calls the above functions with inputs. The
# test() function is used to check if each result is correct or not.

def main():
 print 'My python IngLy Exercise'
 # Each line calls ingly function defined above, compares its results
 # to the expected for the call.
 test(ingly('hail'), 'hailing')
 test(ingly('swiming'), 'swimingly')
 test(ingly('do'), 'do')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
 main()
