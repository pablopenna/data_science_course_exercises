import sys

string = sys.argv[1]
print("your str is {}".format(string))

palabras = string.split(" ")

# res = [(palabra,idx+1,len(palabra),len(palabra)%(idx+1)==0) for idx,palabra in enumerate(palabras)]
# res = [(palabra,idx,len(palabra),len(palabra)%idx==0) for idx,palabra in enumerate(palabras) if idx>0]
res = [ (palabra,idx,len(palabra),len(palabra)%idx==0) if idx>0  else "emptyField" for idx,palabra in enumerate(palabras)]
print(f"res: {res}")
