#point of sorting is to put things in order
#Bubble Sort
#index [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"self.inputlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]"

#Point of j and check for swap, is to run it multiple times until the self.inputlist is sorted instead of once,
class bubble:
    def __init__(self, p,):
        self._inputlist = list(map(int, p.split(",")))
        for j in range(len(self._inputlist)-1,0,-1):
            check_for_swap = False
            for i in range(j):
                if self._inputlist[i] > self._inputlist[i + 1]:
                    swap = self._inputlist[i]
                    self._inputlist[i] = self._inputlist[i +1]
                    self._inputlist[i + 1] = swap
                    check_for_swap = True
            if check_for_swap == False:
                    break
    @property
    def inputlist(self):
        return self._inputlist

if __name__ == "__main__":
    str = "10,9,8,7,6,5,4,3,2,1"
    bubble = bubble(str)
    print(bubble._inputlist)

