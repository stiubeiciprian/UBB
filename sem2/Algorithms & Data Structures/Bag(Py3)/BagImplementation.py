class BagElem():

    def __init__(self, elem):
        self.__elem = elem
        self.__freq = 1

    def increaseFreq(self):
        self.__freq += 1

    def decreaseFreq(self):
        self.__freq -= 1

    def getElem(self):
        return self.__elem

    def getFreq(self):
        return self.__freq

    def __eq__(self, other):
        if self.__elem == other:
            return True
        return False

    def __repr__(self):
        return str(self.getElem()) + " - " + str(self.getFreq())


class Bag:

    # creates a new, empty Bag
    def __init__(self):
        self.__elems = []
        self.__iterator = BagIterator(self)

    # adds a new element to the Bag
    def add(self, e):
        # O(n)

        for elem in self.__elems:
            if e == elem:
                elem.increaseFreq()
                return

        self.__elems.append(BagElem(e))

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        # O(n)
        for i in range(len(self.__elems)):
            if self.__elems[i] == e:
                self.__elems[i].decreaseFreq()
                if self.__elems[i].getFreq() <= 0:
                    self.__elems.pop(i)
                return True

        return False

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        # O(n)
        for elem in self.__elems:
            if e == elem:
                return True
        return False

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        # O(n)
        for elem in self.__elems:
            if e == elem:
                return elem.getFreq()
        return 0

    # returns the size of the Bag (the number of elements)
    def size(self):
        # theta(n)
        sizeOfBag = 0
        for elem in self.__elems:
            sizeOfBag += elem.getFreq()

        return sizeOfBag

    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        # theta(1)
        if len(self.__elems) == 0:
            return True

        return False

    # returns a BagIterator for the Bag
    def iterator(self):
        # theta(1)
        return self.__iterator


class BagIterator:

    #creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        self.__currentPos = 0
        self.__currentCounter = 1
        self.__bag = b


    # returns True if the iterator is valid
    def valid(self):
        # theta(1)
        if self.__currentPos < len(self.__bag._Bag__elems):
            return True
        return False

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        #theta(1)

        if self.valid() is False:
            raise ValueError()

        return self.__bag._Bag__elems[self.__currentPos].getElem()

    # moves the iterator to the next element
    #throws ValueError if the iterator is not valid
    def next(self):
        # theta(1)

        if self.valid() is False:
            raise ValueError()

        self.__currentCounter += 1

        if self.__currentCounter > self.__bag._Bag__elems[self.__currentPos].getFreq():
            self.__currentPos += 1
            self.__currentCounter = 1


    # sets the iterator to the first element from the Bag
    def first(self):
        # theta(1)
        self.__currentPos = 0
        self.__currentCounter = 1
