import os 
import shutil 

def create_directories_for_files():
	file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
	for file in file_list:
		if file[0] != '.':
			directory_name = os.path.splitext(file)[0]
			if not os.path.exists(directory_name):
				os.makedirs(directory_name)
				with open(os.path.join(directory_name, "Readme.md"), 'w') as readme_file:
					pass 
			shutil.copy(file, os.path.join(directory_name, file))

if __name__ == '__main__':
	create_directories_for_files()
