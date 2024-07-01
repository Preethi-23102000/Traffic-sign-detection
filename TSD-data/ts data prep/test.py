import os

full_path_to_ts_dataset = 'C:\\Users\\Preethi Yennemadi\\Desktop\\Udemy course'
os.chdir(full_path_to_ts_dataset)

if __name__ == "__main__":
    for (root,dirs,files) in os.walk('.', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')