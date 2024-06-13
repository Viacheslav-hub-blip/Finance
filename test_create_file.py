from trash import t

file = open('test_file.txt', 'w')

for i in t:
    event = i
    s  = f'what happens after {event.event}? ' \
         f'Answer: {event.description} ' \
         f'stock_price_change: {event.change_stock_price} ' \
         f'semantic: {event.semantic} ' \
         f'company: {event.company} ' \
         f'\n'
    file.write(s)
file.close()

file = open('test_file.txt', 'r')
con  = file.read()
print(con)

s = '{"text": '