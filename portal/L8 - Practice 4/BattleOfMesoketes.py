class BattleOfMesoketes:
    def succeeded_attacks(self, inp):
        SUCCEEDED_ATTACKS = 0
        WALL_HEIGHTS = { "N" : 0, "S" : 0, "E" : 0, "W" : 0 }

        attacks = {}

        def attack_wall(attack):
            tmp_heights = WALL_HEIGHTS.copy()
            for i in attack:
                data = i.split(" - ")
                if int(data[-1]) > WALL_HEIGHTS[data[1]]:
                    tmp_heights[data[1]] = max(tmp_heights[data[1]], int(data[-1]))
            return tmp_heights
        
        def resign_wall_heights(data):
            succeeded_attacks = 0
            for i in data:
                if data[i] > WALL_HEIGHTS[i]:
                    WALL_HEIGHTS[i] = data[i]
                    succeeded_attacks += 1
            return succeeded_attacks
        
        def process_attacks(inp):
            tmp = inp.split(";")
            succeeded_attacks = 0
            for day in tmp:
                k = 0
                for i in day:
                    if i == "$":
                        break
                    k += 1
                tmp_wall_heights = attack_wall([i.strip() for i in day[k + 1:].split(":")])
                succeeded_attacks += resign_wall_heights(tmp_wall_heights)
            return succeeded_attacks
        
        return process_attacks(inp)
        print(WALL_HEIGHTS)
        return SUCCEEDED_ATTACKS

Solution = BattleOfMesoketes()

# print(Solution.succeeded_attacks(inp = "Day 1$ T1 - N - X - 5 : T2 - W - X - 3;Day 2$ T1 - S - X - 2"))
print(Solution.succeeded_attacks(inp = "Day 1$ T1 - S - X - 4 : T1 - N - X - 2 : T3 - W - X - 3;Day 2$ T2 - S - X - 5: T2 - N - X - 1: T3 - N - X - 3; Day 3$ T1 - W - X - 2: T1 - W - X - 4: T2 - N - X - 3: T2 - S - X - 4"))
# print(Solution.succeeded_attacks(inp = "Day 1$ T1 - E - X - 4; Day 2$ T1 - W - X - 3"))