from collections import Counter


class Permutations:
    def __init__(self, s) -> None:
        self.s = list(s)
        self.n = len(self.s)
        self.res = []
        self.temp = []
        self.c = Counter(self.s)

    # Finding all the permutations , TC = O(n! * n) without using map
    def without_repetitions(self):
        if len(self.temp) == self.n:
            self.res.append(self.temp[:])
            return
        for k, v in self.c.items():
            if v > 0:
                self.c[k] -= 1
                self.temp.append(k)
                self.without_repetitions()
                self.c[k] += 1
                self.temp.pop()

    # Finding all the permutations , TC = O(n! * n) without using map
    def with_repetitions(self, x=0):
        if x == self.n:
            self.res.append(self.s[:])
            return
        for i in range(x, self.n):
            self.s[x], self.s[i] = self.s[i], self.s[x]
            self.with_repetitions(x + 1)
            self.s[i], self.s[x] = self.s[x], self.s[i]

    def get_result(self):
        return self.res

    def clear(self):
        self.res = []


solve = Permutations(input())
solve.without_repetitions()
print(solve.get_result())
solve.clear()
solve.with_repetitions()
print(solve.get_result())
