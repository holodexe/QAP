per_cent = { 'ТКБ' : 5.6 , 'СКБ' : 5.9 , 'ВТБ' : 4.28 , 'СБЕР' : 4.0 }
cash = int(input('Введите вашу сумму '))
list=[]
for i in per_cent.values():
    a = int(i*cash/100)
    list.append(a)
print(list)
max_money = max(list)
print('Максимальная сумма депозита: ', max_money)