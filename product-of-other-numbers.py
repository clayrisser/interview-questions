def main():
    numbers = [1, 7, 3, 4]
    print('product_of_other_numbers1')
    product = product_of_other_numbers1(numbers)
    print(product)

# O(n^2) time
# O(1) space
def product_of_other_numbers1(numbers):
    answer = list()
    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers) - 1):
            product *= numbers[mod(i + 1 + j, len(numbers))]
        answer.append(product)
    return answer

def mod(i, length):
    return i if i < length else i % length

main()
