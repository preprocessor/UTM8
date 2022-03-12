from base64 import b64encode
from tkinter import filedialog as fd

open_filetypes = (
  ('ICO Files (*.ico)', '*.ico'),
  ('All Files', '*.*')
)

save_filetypes = (
  ('Text File (*.txt)', '*.txt'),
  ('All Files', '*.*')
)


original_file =  fd.askopenfilename(filetypes=open_filetypes)

with open(original_file, "rb") as image_file:
    encoded_string = b64encode(image_file.read())

processed_file = fd.asksaveasfile(mode='w', filetypes=save_filetypes)

processed_file.write(str(encoded_string))
processed_file.close()