python
import random
import time
import matplotlib.pyplot as plt

sizes = range(1000, 100001, 1000)  
times = []

for size in sizes:
    start_time = time.time()  
    random_list = [random.randint(0, 100) for _ in range(size)]  
    end_time = time.time()  
    times.append(end_time - start_time)  

plt.plot(sizes, times)  
plt.xlabel('Размер списка')
plt.ylabel('Время создания (сек)')
plt.title('Зависимость времени создания списка от его размера')
plt.show()
