#commons 패키지(폴더)에 정의된 모듈로 수열의 합을 출력 
def sum1To10():
	sum = 0
	for i in range(1,11):
		sum += i
	print("1부터 10까지의 합 = ", sum)