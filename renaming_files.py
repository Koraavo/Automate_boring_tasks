import os

os.chdir('path')
#print(os.getcwd()) # checking my directory
#os.rename('101MSDCF', 'Hampi')
num = 0

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)  # split with their extensions
    #print(f_name)
    new_name = f'{"file-name"}-{num:02}{f_ext}'
    num += 1
    #print(new_name)
    os.rename(f, new_name)
