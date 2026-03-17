class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Step 1: Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Sort based on frequency (descending)
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Step 3: Return top k elements
        return sorted_nums[:k]
        