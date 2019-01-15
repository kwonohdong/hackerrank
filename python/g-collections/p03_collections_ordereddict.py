from collections import OrderedDict


n = int(input())

ordered_dictionary = OrderedDict()

for _ in range(n):
    item_name, space, net_price = input().rpartition(' ')
    
    # dict.get('key', default) → key 값이 없으면 default 반환
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + int(net_price)

for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)
