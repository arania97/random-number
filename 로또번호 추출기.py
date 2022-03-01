from random import *
from time import sleep
import webbrowser

print("인생을 쉽게 살고싶은 여러분들을 위해 만든 로또번호 추출기 입니다") #원하는 말 적어도 됩니다.
sleep(1)
print("This program is can change your life. wait 3 second") #너무 느리면 sleep값 수정하든가 지우면 개빨라짐
sleep(3)
print(int(random() * 45) + 1)
sleep(0.5)
print(int(random() * 45) + 1)
sleep(0.5)
print(int(random() * 45) + 1)
sleep(0.5)
print(int(random() * 45) + 1)
sleep(0.5)
print(int(random() * 45) + 1)
sleep(0.5)
print("보너스 번호")
print(int(random() * 45) + 1)
sleep(0.5)
print("만약 당첨되었으면 농협3021419537971 30%때주슨")
sleep(0.7)
print("3초후 로또 최신 당첨번호 보는곳이 열립니다.")
sleep(3)
webbrowser.open("https://dhlottery.co.kr/common.do?method=main") #''안에 원하는 웹사이트 url넣기