class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        int_val = 0
        cur_max = 0
        length = len(s)
        
        for pos in range(length-1, -1, -1):
            int_from_rom = roman_int_map[s[pos]]
            if int_from_rom >= cur_max:
                cur_max = int_from_rom
                int_val += int_from_rom
            else:
                int_val -= int_from_rom
        return int_val
        