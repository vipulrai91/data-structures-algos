# Validate Subsequence

### Understanding the problem

# We are given two arrays of integers `array` and `sequence`. We are asked to implement a
# function that is going to check whether all the numbers in the `sequence` appear in the `array`
#  and they appear in the same order. In other words, the function needs to find out if we can get
# the `sequence` array from the `array`, when we delete some or no elements in the `array` without
# changing the order of the remaining elements.

# Example:

# ```
array = [3, 1, 7, 5, 10, 2]
sequence = [1, 5, 2]
# Output: true
# ```

# #


class ValidateSubsequence:
    def __init__(self, array, sequence) -> None:
        self.array = array
        self.sequence = sequence
        self.isValidSubsequence = self.isValidSubsequence()

    def isValidSubsequence(self):
        arrIdx = 0
        seqIdx = 0

        while arrIdx < len(array) and seqIdx < len(sequence):
            if array[arrIdx] == sequence[seqIdx]:
                seqIdx += 1
            arrIdx += 1
        return seqIdx == len(sequence)


vsq = ValidateSubsequence(array=array, sequence=sequence)
print(vsq.isValidSubsequence)
