PROJECT := emd_c

DEBUG := -Wall -g -O3

GCC ?= cc
CCFLAGS := -arch x86_64
LDFLAGS := 

SRC = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SRC))

all: $(PROJECT)

%.o: %.c 
	$(GCC) $(DEBUG) -c $< -o $@ $(CCFLAGS)

$(PROJECT): $(OBJS) 
	$(GCC) $(DEBUG) $(OBJS) -o $@ $(LDFLAGS)

clean: 
	rm -f *.o $(PROJECT)




