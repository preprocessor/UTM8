from base64 import b64encode
from tkinter import filedialog as fd
with open("icon.ico", "rb") as image_file:
    encoded_string = b64encode(image_file.read())
# print(encoded_string)

filetypes = (
  ('HTML files', '*.html'),
  ('text files', '*.txt'),
  ('All files', '*.*')
) #^ file types for dialogs


f = fd.asksaveasfile(mode='w', filetypes=filetypes, defaultextension='*.html')

f.write(str(encoded_string))
f.close()