AC_INIT(jncurses,0.2,Mark Veltzer <mark.veltzer@gmail.com>)
AC_CANONICAL_HOST()
AC_CANONICAL_TARGET()
AC_CONFIG_SRCDIR(jncurses.i)

# find standard programs
AC_PROG_CC()
dnl AC_PROG_CXX()
dnl AC_PROG_CPP()
dnl AC_PROG_INSTALL()

m4_include(/usr/share/aclocal/ac_pkg_swig.m4)
AC_PROG_SWIG()

m4_include(/usr/share/aclocal/ac_prog_java.m4)
m4_include(/usr/share/aclocal/ac_prog_java_works.m4)
m4_include(/usr/share/aclocal/ac_prog_javac.m4)
m4_include(/usr/share/aclocal/ac_prog_javac_works.m4)
m4_include(/usr/share/aclocal/ac_prog_javadoc.m4)
m4_include(/usr/share/aclocal/ac_prog_javah.m4)
m4_include(/usr/share/aclocal/ac_prog_jar.m4)
m4_include(/usr/share/aclocal/ac_jni_include_dir.m4)
# the next two lines are needed because otherwise we would find gcj
JAVA=java
JAVAC=javac
AC_PROG_JAVAC()
AC_PROG_JAVA()
AC_PROG_JAVADOC()
AC_PROG_JAVAH()
AC_PROG_JAR()
AC_JNI_INCLUDE_DIR()
AC_SUBST(JNI_INCLUDE_DIRS)

AC_CHECK_LIB(ncurses,initscr)
AC_CHECK_LIB(ncursesw,initscr)
AC_CHECK_LIB(form,form_init)
AC_CHECK_LIB(formw,form_init)
AC_CHECK_LIB(menu,menu_init)
AC_CHECK_LIB(menuw,menu_init)
AC_CHECK_LIB(panel,new_panel)
AC_CHECK_LIB(panelw,new_panel)

AC_OUTPUT(Makefile)