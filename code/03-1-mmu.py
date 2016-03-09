# mm manager, first_fit

occupied_space = dict()
free_space = dict()


def _mm_init():
    global free_space
    free_space = dict({0: 1024})
    global occupied_space
    occupied_space = dict()


def _free(start):
    if start in occupied_space:
        len = occupied_space[start]
        occupied_space.pop(start, None)
        free_space[start] = len
        s = start
        # merge
        for i in range(0, 1024):
            if i in free_space and free_space[i] + i == start:
                free_space[i] = free_space[i] + len
                free_space.pop(start, None)
                s = i
                break
        if (s + free_space[s]) in free_space:
            free_space[s] = free_space[s] + free_space[s + free_space[s]]
            free_space.pop(s + free_space[s], None)
        return len
    return -1


def _malloc(size):
    for i in range(0, 1024):
        if i in free_space and free_space[i] >= size:
            free_space[i + size] = free_space[i] - size
            free_space.pop(i, None)
            occupied_space[i] = size
            return i
    return -1


def main():
    _mm_init()
    start0 = _malloc(10)
    # len0 = _free(start0)
    print(start0)
    # print(len0)
    start1 = _malloc(20)
    # len1 = _free(start1)
    print(start1)
    # print(len1)
    start2 = _malloc(30)
    # len2 = _free(start2)
    print(start2)
    # print(len2)
    print(_free(start1))
    print(_free(start0))
    start3 = _malloc(25)
    print(start3)

if __name__ == "__main__":
    main()
