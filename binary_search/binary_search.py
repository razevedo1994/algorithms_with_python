def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            hight = mid - 1

        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    x = binary_search([1, 3, 5, 7, 9], 3)
    y = binary_search([1, 3, 5, 7, 9], -1)
    print(x)
    print(y)
