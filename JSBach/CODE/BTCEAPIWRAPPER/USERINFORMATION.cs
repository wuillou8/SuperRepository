using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class USERINFORMATION
    {
        public FUNDS Funds { get; private set; }
        public RIGHTS Rights { get; private set; }
        public int TransactionCount { get; private set; }
        public int OpenOrders { get; private set; }
        public int ServerTime { get; private set; }

        private USERINFORMATION() { }
        public static USERINFORMATION ReadFromJObject(JObject o)
        {
            return new USERINFORMATION()
            {
                Funds = FUNDS.ReadFromJObject(o["funds"] as JObject),
                Rights = RIGHTS.ReadFromJObject(o["rights"] as JObject),
                TransactionCount = o.Value<int>("transaction_count"),
                OpenOrders = o.Value<int>("open_orders"),
                ServerTime = o.Value<int>("server_time")
            };
        }
    }
}
