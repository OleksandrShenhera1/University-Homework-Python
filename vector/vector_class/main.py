
def read_file(file):
    with open(file, "r") as line:
        lines = line.readlines()
        vec1 = [float(x) for x in lines[0].strip().split()]
        vec2 = [float(x) for x in lines[1].strip().split()]

    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be the same length.")
    return vec1, vec2

class VectorCalculator:
    def __init__(self, vec1):
        self.vec1 = vec1

    def add_vector(self, vec2):
        new_vector = []
        n = len(self.vec1)
        for i in range(n):
            new_vector.append(self.vec1[i] + vec2[i])

        return new_vector

    def subtract_vector(self, vec2):
        new_vector = []
        n = len(self.vec1)
        for i in range(n):
            new_vector.append(self.vec1[i] - vec2[i])

        return new_vector

    def scalar_vector(self, vec2):
        result = 0
        n = len(self.vec1)
        for i in range(n):
            result += self.vec1[i] * vec2[i]
        return result

    def multiply_vector(self, vec2):
        new_vector = []
        n = len(self.vec1)
        for i in range(n):
            new_vector.append(self.vec1[i] * vec2[i])
        return new_vector

    def divide_vector(self, vec2, num):
        new_vector1 = []
        new_vector2 = []
        n = len(self.vec1)
        for i in range(n):
            new_vector1.append(self.vec1[i] / num)
            new_vector2.append(vec2[i] / num)
        return new_vector1, new_vector2


def user_input():
    while True:
        try:
            num = float(input("enter number to divide: "))
            if num != 0:
                return num
            else:
                print("enter number greater or lower than 0.")
        except ValueError:
            print("Enter <float, or int> type, try again.")

if __name__ == "__main__":
    vec1, vec2 = read_file("vector_nums.txt")
    user = user_input()
    my_vector = VectorCalculator(vec1)

    results = {
        "added_vector": my_vector.add_vector(vec2),
        "subtracted_vector": my_vector.subtract_vector(vec2),
        "scalar_vector": my_vector.scalar_vector(vec2),
        "multiplied_vector": my_vector.multiply_vector(vec2),
        "divided_vector": my_vector.divide_vector(vec2, 2)
    }

    with open("vector_output.txt", "w") as w:
        for key, value in results.items():
            w.write(f"{key}: {value}\n")
