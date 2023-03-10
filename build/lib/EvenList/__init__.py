class EvenList:
    def __init__(self, list):
        self.list = list
    def even(self):
        even_list = []
        for i in self.list:
            if i % 2 == 0:
                even_list.append(i)
        return even_list

list = EvenList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list.even())    