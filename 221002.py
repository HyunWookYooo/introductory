from xml.sax.handler import DTDHandler


A = "ATCGATCG"
B =""
for s in A:
  if s == "A":
    B += "T" 
  elif s == "T": 
    B += "A"
  elif s == "G":
    B += "C"
  elif s == "C":
    B += "G"
    print(B[::-1]) 
print(A)