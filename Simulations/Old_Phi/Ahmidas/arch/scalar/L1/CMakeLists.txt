ADD_SUBDIRECTORY(IO)

SET(Sources_IO  IO/ILDGinfo_ILDGinfo.cpp IO/loadILDG.cpp IO/ScidacChecksum/ScidacChecksum_createTable.cpp IO/ScidacChecksum/ScidacChecksum_parse.cpp
                IO/ScidacChecksum/ScidacChecksum_aggregate.cpp IO/ScidacChecksum/ScidacChecksum_crc32.cpp)
ADD_LIBRARY(IO  ${Sources_IO})
TARGET_LINK_LIBRARIES(IO Base Lime)