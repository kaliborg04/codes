local N = 0
while true do
    io.write("Enter number: ")
    local s = io.read()
    if s == nil or s == "" then
        print(N)
        break
    end
    N = N + tonumber(s)
end
