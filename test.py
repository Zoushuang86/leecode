from collections import Counter
def maxInvestment(product: list, limit: int) -> int:
    product = sorted(product, reverse=True)
    product.append(0)
    n = len(product)
    res = 0
    i = 0
    price = product[0]
    while limit and price:
        k = product[i] - product[i + 1]
        if k < limit:
            res += (product[i] + product[i]) * k // 2
            product[i] = product[i + 1]
            price = product[i]
            if k == n:
                limit -= k-1
            else:
                limit -= k
        else:
            temp = product[i] + limit - 1
            res += (product[i] + temp) * limit // 2
            product[i] = temp
            price = temp
            limit = 0
        i = (i + 1) % (n - 1)
    return res % (pow(10, 8) + 7)

# 思维类似增加最小和，列表按照金额递增方便操作
def maxInvestment(product: list, limit: int) -> int:
    c = Counter(product)
    a = [[k, c[k]] for k in c]
    # 增加一个哨兵
    a.append([0, limit])
    a.sort(key=lambda x: x[0], reverse=False)
    res = 0
    p = 10 ** 9 + 7

    while limit > 0 and len(a) > 1:
        u = a[-1][0]
        v = a[-2][0]
        n = a[-1][1]
        if (u-v)*n >= limit:
            x, y = divmod(limit, n) # Return the tuple (x//y, x%y)
            ans += (u + u - x)


print(maxInvestment([2,1,3], 10))