import math

def function_a(numerator, denominator):
    # 找到最大公约数
    # cari fpb (faktor persekutuan terbesar)
    gcd = math.gcd(numerator, denominator)
    
    # 简化分数
    # simplifikasi pecahan
    numerator //= gcd
    denominator //= gcd
    
    # 检查分母是否为完全平方
    # cek kalau denominator adalag kuadrat sempurna
    root = int(math.sqrt(denominator))
    if root * root == denominator:
        # If it is, simplify further
        numerator *= root
        denominator = root
    
    return numerator, denominator

# 示例:
# contoh:
# num, den = 8, 18
# simplified_num, simplified_den = simplify_fraction_to_root(num, den)
# print(f"{num}/{den} simplified to {simplified_num}/√{simplified_den}")
