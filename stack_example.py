class StackExample:
    def isValid(self, s: str) -> bool:
        stack = []

        stackToOpen = {"]" : "[" , "}" : "{" , ")" : "("}

        for c in s:
            if c in stackToOpen:
                if stack and stack[-1] == stackToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
