class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       """
       :type s:str
       :rtype:int
       """
       strings=s.split()
       return len(strings[-1]) 