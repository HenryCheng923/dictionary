import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有', len(data),'筆資料')

start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc: #如果word裡面的字有出現在字典裡就+1
			wc[word] += 1 #類似words['tea'] = '茶'，這裡意思就是找到word這個字，就將value加1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:  #word是key  wc[word] 查找word的次數
	if wc[word] > 1000000: #wc[word] 就是查找有這個字在字典裏面的對應數字
		print(word, wc[word])

end_time = time.time()
print('花了',end_time - start_time, 'seconds')

print(len(wc)) #字典的長度

while True:
	word = input("請問你想查什麼字：")
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為： ', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用')


# sum_len = 0 
# for d in data:
# 	sum_len += len(d)
# print('留言平均長度', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d)<100:
# 		new.append(d)
# print('一共有 ', len(new), '筆留言長度小於100')

# find_good = []
# for d in data :
# 	if 'good' in d:
# 		find_good.append(d)
# print('一共有', len(find_good), '筆留言提到good') 


#list 清單快寫法
f#ind_good = [d for d in data if 'good'in d]
#第一個d的意思是"find_good.append(d)的意思，
#for d in data ，將data資料放到d裡面，
#if 'good' in d  ，如果d裡面有good的，
#放入第一個d裡面