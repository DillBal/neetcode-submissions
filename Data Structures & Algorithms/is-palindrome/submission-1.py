class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = list(s)
        l, r = 0, len(palin) - 1

        while l < r:
            
            while l < r and not palin[l].isalnum():
                l += 1
            while r > l and not palin[r].isalnum():
                r -= 1
            if palin[l].lower() != palin[r].lower():
                print(palin[l].lower())
                return False
            l += 1
            r -= 1

        return True
