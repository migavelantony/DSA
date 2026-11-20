# LeetCode 2379: Minimum Recolors to Get K Consecutive Black Blocks
# Source: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
#
# Problem summary (paraphrased):
# Each operation changes one white block into a black block. Find the fewest operations
# required to obtain a contiguous run of at least k black blocks.

class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        sub_array = {'W': 0, 'B': 0}
        for i in range(k):
            block = blocks[i]
            sub_array[block] += 1
        min_count = sub_array['W']
        for i in range(k, len(blocks)):
            outgoing = blocks[i - k]
            sub_array[outgoing] -= 1
            block = blocks[i]
            sub_array[block] += 1
            count = sub_array['W']
            if count < min_count:
                min_count = count
        return min_count
