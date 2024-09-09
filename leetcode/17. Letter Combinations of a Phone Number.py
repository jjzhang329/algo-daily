#backtrcking, O(4**N*N)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == '': return result
        self.backtracking(digits, [], 0, result)
        
        return result
    
    def backtracking(self, digits, path, idx, result):
        if idx == len(digits):
            result.append(''.join(path))
            return 

        phone = {   '2' : 'abc',
                    '3' : 'def',
                    '4' : 'ghi',
                    '5' : 'jkl',
                    '6' : 'mno',
                    '7' : 'pqrs',
                    '8' : 'tuv',
                    '9' : 'wxyz'
                }
        key = digits[idx]
        letters = phone[key]

        for letter in letters:
            path.append(letter)
            self.backtracking(digits, path, idx+1, result)
            path.pop()