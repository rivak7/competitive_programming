record = input()
i = 0
score = [[0, 0]]
end = False
special = False

while i < len(record) and not end:
    c = record[i]
    s = int(record[i+1])
    if c == 'A':
        score.append([score[-1][0] + s, score[-1][1]])
    elif c == 'B':
        score.append([score[-1][0], score[-1][1] + s])
    i +=2
    
    if len(score) > 1:
        special = (score[-2] == [9,10] and score[-1] == [11,10]) or (score[-2] == [10,9] and score[-1] == [10,11])
    
    A = score[-1][0]
    B = score[-1][1]
    
    if A > 10 and ((A-B) > 1 or special):
        print('A')
        end = True

    if B > 10 and ((B-A) > 1 or special):
        print('B')
        end = True
