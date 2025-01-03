import string 
import random
print("_______PASSWORD GENERATOR_______")
if __name__=="__main__": 
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    length=int(input("Enter the length of the password:"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print(f"GENERATED PASSWORD:{"".join(random.sample(s,length))}")
    

