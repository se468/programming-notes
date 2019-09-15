Reusing the window elements and subtracting one going out, adding one coming in.

```
Getting sum of every 5 elements:

[1,2,3,4,5,6,7,8,9,10]
  ------
    ->
   slide window

1+2+3+4 = 10

[1,2,3,4,5,6,7,8,9,10]
   ------
     ->

1 goes out, 5 comes in.

10 - 1 + 5 = 14

result:
[10, 14, ...] so on
```

Time complexity will reduce to O(N), whereas brute force of finding sum all the time will be O(N * K).