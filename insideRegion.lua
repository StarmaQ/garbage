--a inRegion function which is useful as heck, roblox add please thank you

local NormalIds = Enum.NormalId:GetEnumItems()
function insideRegion(cf,size,point)
    for i = 1, #NormalIds do
        local enum = NormalIds[i]
        local norm = Vector3.FromNormalId(enum)
        local worldnorm = cf:vectorToWorldSpace(norm)
        local distance = (norm * size/2).Magnitude
        local planepoint = cf.Position + worldnorm * distance
        if (point - planepoint):Dot(worldnorm) > 0 then
            -- not inside region
            return false
        end
    end
    -- inside region
    return true
end
