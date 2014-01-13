b = []
f = open('square_detector_example_input.txt','r')
line = f.readlines()
T = (int(line[0].strip()))
i = 1
line_no = 1
while i <= T:
    a = []
    for ti in range(line_no + 1, (line_no + int(line[line_no]) + 1)):
        a.append(line[ti].strip())
    b.append(a)
    line_no += (int(line[line_no]) + 1)
    i += 1
x = []
h_count = []
y_lis = []
def solve(li):
    for y,si in enumerate(li):
        if si.count('#') != 0:
            x.append(si.find('#'))
            h_count.append(si.count('#'))
            y_lis.append(y)
    if len(x) != h_count[0] or len(y_lis) != h_count[0]:
        return 'NO'
    elif all(xi == x[0] for xi in x) and all(hi == h_count[0] for hi in h_count) and all(yi == (y_lis[0] + i) for i,yi in enumerate(y_lis)):
        return 'YES'
    else:
        return 'NO'
print solve(['#####', '#####', '#####', '#####', '#####'])
'''g = open('square_detector_output.txt', 'w')
for i,oi in enumerate(b):
    print i,oi
    print 'Case #' + str(i+1) + ': ' + solve(oi)
    g.write('Case #' + str(i+1) + ': ' + solve(oi) + '\n')
f.close()
g.close()'''
