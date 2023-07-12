
from aptos_sdk.account import Account


print(f"\n\n ")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)


i=0
f=open("aptos_ad.txt", "a", encoding='utf-8')
for private_key in keys_list:
    i+=1
    current_account = Account.load_key(key=private_key)
    ad = current_account.address()
    print(ad)
    f.write(str(ad) + "\n")  

