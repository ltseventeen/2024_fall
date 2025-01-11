n,m=map(int,input().split()) #n件商品，m家店
goods=[]
for _ in range(n):
    goods.append(list(input().split())) #第i件商品的出售店铺和价格
youhui=[]
for _ in range(m):
    youhui.append(list(input().split())) #第i家店的优惠券
result=float('inf')
sold=[0]*m #第i家店的已买的价格

def dfs(i,sum_price): #i表示当前商品编号（0-（n-1）），sum_price表示当前购物车的总价
    global result
    if i==n: #所有商品都已购买完
        result_i=0
        #店铺计算满减
        for i1 in range(m): #第i1家店
            price=float('inf')
            for quan in youhui[i1]: #第i1家店的每种优惠券
                man,jian=map(int,quan.split('-'))
                if sold[i1]>=man: #满减条件成立
                    price=min(price,sold[i1]-jian)

            if price!=float('inf'): #有满减优惠
                result_i+=price
            else: #无满减优惠
                result_i+=sold[i1]
        #计算跨店满减并更新全局最优
        result=min(result,result_i-(sum_price//300)*50)
        return

    for shoujia in goods[i]:
        k,price_i=map(int,shoujia.split(':')) #第i件商品的第k家店的价格
        sold[k-1]+=price_i #第k家店的已买的价格增加
        sum_price+=price_i #购物车总价增加
        dfs(i+1,sum_price) #购买第i+1件商品
        #回溯
        sold[k-1]-=price_i #第k家店的已买的价格减少
        sum_price-=price_i #购物车总价减少

dfs(0,0)
print(result)


