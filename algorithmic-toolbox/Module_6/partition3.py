from itertools import accumulate

def partition_search(A, index, partitions, target):
    if index >= len(A):
        return True
    for i in range(len(partitions)):
        if partitions[i] + A[index] <= target:
            partitions[i] += A[index]
            if partition_search(A, index + 1, partitions, target):
                return True
            partitions[i] -= A[index]
    return False

def partition3(A):
    total = sum(A)
    if total % 3 != 0 or len(A) < 3 or max(A) > total // 3:
        return False
    
    A.sort(reverse=True)
    partitions = [0] * 3
    return partition_search(A, 0, partitions, total // 3)

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().split()))
    print(1 if partition3(A) else 0)
