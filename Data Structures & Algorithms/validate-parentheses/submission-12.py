class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i == ']':
                if stack!=[] and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack!=[] and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif i == ')':
                if stack!=[] and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if not stack else False


        stack=[]
        d={')':'(','}':'{',']':'['}

        for i in s:
            if stack and d[i]==stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False
                
