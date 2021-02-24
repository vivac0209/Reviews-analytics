data=[]
x=0
z=0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		
		

print('檔案讀取完了,總共有',len(data),'筆資料')

for i in data:
	z=len(i)
	x=x+z

answer= x/1000000
print('平均留言長度為:' , answer)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new),'筆留言長度小於100')


