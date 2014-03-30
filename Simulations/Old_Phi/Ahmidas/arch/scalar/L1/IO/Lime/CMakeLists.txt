SET(Sources_Reader Reader/Reader.cpp Reader/Reader_Reader.cpp)
SET(Sources_Writer Writer/Writer.cpp Writer/Writer_finalize.cpp Writer/Writer_newRecord.cpp
                   Writer/Writer_reserveHeader.cpp)
ADD_LIBRARY(Lime ${Sources_Reader} ${Sources_Writer})
