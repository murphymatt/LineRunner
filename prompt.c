#include <stdio.h>
#include <string.h>
#include "speechFunctions.h"

int main() {
  speakText();
  return 0;
}

int speakText() {
  char *text = "hello world! this is a string that I would like to speak";
  int len = strlen(text);

  speakInit();

  speak(text, len);

  speakCleanup();
  
}
