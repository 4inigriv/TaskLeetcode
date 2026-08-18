class Solution(object):
    def largestInteger(self, nums, k):
        # Dicionário para contar: {número: quantas janelas aparece}
        contagem = {}
        primeira_janela = nums[0:k]
        for numero in set(primeira_janela):  # set() remove duplicatas
            contagem[numero] = 1
        janela_atual = primeira_janela
        
        for i in range(k, len(nums)):
            # deslizando
            janela_atual.pop(0)
            janela_atual.append(nums[i])
            # deslizando
            for numero in set(janela_atual):
                contagem[numero] = contagem.get(numero, 0) + 1
        quase_ausentes = []
        for numero, vezes in contagem.items():
            if vezes == 1: 
                quase_ausentes.append(numero)
        if quase_ausentes:
            return max(quase_ausentes)
        else:
            return -1