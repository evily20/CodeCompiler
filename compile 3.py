from tkinter import *
import pickle
import subprocess
import sys
import time
root=Tk()
root.title("CodeX")

L=Label(root,text="CODE COMPILE AND RUN")

    
def func2():
   try:
      print("Hey")
      print("code is compiling")
      str1=T.get("1.0",'end-1c')
      #inp=Tinp.get("1.0",'end-1c')
      #l=len(inp)
      #print(l)
      #if(l!=0):
         #ff=open("input.txt","w")
         #ff.write(inp)
         #ff.close()
      #print(str1)
      str2=TL.get("1.0",'end-1c')
      #print(str2)
      #print(inp)
      if(str2=="C++"):
         f=open("in.cpp","w")
         f.write(str1)
         f.close()
         cmd = "g++ in.cpp"
         op1=((subprocess.check_output(cmd)).decode("utf-8"))
         #print(op1)
         cmd="a"
         #if(l!=0):
            #cmd="a < input.txt"
         op2=subprocess.check_output(cmd)
         entry.delete(0, "end")
         entry.insert(0,op2)
         #print(op2)
      elif(str2=="C"):
         print(str1)
         
         f=open("in.c","w")
         f.write(str1)
         f.close()
         #sys.stdout.close()
         cmd = "gcc in.c"
         op1=((subprocess.check_output(cmd)).decode("utf-8"))
         #print(op1)
         cmd="a"
         #if(l!=0):
            #cmd="a < input.txt"

            #time.sleep(5)
            #op2=subprocess.check_output(cmd)
            #time.sleep(4)
            #print(op2.decode())
         op2=((subprocess.check_output(cmd)).decode("utf-8"))
         print(op2)
         entry.delete(0, "end")
         
         entry.insert(0,op2)
         
            
         #print(op2)
   except:
      entry.delete(0, "end")
      entry.insert(0,"Error in code")
      
      
      
      
   

B1=Button(root,text="RUN",command=func2)

T=Text(root,height=30,width=80)
TL=Text(root,height=2,width=10)

entry = Entry(root, bd=1)
entry.insert(0, 'OUTPUT\n\n.')

#Button(root,text="Hey",command=root.destroy).pack()


L.pack()
TL.pack()
T.pack()


B1.pack()
entry.pack()

root.mainloop()
