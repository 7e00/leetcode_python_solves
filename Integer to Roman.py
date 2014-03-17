class Solution:
    # @return a string
    def intToRoman(self, num):
        res = ""
        if num >= 1000:
            res += "M" * (num//1000)
            num %= 1000
        if num >= 500:
            if num >= 900:
                res += "CM"
                num -= 900
            else:
                res += "D"
                num -= 500
        if num >= 100:
            if num >= 400:
                res += "CD"
                num -= 400
            else:
                res += "C" * (num//100)
                num %= 100
        if num >= 50:
            if num >= 90:
                res += "XC"
                num -= 90
            else:
                res += "L"
                num -= 50
        if num >= 10:
            if num >= 40:
                res += "XL"
                num -= 40
            else:
                res += "X" * (num//10)
                num %= 10
        if num >= 5:
            if num >= 9:
                res += "IX"
                num -= 9
            else:
                res += "V"
                num -= 5
        if num >= 4:
            res += "IV"
        else:
            res += "I" * num
        return res