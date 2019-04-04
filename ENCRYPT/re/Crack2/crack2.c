
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main()
{
    int character;
    int counter;
    int counter2;
    char password [9];
    char username [9];
    char result [9];
    

    int fd;

    read(fd, &username, 8);
    read(fd, &password, 8);

    counter = 0;
    while (counter < 9) {
        result[counter] = password[counter] ^ username[counter];
        counter = counter + 1;
    }
    counter2 = 0;

    character = 0;
    while (counter2 < 9) {
        character = character + result[counter2] + counter2 * -4;
        counter2 = counter2 + 1;
    }

    printf("%d\n", character);
    
    //FUNCTION_CALL(character)
}


undefined8 FUN_0010073a(uint uParm1)
{
  undefined8 FLAG;
  
  FLAG = 0x12e91d141f0e0308;

  int counter = 0;
  while (counter < 0x1f) {
    putchar((int)*(char *)(&FLAG + counter) ^ uParm1);
    counter = counter + 1;
  }
  return 0;
}