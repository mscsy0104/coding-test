# height = [4,3,2,1,4]
height = [1,8,6,2,5,4,8,3,7]
mid= sum(height)/len(height)
print(mid)

k_li=[]
v_li=[]
for i, h in enumerate(height):
    if h>mid:
        k_li.append(i)
        v_li.append(h)
    else: pass

print(f'k_li: {k_li}')
print(f'v_li: {v_li}')
k_sub_li=[]
for i, k1 in enumerate(k_li):
    for j, k2 in enumerate(k_li[i+1:]):
        if k1>k2: k_sub_li.append(k1-k2)
        else: k_sub_li.append(k2-k1)
print(k_sub_li)

li=[]
for i in range(len(k_sub_li)):
    li.append(k_sub_li[i]*v_li[i])

print(li)



# Memory Limit Exceeded
# prod_li = []
# for i, h1 in enumerate(height):
#     for j, h2 in enumerate(height[i+1:]):
#         if h1>h2:
#             prod_li.append((j+1)*h2)
#         else:
#             prod_li.append((j+1)*h1)
# print(prod_li)

