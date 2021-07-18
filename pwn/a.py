from pwn import *

# 외부 서버와 연결하는 함수
r = remote("site.com", 10400) # 사이트 url과 포트 번호
r.recvline() # 한 줄의 문자열 읽어오기
r.recvuntil("buf = (") # buf = ( 까지 값만 받기

r.sendline() # recvline은 받기 이건 보내기


r.interactive
