start, out = map(int,input().split())
if start>out or start==out:
    tempo = (24-start) + out
else:
    tempo = out-start
print(f"O JOGO DUROU {tempo} HORA(S)")