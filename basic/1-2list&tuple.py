# list (배열) 변경가능한 배열 사용법: 괄호가 '[]'로 사용
l_days =["월","화","수","목","금"]
print(type(l_days))
print(l_days[0])
l_days.append("토")
print(l_days)
l_days.reverse()
print(l_days)
l_days.clear()
print(l_days)
#---------------------------------
# tuple(배열) *변경불가능한 배열 사용법: 괄호가 '()'로 사용
t_days = ("월","화","수","목","금")
print(type(t_days))
#t_days.reverse() # tuple type of object has no attribute 'reverse'
#print(t_days)
#t_days.clear()  # tuple type of object has no attribute 'clear'
#print(t_days)
t_days.append("토") # tuple type of object has no attribute 'append'
print(t_days)
#이처럼 튜플은 리스트와는 다르게 배열의 인자값을 바꿀수 없음 삭제 수정 추가 등등..