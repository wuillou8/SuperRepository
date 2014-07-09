using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class CANCELORDERANSWER
    {
        public int OrderId { get; private set; }
		public FUNDS FUNDS { get; private set; }

        private CANCELORDERANSWER() { }
        public static CANCELORDERANSWER ReadFromJObject(JObject o)
        {
            return new CANCELORDERANSWER()
            {
                FUNDS = FUNDS.ReadFromJObject(o["funds"] as JObject),
				OrderId = o.Value<int>("order_id")
			};
		}
    }
}
