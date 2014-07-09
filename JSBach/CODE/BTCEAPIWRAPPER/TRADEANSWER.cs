using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class TRADEANSWER
    {
        public decimal Received { get; private set; }
        public decimal Remains { get; private set; }
        public int OrderId { get; private set; }
        public FUNDS Funds { get; private set; }

        private TRADEANSWER() { }
        public static TRADEANSWER ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new TRADEANSWER()
            {
                Funds = FUNDS.ReadFromJObject(o["funds"] as JObject),
                Received = o.Value<decimal>("received"),
                Remains = o.Value<decimal>("remains"),
                OrderId = o.Value<int>("order_id")
            };
        }
    }
}
