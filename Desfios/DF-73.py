time = ('Palmeiras', 'Flamengo' ,'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético', 'Fortaleza', "São Paulo" ,"América" ,"Botafogo", "Santos", "Goiás", "Red Bull" ,"Bragantino", 'Coritiba', "Cuiabá" ,"Grêmio" ,"Vasco" ,"Bahia")

print("=-"*25)
print(f"Lista de times do Brasileirão: {time}")
print("=-"*25)
print(f"O 5 primeiros {time[0:5]}")
print("=-"*25)
print(f"Os 4 ultimos são {time[-4:]} ")
print("=-"*25)
print(f"Em ordem alfabetica {sorted(time)}")
print("=-"*25)
print(f"São paulo esta na posição {time.index('São Paulo')+1}º")