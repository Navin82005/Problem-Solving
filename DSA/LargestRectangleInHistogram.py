class LargestRectangleInHistogram:
    def findArea(self, histogram):
        max_area = 0
        stack = []
        n = len(histogram)
        
        for i in range(len(histogram)):
            start = i
            while stack and stack[-1][1] > histogram[i]:
                idx, height =  stack.pop()
                max_area = max(max_area, (i - idx) * height)
                start = idx
            stack.append([start, histogram[i]])
        # print(stack)
        
        for i in range(len(stack)):
            max_area = max(max_area, (n - stack[i][0]) * stack[i][1])
        
        return max_area

print(LargestRectangleInHistogram().findArea([2, 1, 5, 6, 2, 3]))