symbol_start = int(input('Enter start symbol: '))
symbol_count = int(input('Enter symbol count: '))
symbol_end = symbol_start + symbol_count
i = symbol_start
while i < symbol_end:
    print(i, chr(i))
    i += 1
