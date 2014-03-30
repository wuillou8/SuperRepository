#pragma once


#include <L0/Base/Random.h>

//////////////////////////////////////////////////////////////////////////
//  The Box-Mueller algo. generates randomly 				//
//  normal distributed numbers: 					//
//  http://www.taygeta.com/random/boxmuller.html                        //
//////////////////////////////////////////////////////////////////////////

namespace Base
{
class BoxMueller
{
public:
 static float box_mueller(float m, float s);
};
}


