using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;

namespace BTCEAPIWRAPPER
{
    public class ORDER
    {
        public BTCECURRENCYPAIR Pair { get; private set; }
        public TRADETYPE Type { get; private set; }
        public decimal Amount { get; private set; }
        public decimal Rate { get; private set; }
        public UInt32 TimestampCreated { get; private set; }
        public int Status { get; private set; }
        public static ORDER ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new ORDER()
            {
                Pair = BTCECURRENCYPAIRHELPER.FromString(o.Value<string>("pair")),
                Type = TRADETYPEHELPER.FromString(o.Value<string>("type")),
                Amount = o.Value<decimal>("amount"),
                Rate = o.Value<decimal>("rate"),
                TimestampCreated = o.Value<UInt32>("timestamp_created"),
                Status = o.Value<int>("status")
            };
        }
    }

    public class ORDERLIST
    {
        public Dictionary<int, ORDER> List { get; private set; }
        public static ORDERLIST ReadFromJObject(JObject o)
        {
            return new ORDERLIST()
            {
                List = o.OfType<KeyValuePair<string, JToken>>().ToDictionary(item => int.Parse(item.Key), item => ORDER.ReadFromJObject(item.Value as JObject))
            };
        }
    }
}
