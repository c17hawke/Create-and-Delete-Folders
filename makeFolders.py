import os 
import sys

def start():
	'''start sequence'''
	start_folder = input('starting folder seq \n')
	if len(start_folder) > 0:
		start_folder = int(start_folder)
	else:
		start_folder = 1
	return start_folder

def creating(start_folder, end_folder, common_name):
	'''creates new folders'''
	for i in range(start_folder ,end_folder + 1):
		try:
			if i < 10:
				os.system('mkdir 0'+ str(i) + common_name)
			else:
				os.system('mkdir '+ str(i) + common_name)
		except Exception as e:
			pass

def validate(start_folder,end_folder):
	'''validate the sequence'''
	if start_folder>end_folder:
		print("relaunch again!!")
		sys.exit()

def make():
	start_folder = start()

	end_folder = int(input('how many folders you need \n'))
	try:
		validate(start_folder,end_folder)

		common_name = input('suggest a common name for the folders \n')

		if len(common_name) > 0:
			pass
		else:
			# default case
			print("No input given.\n Initiating default case!!\n")
			common_name = 'folder'


		creating(start_folder, end_folder, common_name)
	finally:
		print("DONE !!")


if __name__ == '__main__':
	make()
