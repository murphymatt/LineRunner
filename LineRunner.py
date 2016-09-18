from listener import listenToSpeech

FILENAME = "SCRIPT"

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
  return (cue, line)

def main():
  script = open(FILENAME, 'r')
  character = raw_input('Which character will you be reading? ')
  prompt = get_next_prompt(character, script)
  present(prompt)

def present(prompt):
  print prompt[0][0] + ": " + prompt[0][1]
  response = listenToSpeech()
  if verify(prompt[1][1], response):
    print "You correctly responded: " + response
    return;
  else:
    print "Heard: " + response 

def verify(expected, spoken):
  return expected.lower() == spoken.lower()
