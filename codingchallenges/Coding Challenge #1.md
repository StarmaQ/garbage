Coding Challenge #1
--
Welcome everyone to the **Coding Challenge**! This is a series of challenges for interested developers, that I will be releasing every once in a while. The main goal behind doing them is testing yourself and your mind, to see how well you can get around problems. I'm mainly gonna be introducing algorithms and problems where you have to think hard, which is why I think these challenges are great, because they don't just help you improve your inner Roblox developer skills, but also the outer computer science skills, which would be super useful in the future if you're ever going to switch careers. Experience and massive knowledge of what Roblox Studio is capable of isn't really needed to finish a challenge (at least most of them), you just need to know the basics, and work that brains of yours. That's the introduction done, let's get right to it!

First of all, a bunch of info that you would need to know. The challenge would be well-described, giving examples of possible inputs, and required outputs. Once you think you have finished the challenge, dominating every possible case, or you have managed to do a part of it but couldn't finish, you can reply with what you made whenever you want! Even if it's a failed attempt, don't be shy to share it! I never said these challenges were gonna be easy, or hard, the difficulty varies. Also if you have any feedback, or correction, feel free to post a reply! Then expect a DM from me, congratulating you or giving you some notices. The official answer to the challenge would be replied to this topic at maximum before the next 24 hours (sorry if I'm late). The submissions needs some requirements:
* Has to be written in Lua 5.1 (the version roblox uses)
* The program has to be compatible with Roblox Studio, meaning you can't use features vinalla Lua has but rbxlua disabled

****
Now for today's challenge, the first one ever, I want you to write a function, that takes a `number` as an input, and outputs the `French representation` of that number. *Ah oui oui!* :croissant:

Basically, an algorithm to turn numbers into french words. For example, `51` would be `cinquante-cinq`, `168` would be `cent soixante-huit`, and even crazy stuff like `89564686 `which is `quatre-vingt-neuf million cinq cent soixante-quatre mille six cent quatre-vingt-six` (*jeez*).

```lua
print(toFrench(125)) --prints 'cent vingt-cinq'
```

![](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Imgs/codingchallenge1-1.png) 

This algorithm has to work with any given number, no matter how many digits it has (you can limit it to a certain number, 12 digits is enough, meaning billions) and it has to respect all the rules the french numbering system has, such as:
* Adding a hyphen <kbd>-</kbd> when needed
* `80` has an `s` at the end `quatre-vingts` unlike `81` and `82`.. ect. without the `s` (`quatre-vingt-deux`)
* Number with `1` at the end being written às `vingt et un`, `trente et un`, while `81` is written as `quatre-vingt-un` and not  `quatre-vingt et un`
* Invaribale numbers, such as `un`, `deux` .. `onze`, `douze`.../`vingt`, `trente` ..`quatre-vingt-dix`. (Basically numbers from 1 to 16; and all tens, like 10, 20, 30... to 90)
* Numbers between 90 and 99, this is the trickest part
* `1 000 000` and `1 000` written as `un million` and `un mille` but `100` written as just `cent` without a `un`.

And many other special cases that I didn't mention! For a first challenge, this is deffintely tough, which is why you can even share a part of the challenge done, even if it doesn't fully work. Also, which is why you may wanna learn more about the french numbering system, from resources such as [this](https://www.talkinfrench.com/french-numbers/) and [this](https://www.youtube.com/watch?v=WM1FFhaWj9w&feature=emb_title).

Goodluck on your quest! And I hope you had fun doing this! You can find a list of all the challenges [here](http://) (topic not made yet) or a github version [here](http://) (not made yet).

   *Signed,*
   
   
  ![](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Imgs/codingchallenge1-2.png)




Answer
--


Now! Time for the answer :trumpet:!

First thing, we need to setup certain keywords, invariable words, that we will always use throughout the entire program, such as numbers from 0 to 16, and tens like 10, 20 ... all the way to 90, also multiples of ten, such as 1000, 10000000, 10000000000...
So, we would have this
```lua
local invariable = {"zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
"treize", "quatorze", "quinze", "seize"}
local dozens = {"dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt"}
local multiples = {"", "mille", "million", "milliard"}
```
Notice how each number is correspondant to an index. For 1 digit numbers (the tables `invariable`) each number is positioned corresponding to itself plus one, if we wanted 5 (cinq) we would do 5+1, because cinq is at the 6th index. We have to add one because 0 (zéro) is at the first index, and arrays in lua start 1. For tens (the table `dozens`), each number is at its corresponding position as well, for example 40 (quarante) is at 4th index. And for multiples of 10, (the table `multiples`), basically thousands millions billions ect., they're positioned relative to the part of the number they're in. You'll see later that we're dividing each inputed number every 3 numbers, to make things easier. Thousands for example, is always at the second part, (the second 4th, 5th, 6th numbers), millions at third ect. The algorithm I'm writing will only support up to billions (milliard) but you can add more if you want, it's just a matter of adding them into the table.

Next, let's start writing the function
```
function toFrench(num)
	local n = tostring(num) --n is a string represenation of the number, which we would use a lot
	local space = " " --a space that we will use when concatenating
 	local parts = {} --this table would hold each 3 numbers together
	local result = "" --this variable is the output value, that we will constanly change
end
```

To make things easier, we divide each inputed number to different parts each 3 characters, which you might know
![](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Coding%20Challenge%20%231.md)
This makes things easier, because we would always be dealing with 3-digit numbers, and each time just add something from `multiples` according to which part you're currently in. In the upper picture for example, we just need to convert 546, add nothing, then convert 385, add "mille", then convert 1, and add "million". I hope you got the picture.
To divide the number to parts each 3 characters
```
for part in string.gmatch(string.reverse(n),".?.?.?") do --i'm reversing the string for a reason i'll explain later
    table.insert(parts, part)
end
```
Now, it's time to get into the conversion! When I was writing my algorithm, I wrote a list of possible inputs, and started dominating possibility by possibility. I suggest you do that to break down the algorithm to smaller chunks to make things easier.
First, let's eliminate numbers between 0-16. If a person inputed a number inputed between 0 and 16, I can instanly give him the answer, without having to do the parts thing.
```
if invariable[num+1] then return invariable[num+1] end --if it's a number between 0 and 16 (the invariable ones), return what's in that number + 1
```
















