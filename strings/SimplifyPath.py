class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        stack = []
        for i in path:
            if i == "":
                continue
            if i == ".." and stack:
                stack.pop()
            elif i == ".":
                pass
            else:
                if i != "..":
                    stack.append(i)
            print(i, stack)

        return f'/{"/".join(stack)}'

# Possible test cases
# print(Solution().simplifyPath(path="/abc/..."))
# print(Solution().simplifyPath(path="/../"))
# print(Solution().simplifyPath(path="/.../a/../b/c/../d/./"))
# print(Solution().simplifyPath(path="/home/user/Documents/../Pictures"))
