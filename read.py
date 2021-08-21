data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count +1
        if count % 1000 == 0:
            print(count)
print('共有', len(data), '筆資料')

print(data[0])
print('--------------------------------------------')
print(data[1])