TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

QMAKE_CXXFLAGS += -fopenmp
LIBS += -fopenmp
QMAKE_CXXFLAGS_RELEASE += -O3

SOURCES += main.cpp
