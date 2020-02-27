import time
import math


class Tribonachi:
    def __init__(self, length):
        self.length = length
        self.seq = [0, 0, 1]

    def __iter__(self):

        for i in range(self.length):
            if i == 0:
                ret = self.seq[0]
            elif i == 1:
                ret = self.seq[1]
            elif i == 2:
                ret = self.seq[2]
            else:
                k = len(self.seq)
                self.seq.append(self.seq[k-3] + self.seq[k-1] + self.seq[k-2])
                ret = self.seq[k]
            yield ret


class Leibniz:
    """If """
    def __init__(self, sum):
        self.current_sum = 0
        self.seq = []
        self.res_sum = sum

    def __iter__(self):
        n = 0
        while round(self.current_sum, 2) != self.res_sum:
            cur = ((-1)**n)/(2*n+1)
            self.current_sum += cur
            n += 1
            if n == 100:
                print("There are impossible to get given number")
                break
            yield cur


def main():
    # tri_iter = Tribonachi(10)
    # for num in tri_iter:
    #     print(num)

    leibniz_iter = Leibniz(0.88)
    for num in leibniz_iter:
        print(num)



if __name__ == '__main__':
    main()
