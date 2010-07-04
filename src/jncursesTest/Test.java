package jncursesTest;

/**
 * TODO:
 * =====
 * make sure that endwin always gets called (shutdown hook).
 * 	in second thought a full shutdown hook for this is a little too much.
 * 	do a reverse order light weight shutdown hook infrastructure and
 * 	have this library use that...
 * add a refresh thread that does a refresh every x milisec (this way the user
 * doesnt need to worry about refreshes - this idea is not as hot as it seems
 * when you first think of it).
 */

import jncurses.Jncurses;

public class Test {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		/*
		 * This is a simple main which initialized, clears the screen
		 * and ends everything
		 */
		Jncurses.initscr();
		Jncurses.clear();
		Jncurses.refresh();
		for(int i=0;i<20;i++) {
			Jncurses.mvaddstr(i,i,"hello "+i);
			Jncurses.refresh();
			try {
				Thread.sleep(1000);
			} catch(Exception e) {
				throw new RuntimeException(e);
			}
		}
		Jncurses.endwin();
	}
}
