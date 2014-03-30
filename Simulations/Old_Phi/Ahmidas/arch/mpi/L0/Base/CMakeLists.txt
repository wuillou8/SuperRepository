SET(Sources_Weave Weave.h Weave/Weave_Weave_a.cpp Weave/Weave_Weave_b.cpp Weave/Weave_sumOverTimeSlices_a.cpp Weave/Weave_rank.cpp)
ADD_LIBRARY(Weave $ {Sources_Weave})
TARGET_LINK_LIBRARIES(Weave Base Grid)

SET(Sources_Grid Grid.h Grid/Grid_Grid_a.cpp Grid/Grid_rank.cpp Grid/Grid_initContiguousBlock.cpp Grid/Grid_greatestCommonDivisor.cpp Grid/Grid.cpp)
ADD_LIBRARY(Grid $ {Sources_Grid})
TARGET_LINK_LIBRARIES(Grid Base)

# ADD_SUBDIRECTORY(IO)
