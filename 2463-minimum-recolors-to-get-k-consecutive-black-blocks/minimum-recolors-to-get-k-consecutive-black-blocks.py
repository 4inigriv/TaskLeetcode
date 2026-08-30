class Solution(object):
    def minimumRecolors(self, blocks, k):
        #preciso de um set p ser consecutivo? guardar index?
        trocas = 0
        count = 0
        mintrocas = float('inf')  # <- começa com infinito, não 0!
        for i in range(len(blocks)- k + 1): #len(blocks) - k + 1 garante que cada janela tem exatamente k elementos.
        #trocas
            trocas = 0
            #conta a quantidade de W q tem nessa janela 
            for j in range(i, i+k): #1 ate 1+2 ate 3 janela q cresce
                if blocks[j] == 'W':
                    trocas += 1 #quantas trocas vai precisar fazer?
            #como achar o minimo?
            mintrocas = min(mintrocas,trocas)
        return mintrocas




        