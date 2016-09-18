from listener import Listener
import re
FILENAME = "SCRIPT"

def main():
  script = open(FILENAME, 'r')
  character = raw_input('Which character will you be reading? ')
  prompt = get_next_prompt(character, script)

  while prompt != None:
    present(prompt)
    prompt = get_next_prompt(character, script)

  print "All done!"
  
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

def present(prompt, tries_allowed = 3):
  if prompt[0] == None:
    print "Lights up!"
  else:
    print prompt[0][0] + ": " + prompt[0][1]
  listener = Listener()
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
  return present(prompt, tries_allowed)

def verify(expected, spoken):
  e = re.sub('[!?.,:;]', '', expected)
  s = re.sub('[!?.,:;]', '', spoken)
  return e.lower() == s.lower()
