days = int(input('how many rental days? '))
km = float(input('and what was the distance traveled (km/h)? '))

p = 60*days + 0.15*km

print(f'you have to pay R${p:.2f}')
