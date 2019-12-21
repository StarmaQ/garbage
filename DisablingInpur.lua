local ContextActionService = game:GetService("ContextActionService")

ContextActionService:BindAction(
    "DisableZ",
    function() return Enum.ContextActionResult.Sink end, 
    false,
    unpack(Enum.PlayerActions:GetEnumItems()) --these are the inputs we wanna disable, going left and right, basically along the Z axis, here are all of the player inputs, here are all the inputs https://developer.roblox.com/en-us/api-reference/enum/PlayerActions
)
