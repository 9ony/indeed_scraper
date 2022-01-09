exec(open("1-5CodeChallenge1.py").read())

print("---------------------")
num1=input('첫번째숫자를 입력하세요')
num2=input('두번째숫자를 입력하세요')
operation=input('연산자를 입력하세요')
def math(num1,num2,operation):
  try:
    if(operation=="+"):
     return int(num1)+int(num2)
    if(operation=="-"):
     return int(num1)-int(num2)
    if(operation=="*"):
     return int(num1)*int(num2)
    if(operation=="/"):
     return int(num1)/int(num2)
    if(operation=="%"):
     return int(num1)%int(num2)
    if(operation=="**"):
     return int(num1)**int(num2)
  except :
    ()