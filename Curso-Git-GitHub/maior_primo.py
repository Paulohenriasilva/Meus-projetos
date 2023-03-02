def maior_primo(n):
    numero = n
    while numero > 1:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                # print(numero)
                # print(divisor)
                # print(range(2, numero))
                numero -=1
        # print(numero+1)
        return numero+1

# maior_primo(100)