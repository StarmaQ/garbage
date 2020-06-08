local function LargestPalinProduct()
  local previous = 0
  for i = 999, 100, -1 do
    for j = 999, 100, -1 do
      if string.reverse(i*j) == tostring(i*j) and i*j > previous then
        previous = i*j
      end
    end
  end
  return
end

LargestPalinProduct()
