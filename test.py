try:

    3 / 0

except IndexError:

    print("인덱스가 안맞아요!")


except ZeroDivisionError:

    print("0으로 나누면 안돼요!")

finally:

    print("예외에 상관없이 언제나 실행되요!")  

 

print("프로그램이 정상적으로 종료됩니다!")
print("수정해봅니다.!")