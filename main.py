
N = int(input())
heap = []

# heap 에 데이터를 삽입한다. 
def heappush(heap,data):
  heap.append(data)
  # 추가한 원소의 인덱스를 구한다.
  current = len(heap) - 1
  # 현재 원소가 루트(인덱스 0)에 도달하면 종료
  while current > 0:
      # 추가한 원소의 부모 인덱스를 구한다.
      parent = (current - 1) // 2
      if heap[parent] > heap[current]:
          heap[parent], heap[current] = heap[current], heap[parent]
          # 추가한 원소의 인덱스를 갱신한다.
          current = parent
      else:
          break
    

# heap 에서 루트노드의 값을 꺼낸 후 삭제 
def heappop(heap):
  if not heap:
      return 0
  elif len(heap) == 1:
      return heap.pop()
  
  pop_data, heap[0] = heap[0], heap.pop()
  current, child = 0, 1
  while child < len(heap):
      sibling = child + 1
      if sibling < len(heap) and heap[child] > heap[sibling]:
          child = sibling
      if heap[current] > heap[child]:
          heap[current], heap[child] = heap[child], heap[current]
          current = child
          child = current * 2 + 1
      else:
          break
  return pop_data

# 배열 x를 힙 구조로 만든다 
def heapify(arr):
  current = start = len(arr)-1
  while start > 0:
      is_swaped = False
      while current > 0:
          parent = (current - 1) // 2
          if arr[parent] > arr[current]:
              arr[parent], arr[current] = arr[current], arr[parent]
              current = parent
              is_swaped = True
          else:
              break
      if is_swaped:
          current = start
      else:
          current = start = current - 1


for _ in range(N):
  x = int(input())
  if x == 0:
      print(heappop(heap))
  else:
      heappush(heap, x)