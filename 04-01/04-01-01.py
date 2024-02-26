
# 변수 my_name이 문자열 객체를 참조한다.
# 이때 문자열 객체 "Gookhee"의 레퍼런스 카운트는 1이다.
my_name = "Gookhee"

your_name = my_name # 레퍼런스 카운트 2로 증가!

# 문자열 객체 "Gookhee"의 레퍼런스 카운트는 0이다.
# 그로 인해 문자열 객체 "Gookhee"는 가비지 컬렉션 메커니즘에 의해 소멸 대상이 된다. 
my_name = "Cookie"
your_name = "Lucky"

# 소멸 대상으로 등록된 즉시 소멸되는 것은 아니다. 시스템에 시간적 여유가 생기면 파이썬 인터프리터에 의해 소멸된다.



