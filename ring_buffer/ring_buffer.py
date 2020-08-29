class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # create a list to store the items
        self.list_items = []
        # set the first index
        self.index = 0

    def append(self, item):
        # append an element by overriding the oldest element
        # if the list doesn't reach the full capacity then add the element to the end of the list
        if len(self.list_items) != self.capacity:
            self.list_items.append(item)
        # if the list reaches its full capacity
        else:
            self.list_items[self.index] = item
        self.index = (self.index + 1) % self.capacity


    def get(self):
        return self.list_items