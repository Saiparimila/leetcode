class Solution(object):
    def isPalindrome(self, x):
        str1=str(x)
        rev=str1[::-1]
        return str1==rev

        