#define _XOPEN_SOURCE_EXTENDED 1
#include <ncursesw/curses.h>
#include <ncursesw/term.h>
#include <ncursesw/panel.h>
#include <ncursesw/menu.h>
#include <ncursesw/form.h>
#include <unistd.h>
#include <locale.h>

/* This is an ncurses playground in C/C++ so that I could test exactly what
 * ncurses is and how it works */

void func(chtype u) {
}

void diagonal() {
	for(int i=0;i<20;i++) {
		mvaddch(i,i,i+1488);
		refresh();
		sleep(1);
	}
}

int main(int argc,char** argv,char** envp) {
	setlocale(LC_ALL,"");
	WINDOW* stdscr=initscr();
	curs_set(0);
	int nh, nw;
	getmaxyx(stdscr,nh,nw);
	clear();
	move(0,0);
	refresh();
	chtype c=0;
	while(true) {
		for(int x=0;x<nw;x++) {
			for(int y=0;y<nh;y++) {
				mvwaddch(stdscr,y,x,c);
				c++;
			}
		}
		refresh();
		getch();
	}
	endwin();
	return 0;
}
