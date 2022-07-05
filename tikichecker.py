import requests , random
from colorama import Style,Fore

R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
c = Fore.LIGHTMAGENTA_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
print(B+f"""
       _______ _                 _                    _______ _ _     _   
      (_______) |               | |                  (_______|_) |   (_)  
       _      | |__  _____  ____| |  _ _____  ____       _    _| |  _ _   
      | |     |  _ \| ___ |/ ___) |_/ ) ___ |/ ___)     | |  | | |_/ ) |  
      | |_____| | | | ____( (___|  _ (| ____| |         | |  | |  _ (| |  
       \______)_| |_|_____)\____)_| \_)_____)_|         |_|  |_|_| \_)_|                                                                                                                                                                                                                                                                                            
---------------------------------------------------------------------------------------
   {R}By Foatn{B} : {Y}Telegram Channel https://t.me/ifostn{B} : {b}Twitter @lwv5 {B} : {r}Instagram @f09l{B}
---------------------------------------------------------------------------------------

""")
a = 0
countt = int(input(B+"Enter The Count : "))
length = int(input(B+"Enter The Length : "))
save_file = input(Y+"Enter the name of the file to save it ")
chars = "qwertyuiopasdfghjklzxcvbnm123456789_0"

while a < countt:
    users = str("".join(random.choice(chars)for i in range(length)))
    url = (f'https://tiki.video/@{users}?')
    r = requests.get(url)
    if length < 4:
        print(R+"Warning : Please username must be 4 characters or longer")
        break
    elif r.status_code == 404 and length > 3 :
        print(G+f"Available : {users}")
        open(save_file+".txt","a").write(f"{users}\n")
    elif r.status_code == 200:
        print(R+f"Not Available : {users}")
    else:
        print("So many requests please wait  ")
        break
    a = a+1

