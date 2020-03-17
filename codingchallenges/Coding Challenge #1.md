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
* Numbers between 91 and 99, this is the trickest part
* `1 000 000` and `1 000` written as `un million` and `un mille` but `100` written as just `cent` without a `un`.
* `mille` not having an `s` when there are multiple thousands (ex: `cinq mille`),  but `million` and `milliard` ect. having an `s` if there are multiple. (ex: `cinq millions`)

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
Notice how each number is correspondant to an index. For 1 digit numbers (the tables `invariable`) each number is positioned corresponding to itself plus one, if we wanted 5 (cinq) we would do 5+1, because cinq is at the 6th index. We have to add one because 0 (zéro) is at the first index, and arrays in lua start 1. For tens (the table `dozens`), each number is at its corresponding position as well, for example 40 (quarante) is at 4th index. And for multiples of 10, (the table `multiples`), basically thousands (mille) millions (million) billions (milliard) ect., they're positioned relative to the part of the number they're in. You'll see later that we're dividing each inputed number every 3 numbers, to make things easier. Thousands for example, is always at the second part, (the second 4th, 5th, 6th numbers), millions at third ect. The algorithm I'm writing will only support up to billions (milliard) but you can add more if you want, it's just a matter of adding them into the table.

Next, let's start writing the function
```lua
function toFrench(num)
	local n = tostring(num) --n is a string represenation of the number, which we would use a lot
	local space = " " --a space that we will use when concatenating
 	local parts = {} --this table would hold each 3 numbers together
	local result = "" --this variable is the output value, that we will constanly change
end
```

To make things easier, we divide each inputed number to different parts each 3 characters, which you might know

![](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Imgs/codingchallenge1-3.png)

This makes things easier, because we would always be dealing with 3-digit numbers, and each time just add something from `multiples` according to which part you're currently in. In the upper picture for example, we just need to convert 546, add nothing, then convert 385, add "mille", then convert 1, and add "million". I hope you got the picture.

![d](https://github.com/StarmaQ/garbage/blob/master/codingchallenges/Imgs/codingchallenge1-4.png)

To divide the number to parts each 3 characters
```lua
for part in string.gmatch(string.reverse(n),".?.?.?") do --i'm reversing the string for a reason i'll explain later, also this part might be confusing if you don't know about string patterns and iterators, but just know it splits a string every 3 characters, you can easily come up with another way
    table.insert(parts, part)
end
```
Now, it's time to get into the conversion! When I was writing my algorithm, I wrote a list of possible inputs, and started dominating possibility by possibility. I suggest you do that to break down the algorithm to smaller chunks to make things easier.
First, let's eliminate numbers between 0-16. If a person inputed a number inputed between 0 and 16, I can instanly give him the answer, without having to do the parts thing.
```lua
if invariable[num+1] then return invariable[num+1] end --if it's a number between 0 and 16 (the invariable ones), return what's in that number + 1
```

Now for the most important part, we will be looping through each part (each 3 characters), and converting them. I'm gonna set 3 different variables, one containing the ones, the tens and the hundreds.

```lua
for i = #parts, 1, -1 do --notice how i'm looping through the parts backwards, this is because when we're concatenating, we want them to be in order
	local part = parts[i] --each part each time
	if part ~= "" then --an empty string might be in the table, so I check that off
		local ones, tens, hundreds = tonumber(string.sub(part,1,1)), tonumber(string.sub(part,2,2)), 	tonumber(string.sub(part,3,3))
		local double = tostring(tens)..tostring(ones) --contains the number version of tens and ones together, basically 41, 52, 98 ect.
		local second = "" --contains the french version of tens and ones together, that we will add to the hundreds later
		local prefix = "-" --remember we're gonna need this
	end
end
```
Notice how ones is the first index, tens is the second, hundreds is third. Logically, if we had a part like `"569"` for example, ones is the third, tens is the second, hundreds is the first. Why is it backwards then? Well if you remember, in the upper part when I told you i'll explain why I was reversing the string. This is why, the string is reversed, `"569"` becomes `"965"`, ones becomes first, tens stays second, hunderds becomes third. The reason I'm doing this is, what if a part had just 1 number or 2, instead of 3. Like, `"1"` for example, if I didn't reverse the string, and change the orders, hundreds would be 1, when ones is supposed to be. But if we flip the order, we can make ones be 1, and fix things. See! You alawys gotta find a solution to problems like these!

Now, to the toughest part: the conversion! As I said above, second will contain *ones* and *tens* together, then we add them to hundreds, yet again, a way to make things easier. So first, we start to get to the conversion of the first two numbers (ones and tens). As I said earlier, I eleminate case by case! We'll be constanly using the varibale `double` 

First case: what if double was a number between 0 and 16, I can instanly return that!

Second case: as I said in the original post in rules that we must respect, `90`, `80` and `81` are all special cases, that we can just take care of on their own

Third case: numbers between 91 and 99, which I'll leave on their own aswell because they are different from others

Fifth case: normal conversion, where there is nothing special

Additional situations that we need to take care of: -if ones was anything bigger than 0, but tens was 0, we would need to take care of that. 
-if both ones and tens were 0, I just need to ignore without any conversion
-numbers where tens is > 1, and ones was 1, we would need to add a `" et un"`
-numbers where tens is > 1, and ones was 0, basically 20, 30, 40 all the way to 80

So as you can see! A LOT to take care of, which is why this challenge is hard, so let's get to it.

```lua
local ones, tens, hundreds = tonumber(string.sub(part,1,1)), tonumber(string.sub(part,2,2)), tonumber(string.sub(part,3,3))
local double = tostring(tens)..tostring(ones)
local second = ""
local prefix = "-"


if double ~= "00" and tens ~= nil then --this is the 2nd additional case, we pass when both ones and tens are not zero, and tens exists, we just move on
	if invariable[tonumber(double)+1] then --that's the first case done!
		second = invariable[tonumber(double)+1]
	elseif double == "90" then --these three down below
		second = "quatre-vingt-dix"
	elseif tens == 9 then --this is the case when we're dealing with 90-99
		--we'll do this later!
	elseif double == "81" then
		second = "quatre-vingt-un"
	elseif double == "80" then --are the third case
		second = "quatre-vingts"
	elseif ones == 1 then --this is the third additional case where if ones is == 1
		second = dozens[tens].." et un"
	elseif ones == 0 then --this is the fourth additional case where if ones is == 0
		second = dozens[tens]
	else --this is the normal case, just normal conversion
		--we'll do this later as well!			
	end
elseif ones ~= 0 and tens == nil then --this is the 1st additional case where we got a 1 digit number, meaning ones is anything but 0, and tens is 0
	second = invariable[ones+1]
end
```
That's almost everything covered! The conversion is very self-explainable, which I also explained earlier. Like `dozens[tens]` for example, or `invariable[ones+1]`.

Now, let's take care of the rest, I'm gonna start with the normal conversion, which is really straight forward

```lua
second = dozens[tens]..prefix..invariable[ones+1]
```
Find the word for the dozens (vingt, trente, quarante..), add `"-"` to it, find the word for the number between 1 and 9.

But for 91-99 that's something else! Because numbers from 91 to 99 are written in the form: 80+11, 80+12 ... 80+19, `quatre-vingt-onze`, `quatre-vingt-douze` ... `quatre-vingt-dix-neuf`. We have to take care of two seperate things: from 91 to 96 they have their own rule, and from 97 to 99 have their own as well, because if you remember, 1 to 16 are invariable words, that can't be changed, but 17 to 19 have a rule.

```lua
second = "quatre-vingt"..(invariable[tonumber(double)-80+1] or dozens[1]..prefix..invariable[ones+1])
```

I agree! A rather weird notation. `invariable[tonumber(double)-80+1]` is for the numbers from 1 to 16, `dozens[1]..prefix..invariable[ones+1]` is for 17 to 19. First, I am doing `tonumber(double)-80` because the invariable number is from 1 to 16, what if I get something like 96? `96 - 80= 16` to get the part I want. Then I add one to that again, like I explained in the beginning. Second, `dozens[1]..prefix..invariable[ones+1]` is very easy to explain, I always do `dozens[1]` because that gives back `dix`, and we always need dix (`quatre-vingt-dix-sept to dix-neuf`). Then we add a prefix, then we add `invariable[ones+1]`, because from 97 and 98 and 99, ones would be either 7 or 8 or 9, which we need to look for. And that's it! Crazy right? We got this now.

```lua
if double ~= "00" and tens ~= nil then
	if invariable[tonumber(double)+1] then 
		second = invariable[tonumber(double)+1]
	elseif double == "90" then
		second = "quatre-vingt-dix"
	elseif double == "81" then
		second = "quatre-vingt-un"
	elseif double == "80" then
		second = "quatre-vingts"
	elseif ones == 1 then
		second = dozens[tens].." et un"
	elseif ones == 0 then
		second = dozens[tens]
	elseif tens == 9 then
		second = "quatre-vingt-"..(invariable[tonumber(double)-80+1] or dozens[1]..prefix..invariable[ones+1])
	else
		second = dozens[tens]..prefix..invariable[ones+1]		
	end
elseif tens == nil and ones ~= 0 then
	second = invariable[ones+1]
end
```

Now! For the hundreds part, which is easy.
Here, there are three cases:

First case: if hundreds didn't exits, or was 0

Second case: the normal case, where hundreds is > 1

Third case: if hundreds is equal to 1

```lua
if hundreds == nil or hundreds == 0 then --first case, where there are no hundreds so we don't add hundreds ("cent")	
	result = result..second..space..multiples[i]..space
else --cases where there are hundreds
	if hundreds > 1 then  --case if hundreds is bigger than one, so we add a number before "cent"
		result = result..invariable[hundreds+1].." cent "..second..space..multiples[i]..space
	else --case where hundreds is 1, so we don't add a number before "cent"
		result = result.."cent "..second..space..multiples[i]..space
	end
end
```

And that's it! Notice that I'm putting spaces in the correct placement, and putting `second` (previous part of converting ones and tens) in the correct place as well, you gotta think about that. And also! We're using `multiples` for the first time, which I explained at first, where each part gets its corresponding suffix ("mille", "million", "milliard") according to its index, `i`. And that's it! We're actually done! 

And here is the final beautiful code
```lua
local invariable = {"zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze",
"treize", "quatorze", "quinze", "seize"}
local dozens = {"dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt"}
local multiples = {"", "mille", "million", "milliard"}

function toFrench(num)
	local n = tostring(num)
	local parts = {}
	local space = " "
	local result = ""
	

	if invariable[num+1] then return invariable[num+1] end
	
	for part in string.gmatch(string.reverse(n),".?.?.?") do
    		table.insert(parts, part)
	end
	
	for i = #parts, 1, -1 do
		local part = parts[i]
		if part ~= "" then
			local ones, tens, hundreds = tonumber(string.sub(part,1,1)), tonumber(string.sub(part,2,2)), tonumber(string.sub(part,3,3))
			local double = tostring(tens)..tostring(ones)
			local second = ""
			local prefix = "-"
			
			if double ~= "00" and tens ~= nil then
				if invariable[tonumber(double)+1] then 
					second = invariable[tonumber(double)+1]
				elseif double == "90" then
					second = "quatre-vingt-dix"
				elseif tens == 9 then
					second = "quatre-vingt-"..(invariable[tonumber(double)-80+1] or dozens[1]..prefix..invariable[ones+1])
				elseif double == "81" then
					second = "quatre-vingt-un"
				elseif double == "80" then
					second = "quatre-vingts"
				elseif ones == 1 then
					second = dozens[tens].." et un"
				elseif ones == 0 then
					second = dozens[tens]
				else
					second = dozens[tens]..prefix..invariable[ones+1]		
				end
			elseif tens == nil and ones ~= 0 then
				 second = invariable[ones+1]
			end
							
			if hundreds == nil or hundreds == 0 then
			
				result = result..second..space..multiples[i]..space
			else
				if hundreds > 1 then
					result = result..invariable[hundreds+1].." cent "..second..space..multiples[i]..space
				else
					result = result.."cent "..second..space..multiples[i]..space
				end
			end
		end
	end
	
	return result --return that bad boy
end
```
 
AND FINALLY! We can watch out code kicking butts 
```lua
while true do
	wait()
	local x = math.random(1, 999999999)
	print(x, toFrench(x))
end
```

And just in case this challenge annoyed brutally, [here](https://www.youtube.com/watch?v=vx2Ru0J6I9Q) is a funny video revenging you, by making fun of french numbers.



















