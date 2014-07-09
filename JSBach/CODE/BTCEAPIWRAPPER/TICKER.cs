
using Newtonsoft.Json.Linq;
using System;
using System.IO;

namespace BTCEAPIWRAPPER
{
    public class TICKER
    {
        public static System.DateTime dtDateTime = new DateTime(1970, 1, 1, 0, 0, 0, 0);
        public decimal Average { get; private set; }
        public decimal Buy { get; private set; }
        public decimal High { get; private set; }
        public decimal Last { get; private set; }
        public decimal Low { get; private set; }
        public decimal Sell { get; private set; }
        public decimal Volume { get; private set; }
        public decimal VolumeCurrent { get; private set; }
        public Int32 updated { get; private set; }
        public System.DateTime ServerTime { get; private set; }
        public static TICKER ReadFromJObject(JObject o)
        { // useful when writing to csv files, will be deprecated when writing to xls files
            if (o == null)
                return null;
            return new TICKER()
            {
                Average = o.Value<decimal>("avg"),
                Buy = o.Value<decimal>("buy"),
                High = o.Value<decimal>("high"),
                Last = o.Value<decimal>("last"),
                Low = o.Value<decimal>("low"),
                Sell = o.Value<decimal>("sell"),
                Volume = o.Value<decimal>("vol"),
                VolumeCurrent = o.Value<decimal>("vol_cur"),
                updated = o.Value<Int32>("updated"),
                ServerTime = dtDateTime.AddSeconds(o.Value<Int32>("updated")).ToLocalTime(), // risk that the 1st o.Value<Int32>("updated") is not equal to the 2nd one
            };
        }
        public string CreateTickerString()
        {
            string TickerString = Convert.ToString(Average) + ",\t ";
            TickerString += Convert.ToString(Buy) + ",\t ";
            TickerString += Convert.ToString(High) + ",\t ";
            TickerString += Convert.ToString(Low) + ",\t ";
            TickerString += Convert.ToString(Sell) + ",\t ";
            TickerString += Convert.ToString(Volume) + ",\t ";
            TickerString += Convert.ToString(VolumeCurrent) + ",\t ";
            TickerString += Convert.ToString(updated) + ",\t ";
            TickerString += Convert.ToString(ServerTime);
            return TickerString;
        }
    }
}
