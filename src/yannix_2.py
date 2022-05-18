def isValid(s):

    leftChar = []
    for c in s:
        if c in ['(', '{', '[']:
            leftChar.append(c)
        # check if found same type of brackets    
        elif c == ')' and len(leftChar) != 0 and leftChar[-1] == '(':
            leftChar.pop()
        elif c == '}' and len(leftChar) != 0 and leftChar[-1] == '{':
            leftChar.pop()
        elif c == ']' and len(leftChar) != 0 and leftChar[-1] == '[':
            leftChar.pop()
        else:
            return False
    return leftChar == []

# Test outputs
# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("([)]"))
print(isValid("{[]}"))