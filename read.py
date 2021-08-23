data = [] # 建立一個data變數他是一個空清單
count = 0 # 宣告一個變數 count 資料為 0
with open('reviews.txt', 'r') as f: # 用讀取模式打開reviews檔案並當作 f
    for line in f: # line 從 f 裡
        data.append(line) # 新增line至 data的清單
        count += 1 # count = count +1
        if count % 1000 == 0: # 如果 count /1000 取餘數等於 0的話就
            print(count) # 印出 每一千筆的 count
print('共有', len(data), '筆資料') # 印出 執行上列程式後所裝的 data長度

print(data[0])


sum_len = 0 # 宣告 sum_len 變數資料為 0,紀錄留言長度的總數
for d in data: # d 從 data裡
    sum_len += len(d)
print('平均留言長度是', sum_len/len(data)) # 印出 sum_len總數 / data資料數 = 平均數

new = [] # 建立一個新的空清單為 new
for d in data: # d 從 data裡
    if len(d) < 100: # 如果 d的長度 小於 100就
        new.append(d) # 新增 d到 new的清單
print('共有', len(new), '筆留言小於100個字') # 印出 小於100個字的清單總數

good = [] # 新增good空清單
for d in data: # d 從 data裡
    if 'good' in d: #　如果字串 good有在 d裡面就
        good.append(d) # 將 d新增至 good清單裡
print('共有',len(good), '筆留言提到good') # 印出 提到good的總數

# good = [d for d in data if 'good' in d] # output = [(number-1)運算 for number變數 in reference清單 if number %篩選條件 2 == 0]

print(good[0])


# 文字記數
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請輸入查詢字元: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現的次數為', wc[word])
    else:
        print('這個字元沒有出現')

print('感謝使用查詢功能')