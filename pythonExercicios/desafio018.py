import math

a = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo {} tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, sen, cos, tan))
