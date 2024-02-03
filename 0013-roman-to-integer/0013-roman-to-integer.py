class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        s_list = [*s]
        n = len(s_list)    
        result = 0

        for i in range(n - 1):
            if rom_dict[s_list[i]] < rom_dict[s_list[i + 1]]:
                result -= rom_dict[s_list[i]]
            else:
                result += rom_dict[s_list[i]]

        result += rom_dict[s_list[-1]]
            
        return result