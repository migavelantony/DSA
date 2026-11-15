# LeetCode 1282: Group the People Given the Group Size They Belong To
# Source: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
#
# Problem summary (paraphrased):
# Each person specifies the size of their required group. Partition all person indices
# into groups of those exact sizes, assigning each person once. Any valid grouping is
# acceptable.

class Solution:

    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        d = {}
        nums = []
        for i, num in enumerate(groupSizes):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)
        for k in d.keys():
            value = d[k]
            if len(value) == k:
                nums.append(value)
            else:
                for i in range(0, len(value), k):
                    nums.append(value[i:i + k])
        return nums
