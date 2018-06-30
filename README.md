# demo
def ingly(s)
  if (len(s) == 4):
                a = s[:4]+'ing'
                return a
        if (len(s) ==7):
                b = s[:7]+'ly'
                return b
        else:
                return s
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
       
