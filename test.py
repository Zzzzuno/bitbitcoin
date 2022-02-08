import pyupbit
access = "BS53Ga2e7ynAZqK0gAxqhM6i3gdi9x7RwmMlrafh"          # 본인 값으로 변경
secret = "Rtn5V1naSVbT7o2kPUl8azqcr4KVtmJOj8NDrrtN"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
