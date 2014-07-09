using System;

namespace BTCEAPIWRAPPER
{
    public enum BTCECURRENCY
    {
        BTC,
        EUR,
        USD,
        JPY,
        UNFUCKINKNOWN
    }

    class BTCECURRENCYHELPER
    {
        public static BTCECURRENCY FromString(string s)
        {
            BTCECURRENCY ret = BTCECURRENCY.UNFUCKINKNOWN;
            Enum.TryParse<BTCECURRENCY>(s, out ret);
            return ret;
        }
        public static string ToString(BTCECURRENCY v)
        {
            return Enum.GetName(typeof(BTCECURRENCY), v);
        }
    }
}
