![Превью](/img/prew.png "")

# Алгоритм Дейкстры (Dijkstra's algorithm)

Алгоритм Дейкстры (Dijkstra's algorithm) - является алгоритмом поиска кратчайшего пути в графе. Он используется для нахождения кратчайшего пути между двумя вершинами в графе с весами ребер.

## Алгоритм работает следующим образом:

 1. Выбирается начальная вершина и она помечается как посещенная.  

 2. Для каждой непосещенной соседней вершины рассчитывается ее расстояние от начальной вершины.  

 3. Вершина с наименьшим расстоянием помечается как посещенная и становится текущей.  

 4. Шаги 2 и 3 повторяются, пока не будут посещены все вершины или не будет достигнута целевая вершина.  


Алгоритм Дейкстры является одним из самых эффективных алгоритмов поиска кратчайшего пути и широко используется в различных областях.

## Задача:

Изначальное задание имело вид:

![Фото изначального задания](/img/ph1.png "")

Для упрощения понимания, я заменил название точек с цифр на буквы. Расставил направление стрелок в оптимальном положении.

![Фото адаптированного задания](/img/ph2.png "")

Изначально рассчитаем всё вручную.

![Фото рассчёта](/img/ph3.png "")

Проверим через скрипт.

![Фото результаты скрипта](/img/ph4.png "")

Усложним, и немного изменим задание. Теперь нам надо добраться с точки I в точку A

![Фото задания](/img/ph5.png "")

Решим задачу через скрипт:

![Фото работы скрипта](/img/ph6.png "")

Ну и в конце проверим работу скрипта, повторим алгоритмы ручками.

![Фото ручного решения](/img/ph7.png "")

Всё сошлось!

























## Пояснение кода:

   

     import heapq  


Этот код реализует алгоритм Дейкстры для нахождения кратчайшего пути в графе. Он использует библиотеку `heapq` для поддержки очереди с приоритетом, чтобы выбрать вершину с наименьшим расстоянием в каждый момент времени.
      
    def dijkstra(graph, start, end):  
        distances = {vertex: float('infinity') for vertex in graph}  
        distances[start] = 0  
      previous_vertices = {vertex: None for vertex in graph}  
        queue = [(0, start)]  
        while queue:  
            (distance, current) = heapq.heappop(queue)  
            if distance > distances[current]:  
                continue  

`dijkstra` функция принимает 3 аргумента: граф, начальную вершину и конечную вершину. Граф представлен в виде словаря, где ключи являются именами вершин, а значения - словарями, содержащими соседей и их вес.

Внутри функции создается словарь `distances`, который хранит расстояния до каждой вершины от начальной вершины. Начальные значения устанавливаются в `float('infinity')`, кроме расстояния до начальной вершины, которое устанавливается равным нулю.

`start` и `end` являются именами начальной и конечной вершин соответственно.

 `distances` словарь хранит расстояния от начальной вершины до других вершин. Ключи этого словаря являются именами вершин, а значения - расстояниями. В начале, все расстояния устанавливаются равными `float('inf')`, кроме расстояния до начальной вершины, которое устанавливается равным нулю.

`previous_vertices` словарь хранит информацию о предыдущей вершине на пути от начальной до другой вершины. Ключи этого словаря являются именами вершин, а значения - именами предыдущих вершин.

Цикл `for` в этом коде используется для обхода соседних вершин текущей вершины. Он исполняется столько раз, сколько у текущей вершины соседей.

Внутри цикла:

1.  Для каждой соседней вершины вычисляется новое расстояние через текущую вершину.
2.  Если это расстояние меньше текущего расстояния, то оно обновляется, а информация о предыдущей вершине записывается в `previous_vertices`.

Цикл `for` является вложенным циклом, который исполняется в теле цикла `while`. Он выполняется для каждой текущей вершины, которую выбирает цикл `while`.

     for neighbor, weight in graph[current].items():  
                distance = distances[current] + weight  
                if distance < distances[neighbor]:  
                    distances[neighbor] = distance  
                    previous_vertices[neighbor] = current  
                    heapq.heappush(queue, (distance, neighbor))  
        path, current = [], end  

Цикл `while` в этом коде используется для поиска оптимальных расстояний до всех вершин. Он продолжается до тех пор, пока список `vertices` не станет пустым.

Внутри цикла:

1.  Выбирается вершина с минимальным расстоянием из списка `vertices`.
2.  Если выбранная вершина является конечной вершиной, то цикл завершается.
3.  Иначе, для каждой соседней вершины вычисляется новое расстояние через текущую вершину. Если это расстояние меньше текущего расстояния, то оно обновляется, а информация о предыдущей вершине записывается в `previous_vertices`.

После завершения цикла, информация в `previous_vertices` используется для восстановления пути от начальной до конечной вершины.

        while current:  
            path.append(current)  
            next_vertex = previous_vertices[current]  
            current = next_vertex  
        path = path[::-1]  
        return (distances[end], path)
        
  `graph` словарь хранит информацию о вершинах и ребрах графа. Ключи этого словаря являются именами вершин, а значения - словари с соседними вершинами и их весами.
      
    graph = {  
        'A': {'B': 6, 'D': 4},  
      'B': {'C': 3},  
      'C': {'E': 4, 'H': 5},  
      'D': {'C': 5, 'H': 3},  
      'E': {'G': 4},  
      'F': {'H': 5},  
      'G': {'J': 2, 'I': 4},  
      'H': {'G': 3, 'I': 7},  
      'I': {'J': 1},  
      'J': {},  
      
      
    }  
      
    print(dijkstra(graph, 'A', 'J'))


Вывод результатов в этом коде осуществляется путем последовательного отслеживания вершин, через которые прошел оптимальный путь.

1.  Инициализируется переменная `path`, которая будет хранить путь.
2.  Используется цикл `while` для движения от конечной вершины до начальной вершины, отслеживая информацию о предыдущей вершине в словаре `previous_vertices`.
3.  Каждый раз, когда мы переходим к предыдущей вершине, мы добавляем ее в `path`.
4.  После того, как мы достигли начальной вершины, `path` содержит оптимальный путь в обратном порядке.
5.  Чтобы вывести путь в правильном порядке, мы используем метод `reversed()` для инверсии списка.

В конечном итоге, путь выводится в виде списка вершин, начиная с начальной вершины и заканчивая конечной вершины.
