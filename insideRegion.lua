--a inRegion function which is useful as heck, roblox add please thank you

local NormalIds = Enum.NormalId:GetEnumItems()
function insideRegion(region, object)
    for i = 1, #NormalIds do
        local enum = NormalIds[i]
        local norm = Vector3.FromNormalId(enum)
        local worldnorm = region.CFrame:vectorToWorldSpace(norm)
        local distance = (norm * region.Size/2).Magnitude
        local planepoint = region.CFrame.Position + worldnorm * distance
        if (object.Position - planepoint):Dot(worldnorm) > 0 then
            -- not inside region
            return false
        end
    end
    -- inside region
    return true
end
