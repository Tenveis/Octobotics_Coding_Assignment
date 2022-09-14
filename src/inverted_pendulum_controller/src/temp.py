import math
import numpy

data = numpy.linspace(0, 2*math.pi, 50)
val = []
for i in data:
    val.append(math.sin(i))

print(val)
