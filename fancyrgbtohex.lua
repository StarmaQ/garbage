
local hex = 0xFFFFFF --example
local R = bit32.rshift(bit32.band(hex, 0xFF0000), 16)
local G = bit32.rshift(bit32.band(hex, 0x00FF00), 8)
local B = bit32.band(hex, 0x0000FF)
print(R, G, B)
