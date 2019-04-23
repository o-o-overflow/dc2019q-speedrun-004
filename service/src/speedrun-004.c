#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 

   Compilation:
   gcc -o speedrun-004 -no-pie -fno-stack-protector -static speedrun-004.c && strip speedrun-004

 */

void say_hello()
{
   printf("i think i'm getting better at this coding thing.\n");
}

void say_goodbye()
{
   printf("see ya later slowpoke.\n");
}

void get_their_stuff(int size)
{
   char buf[256];
   buf[0] = '\0';
   printf("Ok, what do you have to say for yourself?\n");
   read(0, buf, size);
   printf("Interesting thought \"%s\", I'll take it into consideration.\n", buf);
}

void what_do_they_say()
{
   char num[10];
   int size;
   printf("how much do you have to say?\n");
   read(0, num, 9);
   num[9] = '\0';

   size = atoi(num);

   if (size <= 0)
   {
	  printf("That's not much to say.\n");
	  return;
   }
   if (size > 257)
   {
	  printf("That's too much to say!.\n");
	  return;
   }

   get_their_stuff(size);
}


int main(int argc, char** argv)
{
   setvbuf(stdout, NULL, _IONBF, 0);

   say_hello();
   what_do_they_say();
   say_goodbye();
}
