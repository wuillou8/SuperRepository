using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class FUNDS
    {
        public decimal BTC { get; private set; }
        public decimal EUR { get; private set; }
        public decimal USD { get; private set; }
        public decimal JPY { get; private set; }

        public static FUNDS ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new FUNDS()
            {
                BTC = o.Value<decimal>("btc"),
                USD = o.Value<decimal>("Usd"),
                EUR = o.Value<decimal>("eur"),
                JPY = o.Value<decimal>("jpy"),
            };
        }
    };
}
