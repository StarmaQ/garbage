Coding Challenge #2 
--

Welcome back, to the second coding challenge! I got positive feedback from the first one, so I'm excited to continue this. I decided to make this one a little bit easier, since last one was a little bit intimidating!

As usual, same requirements:
 *  Has to be written in Lua 5.1 (the version roblox uses)
* The program has to be compatible with Roblox Studio, meaning you can’t use features vanilla Lua has but rbxlua disabled
* New rule: you can't use httpservice to cheat the challenge

----
Today's challenge is gonna be very straight forward, implementing a **quick sort**. In computer science, students are introduced to sorting algorithms as head start. Many of [them](https://www.youtube.com/watch?v=JU767SDMDvA&list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl) exist, but quick sort is the most popular among them, mainly because it's the most efficient (average [time complexity](https://www.youtube.com/watch?v=zUUkiEllHG0) of `O(nlogn)`, if you want more info search Big O Notation as a key word).  In fact, `table.sort()` uses quick sort to sort the inputted table. 

A sorting algorithm is basically an algorithm that takes a disordered table of number values, and sorts it to return an ordered version of the table (from lesser to greater). 

You are free to do whatever you want, the end product has to be a function `quicksort()`, that takes a table as input, and returns an ordered table.

I am going to explain to you how this algorithm works.

![Quicksort-example|300x180](upload://kAbn1oc4uodYZ7HmgRblUM9oZEk.gif)  *(observe this gif to see how it works)*

First of all, we choose a *pivot*. In the example below, I chose `3`, you can actually choose any member of the table as a pivot, even the first and last elements.

![codingchallenge2-1|480x93](upload://wybkvz7RHwXE5UJR4e3FVkbGNvo.png) 

The table is now, seperated to two parts, the part on the left to the pivot, and the part to the right of the pivot. Essentially, our goal is to make all the members on the right part greater than the pivot, and all the member on the left part less than the pivot.

We will choose two `pointers`, the first one will be the first element of the list, the other will be the last, it would be fine if the pointer was the pivot itself. The first pointer, the one at the start, will be going forward, and each time it finds an element greater than the pivot it stops and wait. The second pointer, the one at the end, will be going backwards, and each time it finds an element greater than the pivot it stops and wait. If both pointers stopped, they swap the elements they refer to. If one of the pointers was holding the pivot, it's fine, it can be swapped as well.

![codingchallenge2-2|480x93](upload://3e4e1dBjbrIGRJ15BQ0HRTkRyFb.png)
 ![codingchallenge2-3|480x155](upload://6EnW5rsmHw4KBuzYPmSYeCopJBT.png) 

And they carry on, until they hit each other and point to the same element, if that happens, we freeze the pivot, meaning it's in its correct position, and will no longer be touched. 

![codingchallenge2-4|480x203](upload://htxXr8Csd3FbcSDEOMUmEIQwOzm.png) 


After it's frozen, you'll notice that the array is split to two parts, what we'll do is, apply a quicksort to both of them! Choosing a pivot again, two pointers, moving and swapping, until they hit each other. And if one of the parts was also split to two parts, we'll implement another quicksort on both the parts, again and again and again, until we're done!

I think you noticed, that we're doing it **recursively** ([recursion](https://www.youtube.com/watch?v=HXNhEYqFo0o)). And we carry on, until all elements are frozen! I hope this helped!

Since this is such a common task, the internet is FILLED with resources about this, so finding more information will be super easy, a good way to improve your searching skills! You can also find sample codes of this sorting algorithm, which can help you a lot. Which is why I think this challenge is easy! You can't get stuck.

Anywho, this is it again! I hope you have fun with this one! You can find a list of all the challenges [here](https://devforum.roblox.com/t/list-of-coding-challenges/485248) or a github version [here](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Coding%20Challenge%20%231.md).


[details="Answer is here! Don't spoil yourself!"]

**PLOT TWIST:** this challenge will not have a well explained solution, I just think the internet has too many code samples, well explained ones, that it's useless to do one on my own. Writing commented code is easy.

![image|388x379](upload://cuRTqxYKBzSzAXgKWJ5SBlev1lm.png) 

Note that in the code, I took a little different approach from what I explained. Which is making the pivot the last element, by swapping it with `pointer2`, then going from `pointer1` to `pointer2`, where `pointer2` now is at the pivot at first. Sorry if it isn't the same way I explainde it.

Code:
```
local function quicksort(array, left, right) --array is the array to sort, left is from where to start sorting and right is from where to end.
    if right-left < 1 then --if it's a 1-element table, just stop
        return array
    end

    local pointer1 = left 
    local pointer2 = right
    local pivot = math.random(left, right) --randomly chosen pivot

    array[pivot], array[pointer2] = array[pointer2], array[pivot] --swap the second pointer with the pivot

    for i = pointer1, pointer2 do --go from pointer1 to pointer2
        if array[i] < array[pointer2] then --each time pointer1 points at something less than pointer2
            array[pointer1], array[i] = array[i], array[pointer1] --swap them , basically making pointer1 move forward

            pointer1 = pointer1 + 1
        end
    end

    array[pointer1], array[pointer2] = array[pointer2], array[pointer1] --at the end swap pointer1 and pointer2

    quicksort(array, 1, pointer1-1) --apply the algorithm to both of the other parts
    quicksort(array, pointer1+1, pointer2) --the part before pointer1, and the part after pointer1

    return array
end

local unsortedArray = {2,5,6,9,8,5,3,4}

print(unpack(quicksort(unsortedArray, 1, 8))) --prints it ordered
```
[/details]
