def read_file(file):
    with open(file, "r") as f:
        line = f.readline().strip()
        arr = line.split()
        print(f"Parsed nums: num_1 = {arr[0]}, num_2 = {arr[1]}, steps = {arr[-1]}.")
    return arr

def recursive_fibonacci(arr, steps):
    fibonacci_array = [float(x) for x in arr]
    def recursive(arr, steps):
        if steps == 0:
            return

        next = arr[-2] + arr[-1]
        arr.append(next)

        recursive(fibonacci_array, steps - 1)

    recursive(fibonacci_array, steps)

    return fibonacci_array

def write_file(file, arr):
    with open("result.txt", "a") as f:
        f.write(str(arr))

if __name__ == '__main__':
    arr = read_file("nums.txt")
    steps = int(arr[-1])
    arr.remove(arr[-1])
    fibonacci_array = recursive_fibonacci(arr, steps)
    write_file("../result.txt", fibonacci_array)
    print(f"Result: {fibonacci_array}")

