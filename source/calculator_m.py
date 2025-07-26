#list[0]는 리스트의 첫번째 인덱스 값을 의미한다.
#list[:]는 리스트의 모든 값을 의미한다.
#list[-1]는 리스트의 마지막 인덱스 값을 의미한다.
#list[1:]는 리스트의 두번째 인덱스부터 끝까지의 값을 의미한다.
a=input("Enter first number: ").split(" ")
b=list(map(int, a))
c=b[0]
for i in b[1:]:
    c -= i
print("The result of subtraction is:", c)