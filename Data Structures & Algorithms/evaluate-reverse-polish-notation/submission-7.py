class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                x=stack.pop()
                y=stack.pop()
                stack.append(x+y)
            elif i=="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)
            elif i=="*":
                x=stack.pop()
                y=stack.pop()
                stack.append(x*y)
            elif i=="/":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y/x))

            else:
                stack.append(int(i))
            print(stack[-1])
        return stack[-1]