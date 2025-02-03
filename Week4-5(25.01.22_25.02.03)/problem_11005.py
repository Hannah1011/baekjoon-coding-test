if __name__ == '__main__':
    N, B = map(int, input().split())

    # string.index() gives the index location -> Z: 35 as required
    number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''  # initialize empty string for answer notation

    while N:
        s += number[N % B]
        N //= B

    print(s[::-1])