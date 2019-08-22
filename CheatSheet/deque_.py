from collections import deque


def test_deque():
    d = deque([1, 2, 3, 4, 5, 6])
    a = d.pop()  # 有返回
    # d.remove(2)  # 无返回
    # d.rotate(1)
    print(d[0])
    print(a)
    d.append(12)
    print(d)
    # for elem in d:
    #     print(elem)
    # print(a)
    # print(d)


if __name__ == "__main__":
    test_deque()
