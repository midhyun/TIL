numbers = [1, 11, 110, 1110]
def solution(numbers):
    numbers = [*map(str, numbers)]
    numbers.sort(key = lambda x: x*3, reverse=True)
    answer = "".join(numbers) if numbers[0] != "0" else "0"
    return answer

print(solution(numbers))