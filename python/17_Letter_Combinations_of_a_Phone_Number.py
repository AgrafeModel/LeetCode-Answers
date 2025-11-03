class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digit_letters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }


        def f(i,c):
            if i ==len(digits):
                res.append(c)
            else:
                for l in digit_letters[digits[i]]:
                    f(i+1,c+l)
        
        f(0,"")
        
        return res

        
        
