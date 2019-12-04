local plr = game.Players.LocalPlayer 
local mouse = plr:GetMouse() 
local camera = workspace.CurrentCamera
local target 
local down


local function clamp(v3, x, y, z)
  return Vector3.new(math.clamp(v3.X, x[1], x[2]), math.clamp(v3.Y, y[1], y[2]), math.clamp(v3.Z, z[1], z[2]))
end


mouse.Button1Down:connect(function() 
	if mouse.Target ~= nil and mouse.Target.Locked == false then
		target = mouse.Target 
		mouse.TargetFilter = target 
	down = true 

	local gyro = Instance.new("BodyGyro") 
	gyro.Name = "Gyro"
	gyro.Parent = target 
	gyro.MaxTorque = Vector3.new(500000, 500000, 500000)
	local force = Instance.new("BodyPosition") 
	force.Name = "Force" 
	force.Parent = target
	force.MaxForce = Vector3.new(10000, 10000, 10000) 
	end
end)

game:GetService("RunService").RenderStepped:Connect(function()
	if down == true and target ~= nil then 
		target.Force.Position = clamp(camera.CFrame.p + (mouse.UnitRay.Direction * 20), {-20, 20}, {-20, 20}, {-20, 20})
	end 
end) 
mouse.Button1Up:connect(function() 
	if target then
		if target:FindFirstChild("Gyro") or target:FindFirstChild("Force") then
			target.Gyro:Destroy()
			target.Force:Destroy()
		end
	end
	down = false
	mouse.TargetFilter = nil
	target = nil 
end)
