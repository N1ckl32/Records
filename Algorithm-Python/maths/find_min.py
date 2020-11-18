# coding:utf-8
# Author: Neacik

def find_min(nums):
    min_nums = nums[0]
    for num in nums:
        if num < min_nums:
            min_nums = num
    return min_nums


def main():
    print(find_min([1, 2, 89, 65, 22, 33]))


if __name__ == "__main__":
    main()
