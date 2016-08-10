# getting tools from autoconf
JAVAC=@JAVAC@
JAVAH=@JAVAH@
JAVA=@JAVA@
JAVADOC=@JAVADOC@
JAR=@JAR@
CC=@CC@
CXX=@CXX@
SWIG=@SWIG@
JNI_INCLUDE_DIRS=@JNI_INCLUDE_DIRS@
LIBS=@LIBS@
PACKAGE_NAME=@PACKAGE_NAME@
# how do we get this from autoconf ?
RM=rm
ECHO=echo
MKDIR=mkdir
RMDIR=rmdir
#TEST_RUN_ARGS=-verbose:jni -Xcheck:jni -Xcheck:nabounds
TEST_RUN_ARGS=
SWIGFLAGS=

# causes seconday targets not to be deleted
.SECONDARY:

# select the type of compilation here (c/cpp)
# notice that optimization level depends on C/CPP selection
# because of a bug in swig which produces code with warnings
# under C which cannot be opimized using -O2
LINK=$(CC)
SUFFIX=c
SWIGFLAGS=
OPLEVEL=-O2 -fno-strict-aliasing -fPIC
SWIGFLAGS+=-Wall -Werror
# -Wno-unused-but-set-variable

# here come the real targets
sourcesi=$(shell find . -name "*.i")
SOURCES_B=$(basename $(sourcesi))
SOURCES_C=$(addsuffix _wrap.$(SUFFIX),$(SOURCES_B))
SOURCES_O=$(addsuffix _wrap.o,$(SOURCES_B))
C_INCLUDES=$(addprefix -I,$(JNI_INCLUDE_DIRS))
# -O2 creates compilation errors
CFLAGS+=-Wall -Werror -Wno-unused-but-set-variable -Wno-unused-function $(OPLEVEL) -shared $(C_INCLUDES)
JAVA_FLAGS=-Xlint:deprecation -Xlint:unchecked
OUTLIB=lib$(PACKAGE_NAME).so
OUTJAR=$(PACKAGE_NAME).jar
OUTTEST=test.jar
MAINCLASS=jncursesTest.Test
AUTOSRCPATH=autosrc
AUTOCLASSES=autobin
SRCPATH=src
CLASSES=bin
SWIGPATH=$(AUTOSRCPATH)/$(PACKAGE_NAME)
DOC=doc
SOURCES_T=$(shell find $(SRCPATH) -name "*.java")

# the total outcome is what we need for the user: jar and so
# notice that the C/CXX sources which will be generated are not provided
# to the user (the user does not need them) and, consequently, will be
# deleted by make because of the use of implicit rules which cause make
# to treat them as by products which are to be deleted after producing
# the targets
default: $(OUTLIB) $(OUTJAR)

# linking the o files to a single shared lib
$(OUTLIB): $(SOURCES_O)
	$(LINK) $(CFLAGS) -o $(OUTLIB) $(SOURCES_O) $(LIBS)

$(OUTJAR): $(OUTLIB)
	$(MKDIR) -p $(AUTOCLASSES)
	$(JAVAC) -Xlint:deprecation -Xlint:unchecked -d $(AUTOCLASSES) -sourcepath $(AUTOSRCPATH) `find $(AUTOSRCPATH) -name "*.java"`
	$(JAR) -cf $(OUTJAR) -C $(AUTOCLASSES) .
docs: $(DOC)/index.html
$(DOC)/index.html: $(SOURCES)
	$(JAVADOC) -quiet -classpath $(AUTOCLASSES) -sourcepath $(AUTOSRCPATH) -d $(DOC) $(PACKAGE_NAME)
clean:
	-$(RM) -rf $(OUTLIB) $(OUTJAR) $(OUTTEST) $(DOC) $(CLASSES) $(AUTOCLASSES) $(AUTOSRCPATH) $(SOURCES_C) $(SOURCES_O)
distclean: clean
	-$(RM) -rf autom4te.cache config.cache config.status config.log Makefile aclocal.m4 missing
allclean: distclean
	-$(RM) -rf configure config.sub config.guess install-sh
$(OUTTEST): $(OUTJAR) $(SOURCES_T)
	$(MKDIR) -p $(CLASSES)
	$(JAVAC) -classpath $(OUTJAR) -Xlint:deprecation -Xlint:unchecked -d $(CLASSES) -sourcepath $(SRCPATH) $(SOURCES_T)
	$(JAR) -cf $(OUTTEST) -C $(CLASSES) .
test: $(OUTTEST)
	LD_LIBRARY_PATH=. $(JAVA) $(TEST_RUN_ARGS) -classpath $(OUTTEST):$(OUTJAR) $(MAINCLASS)

%_wrap.$(SUFFIX): %.i
	$(MKDIR) -p $(SWIGPATH)
	$(SWIG) $(SWIGFLAGS) -java -outdir $(SWIGPATH) -package $(PACKAGE_NAME) $<
%.o: %.cxx
	$(CXX) -c $< -o $@

# first show the tools
debug:
	$(ECHO) $(JAVAC) $(JAVAH) $(JAVA) $(JAVADOC) $(JAR) $(CC) $(CXX) $(SWIG) $(JNI_INCLUDE_DIRS) $(LIBS) $(PACKAGE_NAME) $(RM) $(ECHO)
	$(ECHO) $(sourcesi) $(SOURCES_B) $(SOURCES_C) $(SOURCES_O) $(C_INCLUDES) $(C_FLAGS) $(JAVA_FLAGS) $(OUTLIB) $(OUTJAR)
