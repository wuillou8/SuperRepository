using System;

namespace BTCEAPIWRAPPER
{
    public enum TRADEINFORMATIONTYPE
    {
        ASK,
        BID
    }

    public class TRADEINFORMATIONTYPEHELPER
    {
        public static TRADEINFORMATIONTYPE FromString(string s)
        {
            switch (s)
            {
                case "ask":
                    return TRADEINFORMATIONTYPE.ASK;
                case "bid":
                    return TRADEINFORMATIONTYPE.BID;
                default:
                    throw new ArgumentException();
            }
        }
    }
}
