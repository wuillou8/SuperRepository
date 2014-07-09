using System;

namespace BTCEAPIWRAPPER
{
    public enum TRADETYPE
    {
        SELL,
        BUY
    }
    public class TRADETYPEHELPER
    {
        public static TRADETYPE FromString(string s)
        {
            switch (s)
            {
                case "sell":
                    return TRADETYPE.SELL;
                case "buy":
                    return TRADETYPE.BUY;
                default:
                    throw new ArgumentException();
            }
        }
        public static string ToString(TRADETYPE v)
        {
            return Enum.GetName(typeof(TRADETYPE), v).ToLowerInvariant();
        }
    }
}
