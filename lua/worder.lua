local words = {}
while true do
    local w = io.read()
    if w == nil or w == '' then
        for _, word in ipairs(words) do
            print(word)
        end
        break
    end
    table.insert(words, w)
end
