import os 
import sys

def end():
	'''this selects and end folder seq'''
	for i in range(2):
		num_of_folder = input('how many folder you want to remove \n')
		if len(num_of_folder) > 0:
			num_of_folder = int(num_of_folder)
			break
		elif i == 1:
			print("Nothing will be deleted ! Hence exiting the program")
			sys.exit()
		else:
			print("please give an input, you have one more chance left\n")
	return num_of_folder

def removing(start_folder,num_of_folder,common_name):
	'''this function deletes the folders'''
	for i in range(start_folder,num_of_folder+1):
		try:
			if i < 10:
				os.system('rm -r 0'+ str(i) + common_name)
			else:
				os.system('rm -r '+ str(i) + common_name)
		except:
			print("folder doesn't exists")

def validate(start_folder,num_of_folder):
	if start_folder>num_of_folder:
		print("relaunch again")
		sys.exit()

def delete():
	start_folder = input('starting folder seq \n')

	if len(start_folder) > 0:
		start_folder = int(start_folder)
	else:
		print("No input given.\n Initiating default case!!\n")
		start_folder = 1

	try:
		num_of_folder = end()
		validate(start_folder,num_of_folder)
		common_name = input('suggest a common name for the folders to remove \n')

		if len(common_name) > 0:
			pass
		else:
			print("No input given.\n Initiating default case!!\n")
			common_name = 'folder'
		removing(start_folder,num_of_folder,common_name)

	finally:
		print("DONE !!")	

if __name__ == '__main__':
	delete()
