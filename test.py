def isDigArti(arti, isDig):
    xmin, ymin, xmax, ymax = arti
    for i in range(xmin, xmax+1):
        for j in range(ymin, ymax+1):
            if isDig[i][j] == False:
                return False
    return True

from collections import Counter, defaultdict
def digArtifacts(n: int, artifacts: list, dig: list) -> int:
    isDig = [[False] * n for _ in range(n)]
    for i,j in dig:
        isDig[i][j] = True
    res = 0
    for arti in artifacts:
        if isDigArti(arti, isDig):
            res += 1
    return res

n = 2
artifacts = [[0,0,0,0],[0,1,1,1]]
dig = [[0,0],[0,1]]
print(digArtifacts(n, artifacts, dig))


