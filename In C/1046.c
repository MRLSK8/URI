#include <stdio.h>
int main(void){
  int i, f;
  
  for(;;){
    scanf("%d %d", &i, &f);
    printf("O JOGO DUROU %d HORA(S)\n", (i >= f) ? ((24 - i) + f) : (f - i));
  };
  return 0;
}