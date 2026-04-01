import csv
import os

class MemoryScan(object):
    """
    Yield all records from the given "table" in memory.

    This is really just for testing... in the future our scan nodes
    will read from disk.
    """
    def __init__(self, table):
        self.table = table
        self.idx = 0

    def next(self):
        if self.idx >= len(self.table):
            return None

        x = self.table[self.idx]
        self.idx += 1
        return x
    
class FileScan(object):
    def __init__(self, path, schema):
        self.file = open(path, 'r')
        self.reader = csv.reader(self.file)
        self.schema = schema
        next(self.reader)
    
    def next(self):
        try:
            return tuple(t(v) for t, v in zip(self.schema, next(self.reader)))
        except StopIteration:
            self.file.close()
            return None

class Projection(object):
    """
    Map the child records using the given map function, e.g. to return a subset
    of the fields.
    """
    def __init__(self, proj):
        self.proj = proj

    def next(self):
        x = self.child.next()
        if x is None:
            return None
        return self.proj(x)


class Selection(object):
    """
    Filter the child records using the given predicate function.

    Yes it's confusing to call this "selection" as it's unrelated to SELECT in
    SQL, and is more like the WHERE clause. We keep the naming to be consistent
    with the literature.
    """
    def __init__(self, predicate):
        self.predicate = predicate

    def next(self):
        while True:
            x = self.child.next()
            if x is None or self.predicate(x):
                return x


class Limit(object):
    """
    Return only as many as the limit, then stop
    """
    def __init__(self, n):
        self.remaining = n

    def next(self):
        if self.remaining == 0:
            return None
        self.remaining -= 1
        return self.child.next()


class Sort(object):
    """
    Sort based on the given key function
    """
    def __init__(self, key, desc=False):
        self.key = key
        self.desc = desc
        self.tuples = None
        self.idx = 0

    def next(self):
        if self.tuples is None:
            self.tuples = []
            while True:
                x = self.child.next()
                if x is None:
                    break
                self.tuples.append(x)
            self.tuples.sort(key=self.key, reverse=self.desc)
       
        if self.idx >= len(self.tuples):
            return None
        
        x = self.tuples[self.idx]
        self.idx += 1
        return x


def Q(*nodes):
    """
    Construct a linked list of executor nodes from the given arguments,
    starting with a root node, and adding references to each child
    """
    ns = iter(nodes)
    parent = root = next(ns)
    for n in ns:
        parent.child = n
        parent = n
    return root


def run(q):
    """
    Run the given query to completion by calling `next` on the (presumed) root
    """
    while True:
        x = q.next()
        if x is None:
            break
        yield x


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'movies.csv')

    test_schema = (int, str, str)
    test_movies = Q(
            # Limit(10),
            Projection(lambda x: (x[1])),
            Selection(lambda x: x[0] == 5000),
            FileScan(path, test_schema)
        )
    assert (tuple(run(test_movies))) == ('Medium Cool (1969)',)
    print("OK")