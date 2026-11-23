class Solution:
    def isPalindrome(self, s: str) -> bool:
        isP = list(s)
        l, r = 0, len(isP) - 1

        while l < r:
            # print("l", isP[l])
            # print("r", isP[r])
            # print(not isP[r].lower().isalnum())
            # if isP[l].lower().isalnum():
            #     l += 1
            # if isP[r].lower().isalnum():
            #     r -= 1

            while l < r and not isP[l].lower().isalnum():
                l += 1

            while l < r and not isP[r].lower().isalnum():
                r -= 1
            
            if isP[l].lower() != isP[r].lower():
                return False
            
            l += 1
            r -= 1
        return True