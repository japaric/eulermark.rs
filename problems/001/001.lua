posix = require "posix"

local function f()
    local ans = 0

    for i = 0,999 do
        if i % 3 == 0 or i % 5 == 0 then
            ans = ans + i
        end
    end

    return ans
end

function toNs(ts)
    return ts[1] * 1000000000 + ts[2]
end

if #arg == 0 then
    print(f())
elseif #arg == 1 then
    iters = tonumber(arg[1])
    start = { posix.clock_gettime("monotonic") }
    for i = 1,iters do
        f()
    end
    end_ = { posix.clock_gettime("monotonic") }
    print(toNs(end_) - toNs(start))
end
