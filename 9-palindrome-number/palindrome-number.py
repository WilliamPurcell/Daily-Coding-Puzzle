class Solution(object):
    def isPalindrome(self, x):
        temp = x
        reverse = 0
        if x<0:         #Check to see if negative. All negative is not a palindrome
            return False
        while temp != 0: #Reverse the number
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10
        return reverse == x #Check if the reversed number is equal to the original number. If it is, the number is a palindrome

        