class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, 0, '', result)
        return result 
    

    def backtracking(self, s, idx, countDot, current, result):
        if countDot == 3:
            if self.is_valid(s, idx, len(s)-1):
                current += s[idx:]
                result.append(current)
                return 
        
        for i in range(idx, len(s)):
            if self.is_valid(s, idx, i):
                sub = s[idx:i+1]
                self.backtracking(s, i+1, countDot+1, current + sub + '.', result)
            else:
                break


    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 0开头的数字不合法
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  # 遇到非数字字符不合法
                return False
            num = num * 10 + int(s[i])
            if num > 255:  # 如果大于255了不合法
                return False
        return True