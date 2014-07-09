using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;   

namespace BTCEAPIWRAPPER
{
    public class TRANSACTION
    {
        public int Type { get; private set; }
        public decimal Amount { get; private set; }
        public BTCECURRENCY Currency { get; private set; }
        public string Description { get; private set; }
        public int Status { get; private set; }
        public UInt32 Timestamp { get; private set; }

        public static TRANSACTION ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new TRANSACTION()
            {
                Type = o.Value<int>("type"),
                Amount = o.Value<decimal>("amount"),
                Currency = BTCECURRENCYHELPER.FromString(o.Value<string>("currency")),
                Timestamp = o.Value<UInt32>("timestamp"),
                Status = o.Value<int>("status"),
                Description = o.Value<string>("desc")
            };
        }
    }

    public class TRANSACTIONHISTORY
    {
        public Dictionary<int, TRANSACTION> List { get; private set; }
        public static TRANSACTIONHISTORY ReadFromJObject(JObject o)
        {
            return new TRANSACTIONHISTORY()
            {
                List = o.OfType<KeyValuePair<string, JToken>>().ToDictionary(a => int.Parse(a.Key), a => TRANSACTION.ReadFromJObject(a.Value as JObject))
            };
        }
    }
}
