class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ""

        stack = []
        wholeWord = []
        paranthesisIndex = {}

        # for loopto iterate through the paranthesis
        for i in range(len(s)):
            if s[i] == "(" or s[i] == ")":
                # adding the paranthesis with their indexes
                paranthesisIndex[i] = s[i]
                stack.append(s[i])

            # adding the paranthesis to the actual string (chars will be removed later)
            wholeWord.append(s[i])
            if s[i] == ")":
                if stack:
                    if stack[-1] == "(":
                        # popping the paranthesis if match
                        stack.pop()

        return str(wholeWord)
