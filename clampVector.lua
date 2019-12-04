local function clamp(v3, x, y, z)
	return Vector3.new(math.clamp(v3.X, x[1], x[2]), math.clamp(v3.Y, y[1], y[2]), math.clamp(v3.Z, z[1], z[2]))
end
