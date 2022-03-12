import argparse, re, pyperclip

desc = 'Tool for bulk UTM manipulation'

parser = argparse.ArgumentParser(description = desc)

input = parser.add_mutually_exclusive_group(required=True)
input.add_argument('-f', '--file', help = 'Read from file')
input.add_argument('-c', '--clipboard', action = 'store_true', help = 'Read from clipboard')

parser.add_argument('UTM', help = 'UTM string')

args = parser.parse_args()


if '&amp;' not in args.UTM:
  utm = args.UTM.replace('&','&amp;')
else:
  utm = args.UTM



def resplit(z):
  return re.split(r'(https?://(?:[\w]|[\d]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', z)

def append(z):
  for i in range(len(z)):
    if re.match(r'(https?://(?:[\w]|[\d]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', z[i]):
      if '&amp;' not in z[i]:
        z[i] += utm
      else:
        z[i] += utm.replace('?', '&amp;')

  return z

if args.file:
  # print('Args: {F} %s' % args.UTM)
  with open(args.file) as f:
    file = f.read()

  data = resplit(file)
  f.close()

  output = ''.join(append(data))

  pyperclip.copy(output)

if args.clipboard:
  # print('Args: {C} %s' % args.UTM)
  clip   = pyperclip.paste()
  data   = resplit(clip)
  output = ''.join(append(data))
  pyperclip.copy(output)
