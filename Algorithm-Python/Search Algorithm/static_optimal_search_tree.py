# coding:utf-8
# Author: Neacik

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


def static_optimal_search_tree(arr, weight, low, high):
    if low > high:
        return None
    sw = []
    for i in range(low, high + 1):
        if i == low:
            sw.append(weight[i])
        else:
            sw.append(sw[(i - 1) - low] + weight[i])

    p = []
    for i in range(low, high + 1):
        if i == low:
            p.append(abs(sw[len(sw) - 1] - sw[i - low]))
        else:
            p.append(abs(sw[len(sw) - 1] - sw[i - low] - sw[i - 1 - low]))

    min = 0
    for i in range(len(p)):
        if p[i] < p[min]:
            min = i
    min = min + low
    return TreeNode(arr[min], static_optimal_search_tree(arr, weight, low, min - 1) \
                    , static_optimal_search_tree(arr, weight, min + 1, high))


if __name__ == "__main__":
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    weight = [1, 1, 2, 5, 3, 4, 4, 3, 5]
    root = static_optimal_search_tree(arr, weight, 0, 8)
    print(root._data)
