def main():
    N = int(input())

    tmp = [i for i in range(1, N+1)if not (i % 3 == 0 or i % 5 == 0)]
    print(sum(tmp))


if __name__ == '__main__':
    main()
