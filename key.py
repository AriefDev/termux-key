import os,sys,time

#### color #####
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;36m'
W = '\033[1;37m'
W1 = '\033[0;37m'

####### logo ###########
logo = '''
%s
                                           _
 _                                        | |
| |_  ____  ____ ____  _   _ _   _        | |  _ ____ _   _
|  _)/ _  )/ ___)    \| | | ( \ / )       | | / ) _  ) | | |
%s| |_( (/ /| |   | | | | |_| |) X ( _______| |< ( (/ /| |_| |
 \___)____)_|   |_|_|_|\____(_/ \_|_______)_| \_)____)\__  |
                                                     (____/%s
------------------------------------------------------------------
|%s Autor : M.Luqman.Arief                                          %s|
|%s Team  : X-Garuda_Red                                            %s|
|%s GT    : \033[4;36mhttps://github.com/AriefDev/\033[0m                            %s|
|%s FB    : \033[4;36mhttps://www.facebook.com/profile.php?id=100055134992811\033[0m %s|
|_________________________________________________________________|
''' % (R,W,G,Y,G,Y,G,Y,G,Y,G)

########## menu #########
def menu():
	os.system("clear")
	print (logo)
	print ('\n')
	print ('%s[%s#%s]%s LIST OF MENU' % (G,R,G,Y))
	print ('\033[0;37m')
	print ('(01).Default extra-key configuration')
	print ('(02).Two rows with more keys')
	print ('(03).Configuration with additional popup keys (swipe up from an extra key)')
	print ('(04).More Tools')
	print ('(05).Exit/Close')
	print ('\n')
	while True:
		try:
			menu = input('%s[%schoose%s]%s >> ' % (B,Y,B,W1))

			if menu == '':
				pass
			elif menu == '1' or menu == '01':
				default()
			elif menu == '2' or menu == '02':
				Thow()
			elif menu == '3' or menu == '03':
				configur()
			elif menu == '4' or menu == '04':
				os.system('xdg-open "https://github.com/AriefDev/"')
			elif menu == '5' or menu == '05':
				print ('%s[%s*%s]%s user Exiting' % (R,Y,R,W1))
				sys.exit()
			else:
				print ('%s[%s*%s]%s wrong input' % (R,Y,R,W1))
		except KeyboardInterrupt:
			print ('%s[%s*%s]%s Stopped (control +C) is detected' % (R,Y,R,W1))
			sys.exit()



################# loading && reload ############
def loading():
	print ('%s[%s*%s]%s add extra-key ...' % (R,Y,R,W1));time.sleep(1)
def reloads():
	print ('%s[%s*%s]%s reload-settings ...' % (R,Y,R,W1));time.sleep(1)
	os.system('termux-reload-settings')
	print ('%s[%s*%s]%s please restart termux app!' % (R,Y,R,W1))

###################### add Extra-Key ############################
def default():
	file = open('termux.properties','w')
	sc = "extra-keys = [[ESC, TAB, CTRL, ALT, {key: '-', popup: '|'}, DOWN, UP]]\n"
	file.write('#code by : M.Luqman.Arief\n')
	file.write('#Team    : X-Garuda_Red\n')
	file.write('#GT      : https://github.com/AriefDev/\n')
	file.write('#FB      : https://www.facebook.com/profile.php?id=100055134992811\n')
	file.write(sc)
	file.close()
	loading()
	os.system('mv termux.properties /$HOME/.termux')
	reloads()

def Thow():
	sc = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'], \['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']] \n"
	file = open('termux.properties','w')
	file.write(sc)
	file.close()
	loading()
	os.system('mv termux.properties /$HOME/.termux')
	reloads()


def configur():
	sc = '''
# code by: M.Luqman.Arief
# Team : X-Garuda_Red
# GT   : https://github.com/AriefDev
# FB   : https://www.facebook.com/profile.php?id=100055134992811
extra-keys = [[ \
  {key: ESC, popup: {macro: "CTRL f d", display: "tmux exit"}}, \
  {key: CTRL, popup: {macro: "CTRL f BKSP", display: "tmux ←"}}, \
  {key: ALT, popup: {macro: "CTRL f TAB", display: "tmux →"}}, \
  {key: TAB, popup: {macro: "ALT a", display: A-a}}, \
  {key: LEFT, popup: HOME}, \
  {key: DOWN, popup: PGDN}, \
  {key: UP, popup: PGUP}, \
  {key: RIGHT, popup: END}, \
  {macro: "ALT j", display: A-j, popup: {macro: "ALT g", display: A-g}}, \
  {key: KEYBOARD, popup: {macro: "CTRL d", display: exit}} \
]]'''
	file = open('termux.properties','w')
	file.write(sc)
	file.close()
	loading()
	os.system('mv termux.properties /$HOME/.termux')
	reloads()
menu()




















