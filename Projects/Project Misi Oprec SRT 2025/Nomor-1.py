nilai = 0
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
n = int(input())
for i in range(1, n + 1, 1):
    cx = int(input())
    cy = int(input())
    r = int(input())

    # Masuk ke persamaan garis singgung lingkaran: Kx + Ly + M = 0
    x = x2 - x1
    y = y2 - y1
    k = y
    l = -x
    m = x2 * y1 - y2 * x1
    jarak = fabs(k * cx + l * cy + m) / sqrt(k ** 2 + l ** 2)
    if jarak <= r:
        nilai = nilai + 1
print(nilai)
