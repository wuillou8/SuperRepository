using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class ORDERINFORMATION
    {
        public decimal Price { get; private set; }
        public decimal Amount { get; private set; }
        public static ORDERINFORMATION ReadFromJObject(JArray o)
        {
            if (o == null)
                return null;
            return new ORDERINFORMATION()
            {
                Price = o.Value<decimal>(0),
                Amount = o.Value<decimal>(1),
            };
        }
    }

    public class DEPTH
    {
        public List<ORDERINFORMATION> Asks { get; private set; }
        public List<ORDERINFORMATION> Bids { get; private set; }
        public static DEPTH ReadFromJObject(JObject o)
        {
            return new DEPTH()
            {
                Asks = o["asks"].OfType<JArray>().Select(order => ORDERINFORMATION.ReadFromJObject(order as JArray)).ToList(),
                Bids = o["bids"].OfType<JArray>().Select(order => ORDERINFORMATION.ReadFromJObject(order as JArray)).ToList()
            };
        }
    }
}
