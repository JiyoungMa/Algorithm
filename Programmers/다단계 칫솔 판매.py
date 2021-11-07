def solution(enroll, referral, seller, amount):
    answer = []
    parent = dict()
    money = dict()
    profit = dict()
    
    parent["-"] = None
    money["-"] = 0
    profit["-"] = []
    
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        money[enroll[i]] = 0
        profit[enroll[i]] = []
        
    for i in range(len(seller)):
        now_money = amount[i]*100
        now_profit = now_money//10
        now_money -= now_profit
        money[seller[i]] += now_money
        profit[parent[seller[i]]].append(now_profit)
        
    for i in range(len(enroll)-1,-1,-1):
        for p in profit[enroll[i]]:
            if p<10:
                continue
            now_profit = p//10
            money[enroll[i]] -= now_profit
            profit[parent[enroll[i]]].append(now_profit)
        
    for e in enroll:
        total = money[e] + sum(profit[e])
        answer.append(total)
    return answer
