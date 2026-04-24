import time

tempo = 10

while tempo > 0:
    print(f"tempo restante: {tempo}segundos")
    time.sleep(1)  # espera 1 segundo
    tempo -= 1
print("tempo finalizado. pode abrir a prensa.") 