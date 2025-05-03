# Lucien Sevault Wolber - CUPGE2
# TP de SNR - Caching

# Import des modules numpy et matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt


# Fonction Zipf
def Zipf(alpha=1.2, R=10, N=10):
    ranked_items = np.arange(1, R+1)
    probs = [1.0 / (rank**alpha) for rank in ranked_items]
    probs /= sum(probs)

    sequence = np.random.choice(ranked_items, size=N, p=probs, replace=True)

    return sequence


# Implémentation de la politique LRU
class LRU:
    def __init__(self, length, cache=[]):
        self.cache = cache
        self.length = length
        self.hit = 0
        self.N = 0

    def maj(self, el):
        if len(self.cache) < self.length:
            self.cache.append(el)
        else:
            self.N += 1
            if el not in self.cache:
                self.cache.pop(0)
            else:
                self.hit += 1
                self.cache.remove(el)
            self.cache.append(el)

    def test_sequence(self, sequence: list[int]):
        for element in sequence:
            self.maj(element)
        return self.hit/self.N


def last_occ(cache, sequence, k):
    res = []
    for i in range(1, len(cache)):
        if cache[i] not in sequence[k:]:
            res.append(-1)
        res.append(sequence[k:].index(cache[i]))


# Implémentation de la politique Min
class Min:
    def __init__(self, length, cache=[]):
        self.cache = cache
        self.length = length
        self.hit = 0
        self.N = 0

    def maj(self, i, el):
        if len(self.cache) < self.length:
            self.cache.append(el)
        else:
            self.N += 1
            if el not in self.cache:
                pred = last_occ(self.cache, sequence, i)
                if -1 in pred:
                    self.cache.pop(pred.index(-1))
                else:
                    self.cache.pop(pred.index(max(pred)))
                self.cache.append(el)
            else:
                self.hit += 1

    def test_sequence(self, sequence: list[int]):
        for i in range(len(sequence)):
            self.maj(i, sequence[i])
        return self.hit/self.N


def test_param(alpha, taille_librairie, taille_cache, pol, N=10):
    probs = []
    print(taille_cache)
    print(taille_librairie)
    for i in range(N):
        cache = LRU(taille_cache)
        probs.append(cache.test_sequence(Zipf(alpha=alpha, R=taille_librairie, N=10*taille_cache)))
    x = sum(probs)/N
    sigma = np.sqrt(sum([(prob - x)**2 for prob in probs])/N)
    IC = [x - 1.96*sigma/np.sqrt(N), x + 1.96*sigma/np.sqrt(N)]
    return x, IC, probs


cache = LRU(3, cache=[3, 2, 1])
sequence = [4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3]
cout = cache.test_sequence(sequence)
print(cout)

probs = []
IC = []
echs = []
taille_librairie = 1000
taille_cache = taille_librairie//10
for alpha in [0.8, 1.0, 1.2]:
    prob, IC, ech = test_param(alpha, taille_librairie, taille_cache, LRU)
    print(prob, IC)
    probs.append(prob)
    echs.append(ech)
plt.figure()
# plt.plot([0.8, 1.0, 1.2], probs)
plt.boxplot(echs, labels=[0.8, 1.0, 1.2])
plt.show()

probs = []
IC = []
echs = []
alpha = 1.0
for taille_librairie in [100, 1000, 10000]:
    taille_cache = taille_librairie//100
    prob, IC, ech = test_param(alpha, taille_librairie, taille_cache, LRU)
    print(prob, IC)
    probs.append(prob)
    echs.append(ech)
plt.figure()
# plt.plot([100, 1000, 10000], probs)
plt.boxplot(echs, labels=[100, 1000, 10000])
plt.show()

probs = []
IC = []
echs = []
alpha = 1.0
taille_librairie = 1000
for taille_cache in [taille_librairie//x for x in [100, 10, 5]]:
    prob, IC, ech = test_param(alpha, taille_librairie, taille_cache, LRU)
    print(prob, IC)
    probs.append(prob)
    echs.append(ech)
plt.figure()
# plt.plot([taille_librairie/x for x in [100, 10, 5]], probs)
plt.boxplot(echs, labels=[taille_librairie/x for x in [100, 10, 5]])
plt.show()
