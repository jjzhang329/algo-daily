class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res  = []

        def backtracking(left, right):
            if left == right == n:
                valid = ''.join(stack)
                res.append(valid)
                return 
            
            if left < n:
                stack.append('(')
                backtracking(left+1, right)
                stack.pop()
            
            if right < left:
                stack.append(')')
                backtracking(left, right+1)
                stack.pop()
        
        backtracking(0, 0)
        return res