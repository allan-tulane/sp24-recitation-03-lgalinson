from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    
    # test with zero
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(5)) == 0*5
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(0)) == 10*0

    # test with large numbers
    assert quadratic_multiply(BinaryNumber(123), BinaryNumber(456)) == 123*456
    assert quadratic_multiply(BinaryNumber(999), BinaryNumber(999)) == 999*999

    # test with edge cases
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(0)) == 1*0
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0*0