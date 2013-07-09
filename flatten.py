# Flattens nested tables into single level
__author__ = 'rbd'

import operator

class Table:
    def __init__(self, rows=5, cols=5, zeroelem=None):
        self.value = [[]]
        self.rows = rows
        self.cols = cols

        if zeroelem:
            row = ['---'.format(i) for i in range(self.cols)]
            self.value = [['---'.format(i, x) for x in row] for i in range(self.rows)]
            self.value[0][0] = zeroelem
        else:
            row = ['C{}'.format(i) for i in range(self.cols)]
            self.value = [['R{}{}'.format(i, x) for x in row] for i in range(self.rows)]

    def append(self, value):
        print('value before appending %s' % str(value))
        print(self)
        self.value.append(value)
        print('value after appending %s' % str(value))
        print(self)

    def extend(self, value, newrows, newcols):
        # if newrows is None or newrows <= self.rows:
        #     newrows = self.rows
        #
        # if newcols is None or newcols <= self.rows:
        #     newcols = self.cols

        print value

        for i in range(newrows):
            for j in range(newcols):
                if j > value.cols:
                    value.value[i].append('---')
            if i > value.rows:
                value.value.append(['---']*newcols)

        # self.rows = newrows
        # self.cols = newcols

        print value

        return value

    def flatten(self):
        rows, cols = self.len()

        for i in range(self.rows):
            for j in range(self.cols):
                v = self.value[i][j]
                if isinstance(v, Table):
                    self.value[i][j] = self.extend(value=v, newrows=rows, newcols=cols)
                    # print('extended')
                else:
                    val = self.value[i][j]
                    # print(val)
                    self.value[i][j] = Table(rows, cols, val)

        value = []
        print(rows, cols)
        for row in self.value:
            for i in range(rows):
                value.append([col.value[i] for col in row])

        return [reduce(operator.add, x, []) for x in value]

    def len(self, value=None):
        if value is None:
            value = self.value
            first = True
        else:
            first = False
        ls = []
        i, j = 0, 0
        for row in value:
            i += 1
            j = 0
            for col in row:
                j += 1
                if isinstance(col, Table):
                    ls.append(self.len(col.value))
        if first:
            ls.append((1, 1))
        else:
            ls.append((i, j))

        return max([x[0] for x in ls]), max([x[1] for x in ls])

    def __len__(self):
        return sum(self.len(self.value))

    def repr(self):
        value = self.flatten()
        row_format = "{:<5}" * len(value[0])
        n = lambda x: '\n'.join(x)
        return n([row_format.format("", *x) for x in value])

    def __repr__(self):
        # return self.repr()
        return str(self.value)


def main():
    a = Table(4, 3)

    # print(len(a))
    print(a.len())

    # b = Table(3, 3)
    # a.value[1][1] = b

    # print(len(a))
    # print(a.len())

    c = Table(2, 2)
    a.value[1][2] = c

    # print(len(a))
    print(a.len())

    print(a)




    # print(a)
    # print(b)

    return

    a.value = [[1, 'R1C2', 3]]


    b = ['R2C1', 'R2C2', 'R2C3']

    a.append(b)
    a.append(b)

    a.value[1][2] = b
    a.value[2][2] = 'a'

    # print(a.value[1][2])
    # print(a.value[2][2])

    print(a)


def valtest():
    x = 1
    y = 2
    z = 3
    a = [x, y, z]

    a.append(y)
    a.append(y)
    a[3] = x


    print(a)


if __name__ == "__main__":
    main()
    # valtest()
