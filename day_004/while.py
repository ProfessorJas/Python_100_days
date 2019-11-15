import tkinter as tk

count = 0

while (count < 9):
    print('The count is: ', count)
    count = count + 1

print("C ya!")

count = 0
while (count < 6):
    print(count, " is less than 6")
    count = count + 1
else:
    print(count, " is not less than 6")

window = tk.Tk()
window.title('Hola')
window.geometry('500x200')

var = tk.StringVar()
l = tk.Label(window, textvariable = var, bg = 'BLUE', font=('Arial', 12), width = 30, height = 2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me')
    else:
        on_hit = False
        var.set('')    
b = tk.Button(window, text = 'JAJA', width = 15, height = 1, command = hit_me)

b.pack()

window.mainloop()
