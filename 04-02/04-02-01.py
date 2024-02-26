# 논리 메모리 주소 확인
foods = ["햄버거", "샐러드", "비스킷"]
print(id(foods))
print(hex(id(foods)))

# 다른 기본함수 
# 바이트로 처리하는 이유 : 이진 데이터로 작업하거나 이진 데이터를 처리하는 파일 또는 네트워크 스트림에서 읽고 쓰기 위해서이다.
mv = memoryview(b"Happy Day")

print(mv)

#return the Unicode of the first character
print(mv[0])

#return the Unicode of the second character
print(mv[1])

# IndexError
#print(mv[20])
