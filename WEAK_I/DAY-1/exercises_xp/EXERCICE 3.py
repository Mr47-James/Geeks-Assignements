import hashlib

Name = input("What your Name? ")
Origin = "855f65a4a53daf40a32ec2fccd103bb3"
def Computing_Your_Name(Name):
    eName = Name.encode('utf-8')
    hasher = hashlib.md5()
    hasher.update(eName)
    hash = hasher.hexdigest()
    return hash
name_hash = Computing_Your_Name(Name)
if name_hash != Origin:
    print("Wow I'm sure that your father was a genius to not give you my name, and yes you can't know my name. ")
else:
    print("High And it's My pleasure, I think we have something here in common <<Only 2 letters>>")



    
