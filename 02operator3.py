num1 = float(input("첫번째 숫자를 입력하세요:"))
num2 = float(input("두번째 숫자를 입력하세요:"))

result1 = num1 == num2
print("같은지 비교", result1) #False

result2 = num1 != num2
print("다른지 비교", result2) #True

result3 = num1 >= num2
print("큰지 비교", result3) #False

result4 = num1 < num2
print("작은지 비교", result4) #True

result5 = not (num1 > num2)
print("관계식 판단의 부정", result5) #True 

logical1 = result1 and result2 #F and T ==> False
logical2 = result1 or result2 #F or T ==> True
logical3 = not (result1 or result2) #not(True) ==> False

print('logical1', logical1)
print('logical2', logical2)
print('logical3', logical3)

