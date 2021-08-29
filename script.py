import os
import subprocess
import sys


file = open("makefile", "r")
lines = file.readlines()
flag = ["-O0" , "-O1" , "-O2" , "-O3" , "-Ofast" , "-Os" , "-Og" , "-funroll-loops"]

file2 = open("src/CHeterodyning_threaded.h", "r")
l = file2.readlines()
threads = [2 , 4 , 8, 16 , 32]

def main():
   for i in flag:      # for loop for running the different CFLAGS of unthreaded C program
      lines[2] = "CFLAGS = -lm -lrt " + i + "\n"
      myfile = open("makefile", "w")
      myfile.writelines(lines)
      myfile.close()
      os.system("make clean")
      os.system("make")
      os.system("make run")
      
      for f in threads:    #for loop for running threaded C program
         lines[2] = "CFLAGS = -lm -lrt \n"
         myfile = open("makefile", "w")
         myfile.writelines(lines)
         myfile.close()
         l[14] = "#define Thread_Count " + str(f) + "\n"
         mfile = open("src/CHeterodyning_threaded.h","w")
         mfile.writelines(l)
         mfile.close()
         os.system("make clean")
         os.system("make threaded")
         os.system("make run_threaded")
      
      
#    for j in threads:    #for loop for running diferent CFLAGS for threaded C program
#       lin[14] = "#define Thread_Count " + str(j) + "\n"
#       myfile3 = open("src/CHeterodyning_threaded.h","w")
#       myfile3.writelines(line)
#       myfile3.close()
#       for k in flag:
#          lines1[2] = "CFLAGS = -lm -lrt " + i + "\n"
#          myfile = open("makefile", "w")
#          myfile.writelines(lines1) """
#          myfile.close()
#          os.system("make clean")
#          os.system("make threaded")
#          os.system("make run_threaded")
      
if __name__ == "__main__" :
   main()
      
      
      
