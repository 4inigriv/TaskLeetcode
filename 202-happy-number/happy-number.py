'''
n = 19
ultimo= n % 10
primeiro = n // 10 
resultado = primeiro * primeiro + ultimo * ultimo
print(resultado)
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            resultado = 0
            while n > 0:
                digito = n % 10
                resultado += digito * digito
                n //= 10

            n = resultado

        return True