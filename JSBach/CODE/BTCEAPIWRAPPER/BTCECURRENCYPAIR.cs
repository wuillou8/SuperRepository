using System;

namespace BTCEAPIWRAPPER
{
    public enum BTCECURRENCYPAIR
    {
        BTC_EUR,
        BTC_USD,
        BTC_JPY,
        USD_EUR,
        JPY_USD,
        JPY_EUR,
        UNFUCKINKNOW
    }
    public class BTCECURRENCYPAIRHELPER
    {
        public static BTCECURRENCYPAIR FromString(string s)
        {
            BTCECURRENCYPAIR ret = BTCECURRENCYPAIR.UNFUCKINKNOW;
            Enum.TryParse<BTCECURRENCYPAIR>(s.ToLowerInvariant(), out ret);
            return ret;
        }
        public static string ToString(BTCECURRENCYPAIR v)
        {
            return Enum.GetName(typeof(BTCECURRENCYPAIR), v).ToLowerInvariant();
        }
    }
}
