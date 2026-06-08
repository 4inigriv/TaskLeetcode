'''
f(e) = a -> dic_c = {e:a}
f(g) = d -> dic_g = {g :d}
egg = ada
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): #basic case
            return False 
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            if s[i] in dic_s:
                #mapear para o mesmo caractere de antes:
                if dic_s[s[i]] != t[i]:
                    return False
            else:
                dic_s[s[i]] = t[i]
            if t[i] in dic_t:
                if dic_t[t[i]] != s[i]: #dic_t[[i]] tradution
                    return False
            else:
                dic_t[t[i]] = s[i] # e : a
        return True

                
