count_ticket = int(input('Введите количество билетов: '))
cost=0
age=[int(input('Введите возраст: '+ str(x+1)+' посетителя ' )) for x in range(count_ticket)]
cost=len([item for item in age if 18<=item<25])*990
cost+=len([item for item in age if item>=25])*1390
if count_ticket>3:
    cost*=0.9
print('К оплате:', int(cost)) ## Выведем только рубли, копейки не считаем так как в тз про них ничего нет, пусть клиенты радуются)
