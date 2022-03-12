import re, os, webbrowser, base64
from datetime import date
import tkinter as tk
from tkinter import PhotoImage, Toplevel, ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

font = ('Segoe UI', 9)

#^---------------------------------------------------------------------------------^#
#^                                      LOGIC                                      ^#
#^---------------------------------------------------------------------------------^#

regex = r'(https?://(?:[\w]|[\d]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

def append(input, utm):
  for i in range(len(input)):
    if re.match(regex, input[i]):
      if '&amp;' not in input[i]:
        input[i] += utm
      else:
        input[i] += utm.replace('?', '&amp;')

  return ''.join(input)

def parse(input, utm):
  data = re.split(regex, input)
  return append(data, utm)

#&---------------------------------------------------------------------------------&#
#&                                   BASE64 IMGS                                   &#
#&---------------------------------------------------------------------------------&#

w_b64 = b'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'
ico_b64 = b'AAABAAIAEBAAAAEAIABoBAAAJgAAACAgAAABACAAqBAAAI4EAAAoAAAAEAAAACAAAAABACAAAAAAAAAEAAAjLgAAIy4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0AAAAhAAAAIQAAABAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGQAAAHgAAACuAAAAkAAAAGgAAABKAAAAJAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALwAAAMMAAAC9AAAAWAAAAEoAAAAYAAAAAAAAAEkAAAC7AAAAMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGQAAAMQAAADDAAAAHAAAAHgAAAD7AAAAfwAAAAAAAACMAAAA/wAAAMMAAAAaAAAAAAAAAAAAAAAAAAAAAAAAAHYAAADwAAAAQwAAAAgAAAC+AAAA/wAAAMIAAAAgAAAAygAAAOgAAAD2AAAAdwAAAAAAAAAAAAAAAAAAAAwAAADEAAAAwgAAAAkAAAAwAAAA6gAAANsAAADmAAAAeQAAAO0AAAB0AAAAyAAAAMQAAAAMAAAAAAAAAAAAAAAdAAAA4gAAAJsAAAAAAAAAbAAAAPYAAABxAAAA3AAAAOgAAADiAAAAJwAAAJsAAADiAAAAHQAAAAAAAAAAAAAAHQAAAOIAAACdAAAABgAAALEAAADhAAAAJQAAAK0AAAD/AAAArwAAAAYAAACdAAAA4gAAAB0AAAAAAAAAAAAAAAwAAADEAAAAygAAACwAAADEAAAAnwAAAAMAAABlAAAA5AAAAGMAAAAPAAAAzAAAAMQAAAAMAAAAAAAAAAAAAAAAAAAAdwAAAPgAAABuAAAAGQAAABEAAAAAAAAACgAAAB4AAAAJAAAAaQAAAPkAAAB3AAAAAAAAAAAAAAAAAAAAAAAAABoAAADEAAAA6wAAAGcAAAAPAAAAAAAAAAAAAAAPAAAAaQAAAOwAAADEAAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAMUAAAD6AAAAzAAAAJ0AAACdAAAAzAAAAPoAAADFAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaAAAAdwAAAMUAAADiAAAA4gAAAMUAAAB3AAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAHQAAAB0AAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//AAD8HwAA8A8AAOBHAADAQwAAwAMAAIABAACIAQAAgAEAAIABAADBAwAAwYMAAOAHAADwDwAA/D8AAP//AAAoAAAAIAAAAEAAAAABACAAAAAAAAAQAAAjLgAAIy4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAXAAAAIgAAACMAAAAZAAAACgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwAAADgAAACAAAAAuQAAANoAAADgAAAA0wAAALwAAACdAAAAbwAA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AGwAAAAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAADgAAACoAAAA7wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA7wAAAKcAAAA3AAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAA6AAAAgQAAALgAAADWAAAA4gAAAOIAAADWAAAAuAAAAIEAAAA5AAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAABcAAAAhAAAAIQAAABcAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/////////////////4D///wAP//wAA//4B+H/8ADA//BAwH/gwMB/wMDAP8GAAD/BgAA/g4AEH4MABB+DAAQfgwQEH4MEDB+CDAwfwAwIP8AOGD/A//A/4H/gf+AfgP/wAAD/+AAB//wAA///AA///+B//////////////////'

def call_ico(parent):
  icon_dec  = base64.b64decode(ico_b64)
  temp_file = 'icon.ico'
  icon_file = open(temp_file, 'wb')

  icon_file.write(icon_dec)
  icon_file.close()

  parent.iconbitmap(temp_file)
  os.remove(temp_file)

#!=================================================================================!#
#!                                   GUI CLASSES                                   !#
#!=================================================================================!#

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('UTM8')
    self.geometry('800x600')
    self.minsize(430,95)
    call_ico(self)

    style = ttk.Style(self)
    style.configure('TCheckbutton', font=font)
    style.configure('TLabel',   font=font)
    style.configure('TButton', font=font)

    self.filetypes = (
      ('HTML Files (*.html)', '*.html'),
      ('Text Files (*.txt)', '*.txt'),
      ('All Files', '*.*')
    ) #^ file types for dialogs

    root_frame = ttk.Frame(self)
    root_frame.pack(fill='both', expand=1, padx=7, pady=7)

    self.file_frame         = File_frame(root_frame)
    self.utm_frame          = Utm_frame(root_frame)
    self.controls_frame     = Controls_frame(root_frame)
    self.input_text_frame   = Text_frame(root_frame, 'Input: ')
    self.output_text_frame  = Text_frame(root_frame, 'Output: ', False)

    self.file_entry         = self.file_frame.entry
    self.utm_entry          = self.utm_frame.entry
    self.input_text         = self.input_text_frame.text_box.text
    self.output_text        = self.output_text_frame.text_box.text

    #* this allows resizing along x axis
    self.file_frame.columnconfigure(0, weight=1)
    self.utm_frame.columnconfigure(0, weight=1)
    self.input_text_frame.columnconfigure(0, weight=1)
    self.output_text_frame.columnconfigure(0, weight=1)
    self.controls_frame.columnconfigure(0, weight=1)

    #* root order
    self.file_frame.rowconfigure(0)
    self.utm_frame.rowconfigure(1)
    self.input_text_frame.rowconfigure(2)
    self.output_text_frame.rowconfigure(3)
    self.controls_frame.rowconfigure(4)

class Label_separator(tk.Frame):
  def __init__(self, parent, text = '', *args):
    tk.Frame.__init__(self, parent, *args)

    self.separator = ttk.Separator(self, orient = tk.HORIZONTAL)
    self.separator.grid(row = 0, column = 0, sticky = 'ew')

    self.label = ttk.Label(self, text = text)
    self.label.grid(row = 0, column = 0, sticky='w', pady=(0,5))

    self.grid_columnconfigure(0, weight=1)

class File_frame(tk.Frame):
  def __init__(self, parent, *args):
    tk.Frame.__init__(self, parent, *args)
    self.pack(fill='x', expand=False, side='top')

    ttk.Label(self, text='File:').pack(side='left', padx=(0,4))

    self.entry = ttk.Entry(self, font=font)
    self.entry.bind('<Return>',self.open_file)

    self.browse_button = ttk.Button(self,
      text='...',
      command=self.locate_file,
      width=3
    )

    self.button_size = 23

    self.entry.pack(fill='x', expand=1, side='left', padx=(0,self.button_size+4))
    self.browse_button.pack()#side='right', padx=(4,0), fill='both')#, ipady=1)
    self.browse_button.place(relx=1.0, anchor='ne', width=self.button_size, height=self.button_size, x=1, y=-1, bordermode='inside')

  def locate_file(self):
    # show the open file dialog
    f = fd.askopenfilename(filetypes=app.filetypes)
    # print the file name into the entry box
    if f != '':
      app.file_entry.delete(0, 'end')
      app.file_entry.insert(0, f)
    self.open_file()

  def open_file(self):
    #* check if a path is present in the file entry box
    if app.file_entry.get() == "":
      return
    #* open the file in read only mode
    f = open(app.file_entry.get(), 'r')
    app.input_text.delete('1.0', 'end')
    #* dump it in the user text box after a wipe
    app.input_text.insert('1.0',f.read())
    f.close()

class Utm_frame(tk.Frame):
  def __init__(self, parent, *args):
    tk.Frame.__init__(self, parent, *args)
    self.pack(fill='x', expand=False, pady=(7,0), side='top')

    ttk.Label(self, text='UTM String:').pack(side='left', padx=(0,4))
    self.entry = ttk.Entry(self, font=font)
    self.entry.pack(side='right', expand=1, fill='x')

class Text_box(tk.Frame):
  def __init__(self, parent, *args):
    tk.Frame.__init__(self, parent, *args)

    self.text = tk.Text(self, wrap='none', height=10)
    self.vsb  = ttk.Scrollbar(self, command=self.text.yview, orient='vertical')
    self.hsb  = ttk.Scrollbar(self, command=self.text.xview, orient='horizontal')
    self.text.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

    self.vsb.pack(side='right', fill='y')
    self.hsb.pack(side='bottom', fill='x')
    self.text.pack(side='left', fill='both', expand=1)

class Text_frame(tk.Frame):
  def __init__(self, parent, title='', edit=True, *args):
    tk.Frame.__init__(self, parent, *args)
    self.pack(fill='both', expand=True)

    self.text_box = Text_box(self)

    Label_separator(self, text=title).pack(fill='x', side='top')

    if not edit:
       self.text_box.text.configure(state='disabled')

    self.text_box.pack(fill='both', expand=1, side='bottom')

class Controls_frame(tk.Frame):
  def __init__(self, parent, *args):
    self.run_box = tk.IntVar()

    ttk.Frame.__init__(self, parent, *args)
    self.pack(fill='x', expand=False, side='bottom', pady=(7,0))

    self.reset_button = ttk.Button(self, text='Reset')
    self.reset_button.bind("<Button-1>", self.reset)
    self.reset_button.bind("<Shift-Button-1>", self.reset_action)

    self.run_button = ttk.Button(self,
      text='Run',
      command=self.run
    )

    self.about_button = ttk.Button(self,
      text='?',
      width=1,
      command=About
    )

    self.copy_button = ttk.Button(self,
      text='Copy',
      command=self.copy
    )

    self.save_button = ttk.Button(self,
      text='Save',
      command=self.save
    )

    self.run_box_cb = ttk.Checkbutton(self,
      text='Run and...',
      variable=self.run_box
    )

    #* left to right order
    self.reset_button.pack(side='left')
    self.run_button.pack(side='left', padx=4)

    #* expand=1 centers here
    self.about_button.pack(side='left', expand=1, padx=(0,4))

    #* right to left order
    self.save_button.pack(side='right')
    self.copy_button.pack(side='right', padx=4)
    self.run_box_cb.pack(side='right')

  def copy_action(self):
    app.clipboard_clear()
    app.clipboard_append(app.output_text.get('1.0','end'))
    app.update()

  def copy(self):
    if self.run_box.get() == 1:
      self.run()
    if not app.output_text.compare('end-1c', '==', '1.0'): #* checks if text is in the output area before wiping clipboard
      self.copy_action()

  def edit_locked(self, text):
    app.output_text.configure(state='normal')
    app.output_text.delete('1.0', 'end')
    app.output_text.insert(1.0, text)
    app.output_text.configure(state='disabled')

  def reset_action(self, *args):
    app.file_entry.delete(0, 'end')
    app.input_text.delete('1.0', 'end')
    app.utm_entry.delete(0, 'end')
    self.edit_locked("")

  def reset(self, *args):
    reset_conf = mb.askquestion('This will clear all text fields!', '       Are you sure?', icon='warning')

    if reset_conf == 'yes':
      self.reset_action()

  def run(self):
    if app.file_entry.get() == '' and app.input_text.compare('end-1c','==', '1.0'):
      mb.showerror('No file or text', 'Browse for a file or paste text into the input area')
      return

    if app.utm_entry.get() == '':
      mb.showerror('No UTM string', 'Enter a string of UTMs in the text box')
      return

    #* if the user hasnt loaded the file or has just pasted a path this will load the file into the user text area
    if app.file_entry.get() != '' and app.input_text.compare('end-1c','==', '1.0'):
      self.open_file()

    output = parse(app.input_text.get('1.0','end'), app.utm_entry.get())
    self.edit_locked(output)

  def save_action(self):
    save_file = fd.asksaveasfile(mode='w', filetypes=app.filetypes, defaultextension='*.html')
    if save_file is None: #^ asksaveasfile returns `None` if dialog closed with 'cancel'.
      return

    data = str(app.output_text.get('1.0','end'))
    save_file.write(data)
    save_file.close()

  def save(self):
    if self.run_box.get() == 1:
      self.run()
    if not app.output_text.compare('end-1c', '==', '1.0'):
      self.save_action()

class About(Toplevel):
  def __init__(self, *args):
    Toplevel.__init__(self, *args)

    self.title('About')
    self.resizable(0,0)
    call_ico(self)

    self.w_photo       = PhotoImage(data=w_b64)
    self.w_logo        = ttk.Label(self, image=self.w_photo)
    self.w_logo.photo  = self.w_photo

    self.text_frame    = ttk.Frame(self)

    self.finished_date = date(2022, 3, 6)
    self.time_delta    = (date.today() - self.finished_date).days
    self.luv_letter    = 'A tool for Adam,\nmade with love,\nby wyspr. <3'
    self.time_message  = 'This tool was made\n' + str(self.time_delta) + ' days ago \non March 6, 2022'

    ttk.Label(self.text_frame, text=self.luv_letter, justify='center').pack(side='top')
    ttk.Label(self.text_frame, text=self.time_message, justify='center').pack(side='bottom')

    self.legal         = ttk.Frame(self)
    ttk.Label(self.legal, text='UTM8 is free software.', justify='center').pack()

    self.controls      = ttk.Frame(self)
    ttk.Button(self.controls, text='wyspr.xyz', command=self.web  ).pack(side='left')
    ttk.Button(self.controls, text='Close',     command=self.close).pack(side='right')

    self.w_logo.grid(row=0, column=0, padx=7, pady=7)
    self.text_frame.grid(row=0, column=1, padx=7, pady=7)
    self.legal.grid(row=1, column=0, columnspan=2, sticky='we')
    self.controls.grid(row=2, column=0, columnspan=2, padx=7, pady=7, sticky='we')

  def web(self):
    webbrowser.open('https://wyspr.xyz')

  def close(self):
    self.destroy()
    self.update()

#*=================================================================================*#
#*                                    MAIN LOOP                                    *#
#*=================================================================================*#

if __name__ == "__main__":
    app = App()
    app.mainloop()