import os
import shutil
import time

def program():

	deletedFolders = 0
	deletedFiles = 0

	path = input("What is the path? : ")
	days = int(input("How many days old should the file be?"))

	seconds = time.time() - (days*86400)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= findAge(root_folder):
				remove_folder(root_folder)
				deletedFolders += 1
				break

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= findAge(folder_path):
						remove_folder(folder_path)
						deletedFolders += 1 

				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= findAge(file_path):
						remove_file(file_path)
						deletedFiles += 1

		else:
			if seconds >= findAge(path):
				remove_file(path)
				deletedFiles += 1

	else:
		print(f'"{path}" is not found')
		deletedFiles += 1

	print(f"Total folders deleted: "+deletedFolders)
	print(f"Total files deleted: "+deletedFiles)


def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Unable to delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print(path+"is removed successfully")

	else:
		print("Unable to delete the "+path)


def findAge(path):
	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__main__':
	program()