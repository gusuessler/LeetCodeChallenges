class Solution(object):
    def romanToInt(self, s):
        separated = [*s]
        numerals ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = 0
        for ix, i in enumerate(separated):
            print("Index:"+str(ix)+",Comprimento:"+str(len(separated))+",Soma:"+str(sum))
            if ix != len(separated)-1:
                if i == "I" and separated[ix+1] == "V":
                    sum=sum+4
                    separated.pop(ix)
                elif i == "I" and separated[ix+1] == "X":
                    sum=sum+9
                    separated.pop(ix)
                elif i == "X" and separated[ix+1] == "L":
                    sum=sum+40
                    separated.pop(ix)
                elif i == "X" and separated[ix+1] == "C":
                    sum=sum+90
                    separated.pop(ix)
                elif i == "C" and separated[ix+1] == "D":
                    sum=sum+400
                    separated.pop(ix)
                elif i == "C" and separated[ix+1] == "M":
                    sum=sum+900
                    separated.pop(ix)
                else:
                    val = numerals[i]
                    sum = sum+val
            else:
                val = numerals[i]
                sum = sum+val

        return sum
print(Solution.romanToInt("","XL"))       
print(Solution.romanToInt("","VI"))
print(Solution.romanToInt("","LVIII"))
print(Solution.romanToInt("","MCMXCIV"))
