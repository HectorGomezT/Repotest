
name = input("Whats your name: ")

def greet(name):
    name = name.lower()
    name = name.capitalize()
    return name 

print(f"Hello,{greet(name)}", f"Wow!, your name has {len(name)} letters", sep=".")

def shout (n):
    def echo (name):
        
        name = name.upper() * n

        return name
    return echo

print(name)
print (shout,2)

