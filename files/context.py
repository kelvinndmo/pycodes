with open('test.txt', 'r') as f:
    f.write('Test')
    # f_content = f.readlines()
    # print(f_content)

    # f = f.readline()
    # print(f, end='')
    # for line in f:
    #     print(line, end="")

    # content = f.read(10)
    # print(content)

    n_content = f.read(10)
    print(n_content, end="")

    f.seek(0)

    n_content = f.read(10)
    print(n_content)

    # size_to_read = 10
    # f_content = f.read(size_to_read)
    # while len(f_content) > 0:
    #     print(f_content, end="*")
    #     f_content = f.read(size_to_read)
