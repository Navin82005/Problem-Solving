class StringFormatting:
    def format(self, s: str):
        def get_number(s):
            tmp = ""
            idx = 1
            for i in s:
                if i.isdigit():
                    idx += 1
                    tmp += i
                else:
                    return tmp, idx
            return tmp, idx

        stack = {}
        indent = -1
        
        n = len(s)
        i = 0
        sub_num = ""
        
        while i < n:
            if s[i] == ",":
                i += 1
                continue
            if s[i] == "}":
                indent -= 1
                i += 1
                continue
            if s[i] == "{":
                indent += 1
                i += 1
                continue
            sub_num, idx = get_number(s[i:])
            i += idx
            if indent in stack:
                stack[indent].append(sub_num)
            else:
                stack[indent] = [sub_num]
        
        print(stack)

print(StringFormatting().format(s = r"{{3,2,1,5},{9,1,3,0}}"))
