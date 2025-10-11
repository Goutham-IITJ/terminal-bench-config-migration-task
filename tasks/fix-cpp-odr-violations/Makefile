CXX := g++
CXXFLAGS := -std=c++17 -O2 -Wall -Wextra -Iinclude
LDFLAGS :=

SRC := $(wildcard src/*.cpp)
OBJDIR := build
BINDIR := bin
OBJS := $(patsubst src/%.cpp,$(OBJDIR)/%.o,$(SRC))

.PHONY: all clean

all: $(BINDIR)/demo

$(BINDIR)/demo: $(OBJS) | $(BINDIR)
	$(CXX) $(OBJS) $(LDFLAGS) -o $@

$(OBJDIR)/%.o: src/%.cpp | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $(OBJDIR)

$(BINDIR):
	mkdir -p $(BINDIR)

clean:
	rm -rf $(OBJDIR) $(BINDIR)
