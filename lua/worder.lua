local words = {}
while true do
    io.write("Enter number: ")
    local w = io.read()
    if w == nil or w == '' then
        table.sort(words)
        for _, word in ipairs(words) do
            print(word)
        end
        break
    end
    table.insert(words, w)
end
