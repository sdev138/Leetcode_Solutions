class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if the last digit is less than 9
        if digits[len(digits)-1] < 9:
            digits[len(digits)-1] += 1
            return digits
        else:
            # making the last digit zero
            digits[len(digits)-1] = 0
            
            if len(digits) > 1:
                nextElement = len(digits) - 2
                while nextElement != 0:
                    if digits[nextElement] < 9:
                        digits[nextElement] += 1
                        return digits
                    else:
                        digits[nextElement] = 0
                        nextElement -= 1
                if digits[0] < 9:
                    digits[0] += 1
                else:
                    digits[0] = 0
                    digits.insert(0, 1)
            else:
                digits.insert(0, 1)
            
            return digits
            



            
