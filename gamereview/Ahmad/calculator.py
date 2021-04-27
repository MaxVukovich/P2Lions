import random


class Games:
    """Initializer of class takes k parameter and returns Class Object"""
    def __init__(self, k):
        """Built in validation and exception"""
        if k < 0 or k > 6:
            raise ValueError("k must be between 2 and 10")
        self._k = k
        self._list = []
        self._games = ["Fortnite,", "Minecraft", "Overwatch", "Sub-Rosa", "Cold War", "Fall Guys", "Warzone", "MW2"]
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.game_k()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def game_k(self):
        f = [(random.sample((self._games), k=self._k))]  # fibonacci starting array/list
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
    k = 3
    '''Constructor of Class object'''
    gamerecs = Games(k)
    print(f"Here are some game recomendations = {gamerecs.list}")

#for i in range(a):
#print(f"Listing of Book Recs {i}= {bookrecs.get_sequence(i)}")