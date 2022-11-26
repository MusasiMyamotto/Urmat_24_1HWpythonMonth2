def binary_search(arr, low, high, x):
  if high >= low:
    mid = (high + low) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binary_search(arr, low, mid - 1, x)
    else:
      return binary_search(arr, mid + 1, high, x)
  else:
    return -1
arr = list(range(1, 100))
x = 41
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
  print("елемент под индексом номер", str(result))
else:
  print("елемент отсутствует в списке")




def bubbleSort(arr):
  n = len(arr)
  swapped = False
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        swapped = True
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if not swapped:
      return

arr = [64, 34, 25, 12, 22, 11, 90, 23, 567, 234, 890]

bubbleSort(arr)

print("отсортированный список:")
for i in range(len(arr)):
  print("% d" % arr[i], end=" ")