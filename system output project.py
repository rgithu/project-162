from tkinter import * 
from PIL import ImageTk, Image

root= Tk();
root.title("HTML IDE")
root.minsize("650","650")
root.maxsize("650","650")
root.configure(background="#b093c4")

open_image = ImageTk.PhotoImage(Image.open ("open.png"))
save_image = ImageTk.PhotoImage(Image.open ("save.png"))
exit_image = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
my_text.configure(background="#d4afed")

name = ""

def open_file() : 
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    html_file = filedialog.askopenfilename(title="Open HTML File", filetypes=(( "Html Files" ,"*.html"),))
    print(html_file)
    name=os.path.basename(html_file)
    formatted_name = name.split(".")[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    html_file.close()
    
    
def save() :
    input_name = input_file_name.get()
    file = open(input_name+".html",'w')
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    messagebox.showinfo("HTML Updated","Success!")

def run_file() :
    global name
    webbrowser.open(name)
    
open_button = Button(root, image=open_image,command= open_file)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()