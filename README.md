c = np.array([
    [[100, 50]],
    [[150, 80]],
    [[120, 120]],
    [[90, 100]]
])
Primero buscamos el mínimo y máximo valor de las coordenadas x (horizontal):

xs = [100, 150, 120, 90]

x mínimo = 90

x máximo = 150

Luego hacemos lo mismo para las coordenadas y (vertical):

ys = [50, 80, 120, 100]

y mínimo = 50

y máximo = 120

Cómo se calculan w y h:
w (ancho) = x máximo - x mínimo = 150 - 90 = 60

h (alto) = y máximo - y mínimo = 120 - 50 = 70

x = 90     # esquina superior izquierda en X
y = 50     # esquina superior izquierda en Y
w = 60     # ancho del rectángulo (ancho)
h = 70     # altura del rectángulo (alto)
