'''
1-> pegar a soma q é mais vantajosa 
2-> pega o maior numeor da lista e tenta ve se da p pegar ele de graça

'''
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        pay = []
        cost.sort()
        cost = cost[::-1] #bigger to smaller
        if len(cost) <= 2:#basic case -> [5,5] = 10
            return sum(cost)
        for i in range(len(cost)):
            if i % 3 != 2:
                pay.append(cost[i]) #take pay
        return sum(pay)
            

        