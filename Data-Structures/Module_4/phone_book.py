class Query:
    def __init__(self, type, number, name=None):
        self.type = type
        self.number = number
        self.name = name

def read_data():
    n = int(input())
    queries = []
    for _ in range(n):
        query = input().split()
        if query[0] == "add":
            queries.append(Query(query[0], int(query[1]), query[2]))
        else:
            queries.append(Query(query[0], int(query[1])))
    return queries

def write_response(result):
    for res in result:
        print(res)

def process_queries(queries):
    result = []
    contact_size = 10000000
    contacts = [""] * contact_size

    for query in queries:
        if query.type == "add":
            contacts[query.number] = query.name
        elif query.type == "del":
            contacts[query.number] = ""
        else:
            if contacts[query.number] == "":
                result.append("not found")
            else:
                result.append(contacts[query.number])

    return result

if __name__ == "__main__":
    write_response(process_queries(read_data()))
