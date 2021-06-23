import os
import glob
#import os.path
from os import path
import  csv
from datetime import datetime

#Scratch version. 

#to check if a file exists in a path true if yes false if no
path.exists('/var/log/TMStomV2_...') #true or false
# reading a file  starting from the second column the result is 2d list  will be used later after gettign the paths
# the output of a function get_last _file  will provide us with the argument for var file.

#to get from the second line
file = "tracesmetiers.log"
result = [x.split(';')[2:-1] for x in open(file).readlines()]
print(result)

# to write list into a file
with open("out.csv","w") as f:
    wr = csv.writer(f)
    wr.writerows(result)

######################################################################################
#this function will provide us the lastest folder or file
#global_path = '/var/log/*'
def get_last_file(global_path):
    list_of_static_folders_h5 = ['1-intra', '3-intran', 'c-intran', '4-intran']
    list_of_folders = glob.glob(global_path)
    path_of_latest_global_folder = max(list_of_folders, key=os.path.getctime) #<type 'str'>  we get this output: /var/log/T...
    list_of_the_latests_h5_folders = [path_of_latest_global_folder+'/'+ sub+'/*' for sub in list_of_static_folders_h5] #CHECKED 18/06/21 17:26

    #list_of_log_files = [glob.glob(latest_h5_folder) for latest_h5_folder in list_of_the_latests_h5_folders]

    list_of_log_files = map(''.join, [glob.glob(latest_h5_folder) for latest_h5_folder in list_of_the_latests_h5_folders])
    return list_of_log_files


'''
This function will merge all the files together. 
'''
def merging_files(list_of_log_files):

    # Open log_file.log in write mode
    with open('LOG_FILE.txt', 'w') as fout:
        #add current date & time which will be visible by  the command head -1
        fout.write(str(datetime.now())+"\n")

        for element in list_of_log_files:

            with open(element) as fin:
                fout.write(fin.read())
        # Add '\n' to enter data of the nextfile
        #fout.write("\n")

list_of_log_files = ['tracesmetiers.log', 'DCI_tracesmetiers.log' ,'H54_tracesmetiers.log']
merging_files(list_of_log_files)
