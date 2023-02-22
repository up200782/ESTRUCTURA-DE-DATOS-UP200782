def main():
    arr_int = []
    n = int(input("Ingrese el número de elementos: "))
    for i in range(n):
        while True:
            try:
                element = input(f"Ingrese el elemento {i+1}: ")
                if element == "":
                    raise ValueError
                arr_int.append(int(element))
                break
            except ValueError:
                print("Ingrese un número entero válido.")
    print("Lista antes de ordenar:")
    print(arr_int)
    print("Lista después de ordenar:")
    print(quicksort(arr_int))

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    main()