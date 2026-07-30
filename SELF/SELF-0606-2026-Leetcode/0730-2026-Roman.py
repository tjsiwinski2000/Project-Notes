# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    """ TJS: my first olution which worked """
    def romanToInt(self, s: str) -> int:
        if "IV" in s:
            s = s.replace('IV','z')
        if 'IX' in s:
            s = s.replace('IX','y')
        if 'XL' in s:
            s = s.replace('XL','w')
        if 'XC' in s:
            s= s.replace('XC','q')
        if 'CD' in s:
            s = s.replace('CD', 'k')
        if 'CM' in s:
            s = s.replace('CM', 'j')
        
        value=0
        for numeral in s:
            if numeral == 'I':
                value +=1
            elif numeral == 'V':
                value +=5
            elif numeral == 'X':
                value +=10
            elif numeral == 'L':
                value += 50
            elif numeral =='C':
                value += 100
            elif numeral == 'D':
                value += 500
            elif numeral == 'M':
                value += 1000
            elif numeral == 'z':
                value += 4
            elif numeral == 'y':
                value += 9
            elif numeral == 'w':
                value += 40
            elif numeral == 'q':
                value += 90
            elif numeral == 'k':
                value += 400
            elif numeral == 'j':
                value += 900
        
        return value
       
class Solution2:
    """ TJS: incorporating dictionary approach from CLAUDE """
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        temp_list = []
        for numeral in s:
            temp_list.append(values[numeral])
        # temp_list is now a list 
        # MCMXCIV becomes  [1000, 100, 1000, 10, 100, 1, 5]
        total_value=0
        
        for index in range(0,len(temp_list)):
            # iterate thr. temp_list
            # if small is before a larger, subract the smaller e.g. 1,5
            print(f'{index}. {temp_list[index]}')
            if index+1 < len(temp_list) and temp_list[index] >= temp_list[index +1]:
                total_value += temp_list[index]
            elif index ==len(temp_list)-1:
                # last value of the list; gets added since no value after it
                total_value += temp_list[index]
            else:
                total_value -= temp_list[index]
            print(f'total_value now : {total_value}')
        return  total_value
    
    
my_object = Solution2()
print(my_object.romanToInt('MCMXCIV'))

