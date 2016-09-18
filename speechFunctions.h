/**
 Credit goes to Apex Logic for these functions
 **/

#include <stdio.h>
#include <string.h>
#include <espeak/speak_lib.h>

//don't delete this callback function.
int SynthCallback(short *wav, int numsamples, espeak_EVENT *events) {
  return 0;
}

int speakInit() {
  //must be called before any other functions
  //espeak initialize
  if (espeak_Initialize(AUDIO_OUTPUT_SYNCH_PLAYBACK,
			0, NULL ,espeakINITIALIZE_PHONEME_EVENTS) < 0) {
    puts("could not initialize espeak\n");
    return -1;
  }
  espeak_SetSynthCallback(SynthCallback);
  return 0;
}

void speakCleanup() {
  espeak_Terminate();
}

//takes in a char array and length, will speak the words. 
int speak(char * cp, int len) {
  espeak_ERROR speakErr;

  if((speakErr=espeak_Synth(cp, len, 0,0,0,espeakCHARS_AUTO,NULL,NULL))!= EE_OK) {
    printf("error on synth\n");
    return -1;
  }
    
  return 0;
}


//changes the base pitch, accepts values within 0-100
int changePitch(int newVal) {
  espeak_ERROR sErr;
    
  if(newVal < 0) {
    newVal = 0;
  }
  if(newVal > 100) {
    newVal = 100;
  }
        
  if((sErr=espeak_SetParameter(espeakPITCH, newVal, 0)) != EE_OK) {
    printf("error while setting espeak parameters\n");
    return -1;
  }
  return 0;
}


//changes the range of pitch within the voice accepts values within 0-100, 50 is normal
int changeRange(int newVal) {
  espeak_ERROR sErr;
    
  if(newVal < 0) {
    newVal = 0;
  }
  if(newVal > 100) {
    newVal = 100;
  }
    
  if((sErr=espeak_SetParameter(espeakRANGE, newVal, 0)) != EE_OK) {
    printf("error while setting espeak parameters\n");
    return -1;
  }
  return 0;
}


//changes word speed values should be bwtween 80 and 450. 
int changeWordSpeed(int newVal) {
  espeak_ERROR sErr;
    
  if(newVal < 80) {
    newVal = 80;
  }
  if(newVal > 450) {
    newVal = 450;
  }
        
  if((sErr=espeak_SetParameter(espeakRATE, newVal, 0)) != EE_OK) {
    printf("error while setting espeak parameters\n");
    return -1;
  }
  return 0;
}
