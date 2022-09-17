
from math import remainder


def reverseNum(number):
    reverse = 0
    # while(number>0):
    #     remainder=number%10
    #     print(remainder," dividing number by 10")
    #     print(reverse,"before revese")
    #     reverse=(reverse*10)+remainder
    #     print("after reverse",reverse)
    #     number=number//10
    #     print(number)

    """uding foor loop"""
    for i in range(len(str(number))):
        remainder=number%10
        reverse=(reverse*10)+remainder
        number=number//10
 
    return reverse

"""Check palindrome"""
def checkPalindrome():
    number = int(input("enter number: "))
    reverseNumber = reverseNum(number)
    if number== reverseNumber:
        print(number," is palindrome")

checkPalindrome()