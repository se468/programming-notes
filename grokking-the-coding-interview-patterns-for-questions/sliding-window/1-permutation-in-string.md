# Permutation in a String (hard)
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, "abc" has the following six permutations:
```
abc
acb
bac
bca
cab
cba
```
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:
```
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
```

# Solution
1. Create HashMap to store frequencies of all chars
2. Iterate string adding one char at a time in sliding window
3. If char exists in HashMap: decrement its frequency in map
4. If char frequency become zero: complete match
5. If at any time, num chars matched == num distinct chars in pattern - return True
6. If window size > length of pattern - shrink window to make it equal to size of pattern. 
7. At the same time, if char going out was part of pattern, put it back in frequency HashMap.

```python
def find_permutation(str, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False
```