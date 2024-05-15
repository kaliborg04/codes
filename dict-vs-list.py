l = ['mk45', 'rg3', 'vostok3']
l[0]
l.append('sun')
l += ['sun']
l[1] = 'iss'

d = {'mk45': 1, 'rg3': 7, 'vostok3': 5}
d['rg3']
d['sun'] = 1
d['Mars'] = 1
d['mk45'] = 2
d['Mars'] += 1

d = {1: 'rg3', 0: 'mk45', 2: 'vostok3'}
d[0]