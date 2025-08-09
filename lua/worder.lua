local words = {}
while true do
    local w = io.read()
    if w == nil then
        for w in ipairs(words) do
            print(w)
        end
        break
    end
    table.insert(words, w)
end
