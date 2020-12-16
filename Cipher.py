import tkinter as tk


alpha = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

fields = ('Key\n(no common factors with 26)', 'Second key\n(0-25)',
          'Text to Encrypt', 'Text to Decrypt')

def Encrypt(entries):
    #First key
    ciphered = ""
    key = (int(entries['Key\n(no common factors with 26)'].get()))
    # Second key
    key2 = int(entries['Second key\n(0-25)'].get())
    string =  entries['Text to Encrypt'].get()
    string.lower()
    for i in string:
        if(i == " "):
            ciphered = ciphered + i
        else:
            if(i.isupper()):
                i = i.lower()
            a = alpha.index(i) #the index of the original letter in the alphabet
            temp = key*a+key2   #counting the index of a new letter in the alphabet
            while temp > 25:    #When the index of the new letter goes over the index of alphabet-list, it will downscale the index to fit in alphabet
                temp = temp - 26
            ciphered = ciphered + alpha[temp]
    string = ciphered
    entries['Text to Decrypt'].delete(0, tk.END)
    entries['Text to Decrypt'].insert(0, string )

def Decrypt(entries):
    #First key
    deciphered = ""
    key = (int(entries['Key\n(no common factors with 26)'].get()))
    # Second key
    key2 = int(entries['Second key\n(0-25)'].get())
    string = entries['Text to Decrypt'].get()
    string.lower()
    for i in string:
        if(i == " "):
            deciphered = deciphered + i
        else:
            if(i.isupper()):
                i = i.lower()
            a = alpha.index(i) #the index of the original letter in the alphabet
            temp = (26-key)*(a-key2)   #inverse of the encryption key is used to decrypt ie. (26-key)
            while temp > 25 or temp < 0:
                if(temp > 25):    #When the index of the new letter goes over the index of alphabet-list, it will downscale the index to fit in alphabet
                    temp = temp - 26
                elif(temp < 0):
                    temp = temp + 26
            deciphered = deciphered + alpha[temp]
    string = deciphered
    entries['Text to Encrypt'].delete(0, tk.END)
    entries['Text to Encrypt'].insert(0, string )

def makeform(root, fields):
    entries = {}
    for field in fields:
       # print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Affine Cipher 1.0")
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Encrypt',
           command=(lambda e=ents: Encrypt(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Decrypt',
           command=(lambda e=ents: Decrypt(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()


