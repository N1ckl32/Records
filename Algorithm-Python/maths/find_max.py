# coding:utf-8
# Author: Neacik

def find_max(nums):
    max_mum = nums[0]
    for x in nums:
        if x > max_mum:
            max_mum = x
    return max_mum


def main():
    print(find_max([0, 2, 34, 5, 8, 89, 22]))


if __name__ == "__main__":
    main()
