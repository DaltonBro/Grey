
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int strL();
char concat();
void replace();

int main(int argc, char * argv[]) {
	printf("Arguments Passed - 1: %s  - 2: %s  - 3: %s\n", argv[1], argv[2], argv[3]);

	printf("Lets get started, first is strL \n");
	strL(argv[1]);
	printf("Next is Concatenate \n");
	concat(argv[1],argv[2]);
	printf("Finally we have Replace \n");
	replace(argv[1],argv[2],argv[3]);

	exit(0);
}


int strL(char * s){
	int check = strlen(s);
	printf("With built in Function strlen: %d\n",check);
	int i = 0;
	while(s[i] != '\0') {
		i++;
	}
	printf("With my while loop: %d\n",i);

}


char concat(char * a, char * b){
	char * cat = (char *) malloc(sizeof(char) * 25);
	strncpy(cat,a,25);
	strcat(cat,b);
	printf("Strcat Function: %s\n", cat);
	
	char * join = (char *) malloc(sizeof(char) * 25);
	strncpy(join,a,25);
	for(int i = 0; i<=strlen(b); i++){
		join[i+strlen(a)] = b[i];
	}
	printf("My For Loop version: %s\n",join);

}


void replace(char * s, char * a, char * b){
	
	
	
	if(strlen(s) > strlen(a)) {
		for(int i = 0; i<=strlen(a); i++){
			s[i] = a[i];			
		}
		for(int x = 0; x<=(strlen(s)-strlen(a)-1); x++){
			s[x+strlen(a)] = b[x];
		}
	}
	else{
		for(int t = 0; t<=strlen(a); t++){
			s[t] = a[t];
		}
	}
	
	printf("Replacing first argument with new chars: %s\n",s);

}



