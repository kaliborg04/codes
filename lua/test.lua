local t = {"foo", "bar", "baz"}
for i = 1, #t do
    print(t[i])
end

for i = #t, 1, -1 do
    print(t[i])
end

local i = 1
while i <= 3 do
    print(t[i])
    i = i + 1
end

local i = #t
while i >= 1 do
    print(t[i])
    i = i - 1
end

for i, x in ipairs(t) do
    print(i, x)
end

local function reverse(t)
    local rev = {}
    for i = #t, 1, -1 do
        table.insert(rev, t[i])
    end
    return rev
end

for _, x in ipairs(reverse({7, 8, 9})) do
    print(x)
end

local t = {foo=7, bar=8, baz=9}
for k, v in pairs(t) do
    print(k, v)
end

