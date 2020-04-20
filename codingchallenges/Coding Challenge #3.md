Coding Challenge #3
--  
Welcome back, to another coding challenge! I hope you have fun with today's. I think it's much simpler and shorter, and just requires some amount of creativity. Credit belongs to @Fifkee for sharing this challenge with me!

 As usual, same requirements:
* Has to be written in Lua 5.1 (the version roblox uses)
* The program has to be compatible with Roblox Studio, meaning you can’t use features vanilla Lua has but rbxlua disabled
* You can’t use httpservice to cheat the challenge
---
Let's say we have an array `A`.

We define `S` to be a *subarray* of `A` if contains some elements that also exist in `A`.

We define `S` to be a *continuous subarray* of `A`, if it is a *subarray* of `A`, and staisfies the condition: `S[1]` , `S[2]` , `...` , `S[n] = A[i]` , `A[i + 1]` , `...` , `A[i + n - 1]` for some index `i`. An array has multiple *continuous arrays*.

For this challenge, you need to create a function `subarrays`, which takes an array as input, and return a table containing all of the array's *continuous subarrays*.

Wait... What? Well the first part is simple, but what about the *continuous subarray*? I think giving an example is the best way to explain it.

Let `A` be `{1, 2, 3}`, the continuous subarrays of `A` would be `{1}`, `{2}` , `{3}` , `{1, 2}` , `{2, 3}` and `{1, 2, 3}`.

Let `A` be `{1, 2, 3, 4}`, the continuous subarrays of `A` would be `{1}`, `{2}` , `{3}` , `{4}`, `{1, 2}` , `{2, 3}`, `{3, 4}`, `{1, 2, 3}`, `{2, 3, 4}` and `{1, 2, 3}`.

![codingchallenge3-1|388x207](upload://yJPCIMmJ6UGg9blVNZoEwEqh6Sd.png) 

Basically, you need to make all possible subarrays using initial array A's elements that have a length of 1, and all subarrays that have a length of 2, where the elements of each subarray are next to each other (e.g `{1, 3}` isn't correct, because 1 and 3 aren't next to each other) ect.


[details="The answer is here, don't spoil yourself!"]
Basically, the way this will work is, we will loop through the array, and for each element, using the fact that `unpack(table, from, to)` has two optional argument; from where to start  and stop unpacking, we loop from that element to the next element, inserting those two into a subarray, then loop from the same element to the next next element ect. until the there are no elements, and we move to the second element, and do the same stuff.

![codingchallenge3-2|450x500](upload://4XVD9gsm7J9ruMMScoW3xL4eR96.png) 

```
local function subarrays(array) --array is the inputted array
    local subarrays = {} --this is the returned table
    for x, _ in pairs(array) do --loop through all elements
        for i = x, #array do --loop from the element's index, to the end of the list, i would be the current next element
            table.insert(subarrays, {unpack(array, x, i)}) --basically insert an array in the returned table of elements starting from the element and the current next element
       end
    end
    return subarrays --return
end

local A = {1,2,3,4,5} --an example

for i, v in pairs(subarrays(A)) do  
    print(string.format("{ %s }", table.concat(v, ", "))) --just a way to print the subarrays
end
```
Result:
![image|155x243](upload://7iok05UuAdd0RKoev9SpPliUxer.png) 
Note that order isn't needed.

[/details]
