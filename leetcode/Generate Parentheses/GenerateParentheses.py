class Solution(object):
    
    def generateParenthesis(self, n):
        res = []
        def dfs(path, left, right):             
            if left > n  or right > n: return   
            if left == right == n:  
                res.append(path)   
                return     
            if left > right:    
                dfs(path + '(', left + 1, right)
                dfs(path + ')', left, right + 1)   
            else:
                dfs(path + '(', left + 1, right)              
        dfs('', 0, 0)   
        return res