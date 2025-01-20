class InfixToPostfix:
    def convert(self, expression: str) -> str:
        n = len(expression)
        s = []
        
        # Corrected `is_power` function for handling precedence
        def is_power(a):
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            # Ensure we have a valid operator to compare
            if not s or s[-1] == '(':
                return True
            # Compare precedence
            return precedence[s[-1]] < precedence[a]

        out = ""
        for i in range(n):
            if expression[i] == "(":
                s.append(expression[i])
            elif expression[i] in "/*-+":
                while s and not is_power(expression[i]):
                    out += s.pop()
                s.append(expression[i])
            elif expression[i] == ")":
                while s and s[-1] != "(":
                    out += s.pop()
                if s:  # Remove the opening parenthesis
                    s.pop()
            else:
                out += expression[i]
        
        while s:
            out += s.pop()
        
        return out

# Testing
print(InfixToPostfix().convert("A+B"))        # Output: AB+
print(InfixToPostfix().convert("A+B*C"))      # Output: ABC*+
print(InfixToPostfix().convert("A*(B+C)"))    # Output: ABC+*
print(InfixToPostfix().convert("A*B+C"))      # Output: AB*C+
