local RunService = game:GetService("RunService")

local function wait(n)
    local dt = 0

    while dt < n do
        dt = dt + RunService.Heartbeat:Wait()
    end
    return false, dt
end
