start = list(map(int,input("Digite o horário do início do jogo, no formato HH:MM:SS -->").split(":")))
# Pergunta pro usuário o horário inicial no formato padrão, usando : como separador e transforma isso em uma lista de inteiros
out = list(map(int,input("Digite o horário do fim do jogo, no formato HH:MM:SS -->").split(":")))
# Pergunta pro usuário o horário final no formato padrão, usando : como separador e transforma isso em uma lista de inteiros

horas_start = start[0]
minutos_start = start[1]
segundos_start = start[2]

horas_out = out[0]
minutos_out = out[1]
segundos_out = out[2]
#Indica os valores na lista criada anteriormente

horas_em_segundos_start = horas_start * 60 * 60
minutos_em_segundos_start = minutos_start * 60
segundos_totais_start = horas_em_segundos_start + minutos_em_segundos_start + segundos_start

horas_em_segundos_out = horas_out * 60 * 60
minutos_em_segundos_out = minutos_out * 60
segundos_totais_out = horas_em_segundos_out + minutos_em_segundos_out + segundos_out
# Converte tudo pra segundo para facilitar os cálculos

if segundos_totais_out < segundos_totais_start: #Case para quando o jogo virou a noite
    tempo_i = (24 * 60 * 60 - segundos_totais_start) + segundos_totais_out
    horas_final = tempo_i // 3600
    resto = tempo_i % 3600
    minutos_final = resto // 60
    segundos_final = resto % 60


else: #Case para quando ambos os eventos aconteceram no mesmo dia
    tempo_i = segundos_totais_out - segundos_totais_start
    horas_final = tempo_i // 3600
    resto = tempo_i % 3600
    minutos_final = resto // 60
    segundos_final = resto % 60

print(f"O evento durou {horas_final} hora(s), {minutos_final} minuto(s) e {segundos_final} segundo(s).")

