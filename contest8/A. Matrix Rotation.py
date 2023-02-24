    t = int(input())
    for _ in range(t):
        ans = "NO"
        matrix = [list(map(int, input().split())) for _ in range(2)]
        def check(matrix):
            if (matrix[0][0] < matrix[0][1] and matrix[1][0] < matrix[1][1] and
                matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1]):
                return True
            return False
        def rotate(matrix):
                matrix = [[matrix[1][0], matrix[0][0]], [matrix[1][1], matrix[0][1]]]
                return matrix
        i = 0
        while i < 4:
            if check(matrix):
                ans = "YES"
                break
            matrix = rotate(matrix)
            i+=1
        print(ans)
