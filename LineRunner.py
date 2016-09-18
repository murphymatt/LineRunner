import re

from listener import Listener
from speaker import Speaker

FILENAME = "SCRIPT2"

def main():
  script = open(FILENAME, 'r')
  l = Listener()
  s = Speaker()

  # list character options to user
  print "Characters:\n"
  for person in getCharacters(script):
    print person,
  print '\n'
  character = raw_input('Which character will you be reading? ')
  prompt = get_next_prompt(character, script)

  while prompt != None:
    present(l, s, prompt)
    prompt = get_next_prompt(character, script)

  print "All done!"

def getCharacters(file):
  line = file.readline()
  if '[' not in line:
    line = file.readline()
  return line[1:-2].split(',')
  
def get_next_line(file):
  input = file.readline()
  if input == '':
    return None
  s = input.split(": ")
  character = s[0]
  line = s[1]
  line = line.split('\n')[0]
  return (character, line)

def get_next_prompt(character, file):
  line = get_next_line(file)
  cue = None
  if line == None:
    return None
  skipped_lines = 0
  while (line != None) and (line[0].lower() != character.lower()):
    skipped_lines += 1
    cue = line
    line = get_next_line(file)
  if line == None:
    return None
  return (cue, line)

def present(listener, speaker, prompt, tries_allowed = 3):
  if prompt[0] == None:
    print "Lights up!"
  else:
    speaker.say_line(str(prompt[0][0] + ": " + prompt[0][1]))
#  listener = Listener()
  for i in (1,tries_allowed):
    print "Listening for your line..."
    response = listener.listen_to_speech()
    if verify(prompt[1][1], response):
      print "You correctly responded: " + response
      return;
    else:
      print "Not quite... Try again."
  print "Your line is: " + prompt[1][1]
  print "Try it again!"
  return present(listener, prompt, tries_allowed)

def verify(expected, spoken):
  e = re.sub('[!?.,:;]', '', expected)
  s = re.sub('[!?.,:;]', '', spoken)
  return e.lower() == s.lower()

if __name__=='__main__':
  main()
