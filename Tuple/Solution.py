if __name__ == '__main__':
    n = (input())
    integer_list = map(int, input().split())
    a = tuple(integer_list)
    print(hash(a))