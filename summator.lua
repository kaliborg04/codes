local N = 0
while true do
    local s = io.read()
    if s == 0 then
        print(N)
    end
    n = tonumber(s)
    N = N + n
end
        
