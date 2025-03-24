class Query:
    def __init__(self, type, str=None, index=None):
        self.type = type
        self.str = str
        self.index = index

class QueryProcessor:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elements = [[] for _ in range(bucket_count)]

    def hash_function(self, s):
        x = 263
        p = 1000000007
        hash_value = 0
        for c in reversed(s):
            hash_value = (hash_value * x + ord(c)) % p
        return hash_value % self.bucket_count

    def read_data(self):
        query_type = input()
        if query_type == "check":
            index = int(input())
            return Query(query_type, index=index)
        else:
            s = input()
            return Query(query_type, str=s)

    def write_data(self, was_found):
        print("yes" if was_found else "no")

    def process_query(self, query):
        if query.type == "check":
            if query.index < len(self.elements):
                print(" ".join(self.elements[query.index]))
        else:
            hash_index = self.hash_function(query.str)
            if query.type == "find":
                self.write_data(query.str in self.elements[hash_index])
            elif query.type == "add":
                if query.str not in self.elements[hash_index]:
                    self.elements[hash_index].insert(0, query.str)
            elif query.type == "del":
                if query.str in self.elements[hash_index]:
                    self.elements[hash_index].remove(query.str)

    def process_queries(self):
        n = int(input())
        queries = [self.read_data() for _ in range(n)]
        for query in queries:
            self.process_query(query)

if __name__ == "__main__":
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
