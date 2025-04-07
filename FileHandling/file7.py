f=open('C:\\FileHandling\\XYZ.c','w') 
       # file is opened 
f.write("#include<stdio.h>\n\n")
f.write("int main()\n{") 
f.write('\nprintf(\"Hello World\");\n')
f.write('\nreturn(0);\n}')

f.close()
print('File Created')