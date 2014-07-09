using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;

namespace BTCEAPIWRAPPER
{
    public class TRADE
    {
        public BTCECURRENCYPAIR Pair { get; private set; }
        public TRADETYPE Type { get; private set; }
        public decimal Amount { get; private set; }
        public decimal Rate { get; private set; }
        public int OrderId { get; private set; }
        public bool IsYourOrder { get; private set; }
        public UInt32 Timestamp { get; private set; }
        public static TRADE ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new TRADE()
            {
                Pair = BTCECURRENCYPAIRHELPER.FromString(o.Value<string>("pair")),
                Type = TRADETYPEHELPER.FromString(o.Value<string>("type")),
                Amount = o.Value<decimal>("amount"),
                Rate = o.Value<decimal>("rate"),
                Timestamp = o.Value<UInt32>("timestamp"),
                IsYourOrder = o.Value<int>("is_your_order") == 1,
                OrderId = o.Value<int>("order_id")
            };
        }
    }
    public class TRADEHISTORY
    {
        public Dictionary<int, TRADE> List { get; private set; }
        public static TRADEHISTORY ReadFromJObject(JObject o)
        {
            return new TRADEHISTORY()
            {
                List = o.OfType<KeyValuePair<string, JToken>>().ToDictionary(item => int.Parse(item.Key), item => TRADE.ReadFromJObject(item.Value as JObject))
            };
        }
    }
}
