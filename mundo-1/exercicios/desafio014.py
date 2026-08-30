# Conversor de temperatura
# Link do vídeo: https://youtu.be/9l_Gay8BuAw?si=FKpFzun5-NAx07OL

t = float(input('Digite a temperatura em °C: '))
f = (t * 1.8) + 32
k = 273 + t

print(f'A temperatura {t}°C em °F é {f}°F e em °K é {k}°K')