data=[]
x=0
z=0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		
		

print('檔案讀取完了,總共有',len(data),'筆資料')
print(data[0])

for i in data:
	z=len(i)
	x=x+z

answer= x/1000000
print('平均留言長度為:' , answer)

# # 篩選 每筆資料的字數長度小於100的話 就抓出來 存到new清單中
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new),'筆留言長度小於100')
print(new[0])
print(new[1])

# # 篩選 每筆資料中 有good這個字 就抓出來這筆資料  存在good清單中
good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('一共有', len(good),'筆留言包含good')
print(good[0])
print(good[1])

# # 快寫法 最前面的d 是把d代表的資料存在good清單中
# #就是把讀取到這筆資料存在d 跑到if做判斷 true的話就會把d代表的資料存在good清單中
# good= [d for d in data if 'good' in d]
# print(good)

# # 把前面的d 改成1  等於符合這條件的 加到good清單中的會是1 不是資料 有兩段多筆資料符合
# # 那good清單中就會有兩萬多個的1
# good= [1 for d in data if 'good' in d]
# print(good)

# # 另一種快寫法的篩選 
# # 把每筆資料都跑一遍 前面的'bad' in d 是每跑一次抓出的資料放在d 去判斷資料中有沒有bad
# # 有的話變成true存進去 沒有的話變成false存進去 這樣bad清單裡面存放的都是true 或 false
# bad =['bad' in d  for d in data]
# print(bad)

# # 上面快寫法的 原本寫法
# bad = []
# for d in date:
# 	bad.append('bad' in d) #這邊print出的是 布林值


# 文字計數功能
wc = {}			# word_count

for d in data:
	words = d.split()			# split的預設值是空白鍵
	for word in words:
		if word in wc:
			wc[word]+=1
		else:
			wc[word]=1		#新增新的key進wc字典
# 把每個字出現次數 print出來  用for loop跑 print這樣比較整齊 
for word in wc:
	if wc[word] > 100:					# 這個字出現超過100次
		print(word , wc[word])

print(len(wc))
print(wc['Allen'])					#這個是查詢allen在裡面出現過幾次

# 這功能是查詢這個字 在留言裡出現多少次
while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:' , wc[word])
	else:
		print('這個字沒有出現過!')

print('感謝使用本查詢功能')








	

