local module = {}


function module.Visualise(v3) 
	local part = Instance.new("Part")
	part.Name = "Vector"
	part.BrickColor = BrickColor.Random()
	part.Anchored = true
	part.Size = Vector3.new(0.2, 0.2, v3.magnitude)
	part.CFrame = CFrame.new(v3/2, v3)
	part.Locked = true
	part.Parent = workspace
end

return module
