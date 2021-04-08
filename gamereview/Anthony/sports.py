import random


class Sports:
    """Initializer of class takes k parameter and returns Class Object"""
    def __init__(self, k):
        """Built in validation and exception"""
        if k < 0 or k > 6:
            raise ValueError("k must be between 2 and 10")
        self._k = k
        self._list = []
        self._sports = ["Soccer,", "Football", "Swimming", "Baseball", "Basketball", "Rugby", "Golf", "UFC"]
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.sport_k()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def sport_k(self):
        f = [(random.sample((self._sports), k=self._k))]  # fibonacci starting array/list
        self.set_data(f[0])
        f = [f[0]]


    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    """Getters with decorator to allow . notation access"""
    @property
    def k(self):
        return self._k

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Value for testing'''
    k = 2
    '''Constructor of Class object'''
    sportrecs = sports(k)
    print(f"Here are some sport recommendations = {sportrecs.list}")

#for i in range(a):
#print(f"Listing of Book Recs {i}= {bookrecs.get_sequence(i)}")