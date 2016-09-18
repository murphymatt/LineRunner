#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct LinePair {
  char *character;
  char *line;
} LinePair;

static const char delimiters[] = ":";

int readLine(FILE *file, LinePair *out);

int main(int argc, char *argv[]) {

  FILE *script;  
  switch (argc) {
    case 1: // No arguments, default to file named SCRIPT
      script = fopen("SCRIPT", "r");
      break;
    case 2: // One Argument, use input string as filename
      if ((script = fopen( argv[1], "r" )) == NULL)
       {
          puts( "Can't open input file.\n" );
          exit( 0 );
       }  
  }

  LinePair line; 
  while (readLine(script, &line)){
    printf("%s => %s\n", line.character, line.line); 
  }
  return fclose(script);
}

int readLine(FILE *file, LinePair *out) {
  char read[256];
  char *running;
  if (fgets(read, sizeof read, file) != NULL) {
    running = strdup(read);
    out->character = strsep(&running, delimiters);
    out->line = strsep(&running, delimiters);    
    return 1;
  }
  return 0;
}