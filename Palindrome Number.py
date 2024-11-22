# https://leetcode.com/problems/palindrome-number

def isPalindrome(x):
    if x<0:
        return False
    else:
        origin = x
        reversed =  0
        while x!=0:
            last_digit = x%10
            reversed = reversed*10 + last_digit
            x//=10
        if reversed == origin: 
            return True
        else: 
            print(type(reversed))
            return False
        
        
if __name__ == '__main__':
    print(isPalindrome(-121))



