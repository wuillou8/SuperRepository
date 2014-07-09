using BTCEAPIWRAPPER.UTILS;
using Newtonsoft.Json.Linq;
using System;

namespace BTCEAPIWRAPPER
{
    public class TRADEINFORMATIONv2
    {
        public decimal Amount { get; private set; }
        public DateTime Date { get; private set; }
        public BTCECURRENCY Item { get; private set; }
        public decimal Price { get; private set; }
        public BTCECURRENCY PriceCurrency { get; private set; }
        public UInt32 Tid { get; private set; }
        public TRADEINFORMATIONTYPE Type { get; private set; }

        public static TRADEINFORMATIONv2 ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;

            return new TRADEINFORMATIONv2()
            {
                Amount = o.Value<decimal>("amount"),
                Price = o.Value<decimal>("price"),
                Date = UNIXTIME.ConvertToDateTime(o.Value<UInt32>("date")),
                Item = BTCECURRENCYHELPER.FromString(o.Value<string>("item")),
                PriceCurrency = BTCECURRENCYHELPER.FromString(o.Value<string>("price_currency")),
                Tid = o.Value<UInt32>("tid"),
                Type = TRADEINFORMATIONTYPEHELPER.FromString(o.Value<string>("trade_type"))
            };
        }
    }

    public class TRADEINFORMATIONv3
    {
        public decimal Amount { get; private set; }
        public DateTime Timestamp { get; private set; }
        public decimal Price { get; private set; }
        public UInt32 Tid { get; private set; }
        public TRADEINFORMATIONTYPE Type { get; private set; }

        public static TRADEINFORMATIONv3 ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;

            return new TRADEINFORMATIONv3()
            {
                Amount = o.Value<decimal>("amount"),
                Price = o.Value<decimal>("price"),
                Timestamp = UNIXTIME.ConvertToDateTime(o.Value<UInt32>("timestamp")),
                Tid = o.Value<UInt32>("tid"),
                Type = TRADEINFORMATIONTYPEHELPER.FromString(o.Value<string>("type"))
            };
        }
    }
}
