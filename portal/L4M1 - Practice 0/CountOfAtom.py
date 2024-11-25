class Solution:
    def countAtoms(self, formula: str):
        countedAtoms = ""
        atom_map = {}
        atom_count = {}
        n = len(formula)
        let = 0
        factor = 1
        i = 0
        
        def processStringToDict(formula: str, factor: int):
            dit = {}
            t = ""
            # print("Processing formula:", formula, factor)
            for i in formula:
                if i.isdigit():
                    # print(t)
                    dit[t] = int(i) * factor
                    t = ""
                else:
                    t += i
            dit[t] = factor
            return dit
        def processNextElement(formula: str):
            # print("Formula: ", formula)
            t = ""
            for i in range(len(formula)):
                if formula[i] != ")":
                    t += formula[i]
                else:
                    # print("t:", t)
                    if formula[i + 1].isdigit():
                        # print("Processed t:", processStringToDict(t, int(formula[i + 1])))
                        return i, (processStringToDict(t, int(formula[i + 1])))
                    
                    return i - 1, (processStringToDict(t, 1))
            return len(formula) + 1, (processStringToDict(t + "1", 1))
        
        while i < n:
            while formula[i] == "(":
                i += 1
            if formula[i] == "(":
                tmpI, atom_map[let] = processNextElement(formula[i + 1:])
                i += tmpI + 2
                let += 1
            elif formula[i].isdigit():
                i += 1
            else:
                tmpI, atom_map[let] = processNextElement(formula[i:])
                i += tmpI + 2
                let += 1
        
        # print(atom_map)
        
        for i in atom_map:
            for j in atom_map[i]:
                if j in atom_count:
                    atom_count[j] += atom_map[i][j]
                else:
                    atom_count[j] = atom_map[i][j]
        dic = sorted(atom_count)
        for i in dic:
            if i != "":
                countedAtoms += f"{i}{atom_count[i] if atom_count[i] != 1 else ''}"
        return countedAtoms
    
print(Solution().countAtoms(input()))