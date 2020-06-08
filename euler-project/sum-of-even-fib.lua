local function fib(n, memo)
  if n == 0 then return 0 end
  if n == 1 then return 1 end
  local num = (memo[n-1] or fib(n-1, memo)) + (memo[n-2] or fib(n-2, memo))
  if not(memo[n]) then
    memo[n] = num
  end

  return num, memo
end

local sum = 0
local i = 0
while true do
  local n = fib(i, {}) 
  i = i + 1
  if n < 4e6 then
    if n%2==0 then
      sum = sum + n
    end
  else
    break 
  end
end
print(sum) --4613732
