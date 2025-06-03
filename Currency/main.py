pesos = int(input('Enter the pesos you have got:\n '))
soles = int(input('Enter the soles you have got:\n '))
reais = int(input('Enter the reais you have got:\n '))

usd_pesos = pesos * 19.27
usd_soles = soles * 3.70
usd_reais = reais * 5.65

total_usd = usd_pesos + usd_soles + usd_reais

print(f"Total in USD: {total_usd:.2f}")