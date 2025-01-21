class Solution:
    def validPalindrome(self, s: str) -> bool:
        # checking the string if its a palindrome
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            # found a mismatched pair, will try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)    
            i += 1
            j -= 1
        return True

# if the imperfections are in the middle, then you can remove one to be a palindrome
# if one imperfection exists, everything should be equal below the bound