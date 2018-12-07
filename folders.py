import sys

def main():
	yourChoice = input("enter\n 'm' to make folders\n 'r' to remove folders\n")
	if yourChoice == 'm':
		import makeFolders
		makeFolders.make()
	elif yourChoice == 'r':
		import removeFolders
		removeFolders.delete()
	else:
		print('exiting !!')
		sys.exit()
		
if __name__ == '__main__':
	main()
