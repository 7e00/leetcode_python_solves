class Solution:
    # @return a boolean
    def isValid(self, s):
        sta = []
        top = 0
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                if top == len(sta):
                    sta.append(letter)
                else:
                    sta[top] = letter
                top += 1
            else:
                if top == 0:
                    return False
                if letter == ')' and sta[top-1] != '(':
                    return False
                if letter == ']' and sta[top-1] != '[':
                    return False
                if letter == '}' and sta[top-1] != '{':
                    return False
                top -= 1
        return top == 0