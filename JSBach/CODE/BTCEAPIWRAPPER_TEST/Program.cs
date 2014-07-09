using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using BTCEAPIWRAPPER;

using Newtonsoft.Json.Serialization;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Utilities;
using Newtonsoft.Json; //.JsonConvert;

using DBMONGO;

using MongoDB.Bson;
using MongoDB.Driver;

using MongoDB.Driver.Builders;
using MongoDB.Driver.GridFS;
using MongoDB.Driver.Linq;

using MongoDB.Bson.IO;
using MongoDB.Bson.Serialization;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson.Serialization.Conventions;
using MongoDB.Bson.Serialization.IdGenerators;
using MongoDB.Bson.Serialization.Options;
using MongoDB.Bson.Serialization.Serializers;
using MongoDB.Driver.Wrappers;


namespace BTCEAPIWRAPPER_TEST
{
    class Program
    {
        static public /*override*/ void pullFromNetIntoDBase_Txt()
        {
            // pull quantities from INet
            var depth3 = BTCEAPIv3WRAPPER.GetDepth(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var ticker3 = BTCEAPIv3WRAPPER.GetTicker(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var trades3 = BTCEAPIv3WRAPPER.GetTrades(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR }, 10000); // 2000 is the limit
            var ticker = BTCEAPIv2WRAPPER.GetTicker(BTCECURRENCYPAIR.BTC_EUR);
            var trades = BTCEAPIv2WRAPPER.GetTrades(BTCECURRENCYPAIR.BTC_EUR);
            var btcusdDepth = BTCEAPIv2WRAPPER.GetDepth(BTCECURRENCYPAIR.BTC_EUR);
            var fee = BTCEAPIv2WRAPPER.GetFee(BTCECURRENCYPAIR.BTC_EUR);
            string APIKEY = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEY;
            string APIKEYSECRET = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEYSECRET;
            var TheBTCEAPIv2WRAPPERObj = new BTCEAPIv2WRAPPER(APIKEY, APIKEYSECRET);
            var info = TheBTCEAPIv2WRAPPERObj.GetInfo();

            string trades_deserial = JsonConvert.SerializeObject(trades);
            string trades3_deserial = JsonConvert.SerializeObject(trades3[0]);
            string btcusdDepthAsks_deserial = JsonConvert.SerializeObject(btcusdDepth.Asks);
            string btcusdDepthBids_deserial = JsonConvert.SerializeObject(btcusdDepth.Bids);

            System.IO.File.WriteAllText(@"C:\data\Trading\trades.json", trades_deserial);
            System.IO.File.WriteAllText(@"C:\data\Trading\trades.json", trades3_deserial);
            System.IO.File.WriteAllText(@"C:\data\Trading\btcusdAsks.json", btcusdDepthAsks_deserial);
            System.IO.File.WriteAllText(@"C:\data\Trading\trades3.json", trades3_deserial);
        }

        /*public void somefunct()
        {

        }*/

        static void Main(string[] args)
        {
            pullFromNetIntoDBase_Txt();
            /*
            var depth3 = BTCEAPIv3WRAPPER.GetDepth(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var ticker3 = BTCEAPIv3WRAPPER.GetTicker(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var trades3 = BTCEAPIv3WRAPPER.GetTrades(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR }, 2000); // 2000 is the limit
            var ticker = BTCEAPIv2WRAPPER.GetTicker(BTCECURRENCYPAIR.BTC_EUR);
            var trades = BTCEAPIv2WRAPPER.GetTrades(BTCECURRENCYPAIR.BTC_EUR);
            var btcusdDepth = BTCEAPIv2WRAPPER.GetDepth(BTCECURRENCYPAIR.BTC_EUR);
            var fee = BTCEAPIv2WRAPPER.GetFee(BTCECURRENCYPAIR.BTC_EUR);
            string APIKEY = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEY;
            string APIKEYSECRET = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEYSECRET;
            var TheBTCEAPIv2WRAPPERObj = new BTCEAPIv2WRAPPER(APIKEY, APIKEYSECRET);
            var info = TheBTCEAPIv2WRAPPERObj.GetInfo();
            
            List<decimal> list = new List<decimal>();
            List<string> listJSON = new List<string>();

            for (int i = 0; i < list.Count; i++) // Loop through List with for
            {
                Console.WriteLine(list[i]);
            }

            // Tests with IO //////////////////////////////////////////////////////////////////////////////////////
            // Write in file, one (long) line:
            string trades_deserial = JsonConvert.SerializeObject(trades);
            System.IO.File.WriteAllText(@"C:\data\WriteTxt.json", trades_deserial);
            // slicing over array ...
            foreach (TRADEINFORMATIONv2 item in trades)
            {
                list.Add(item.Price);
                listJSON.Add(JsonConvert.SerializeObject(item));
            } 
            System.IO.File.WriteAllLines(@"C:\data\WriteLin.json", listJSON);

            //Console.WriteLine(text);

            // Run Database
            DBMONGO.Current.mainfunct( trades );
            */
            //.Current.mainfunct( trades ); // .fct("bladibla"); //TESTS.Hellos
        }
    }
    
    public class Event
    {
        public string Name { get; set; }
        public DateTime StartDate { get; set; }
    }

}
    /*
    public void oldMain() //string[] args/)
        {
            var depth3 = BTCEAPIv3WRAPPER.GetDepth(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var ticker3 = BTCEAPIv3WRAPPER.GetTicker(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR });
            var trades3 = BTCEAPIv3WRAPPER.GetTrades(new BTCECURRENCYPAIR[] { BTCECURRENCYPAIR.BTC_EUR }, 2000); // 2000 is the limit
            var ticker = BTCEAPIv2WRAPPER.GetTicker(BTCECURRENCYPAIR.BTC_EUR);
            var trades = BTCEAPIv2WRAPPER.GetTrades(BTCECURRENCYPAIR.BTC_EUR);
            var btcusdDepth = BTCEAPIv2WRAPPER.GetDepth(BTCECURRENCYPAIR.BTC_EUR);
            var fee = BTCEAPIv2WRAPPER.GetFee(BTCECURRENCYPAIR.BTC_EUR);
            string APIKEY = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEY;
            string APIKEYSECRET = BTCEAPIWRAPPER_TEST.Properties.Settings.Default.APIKEYSECRET;
            var TheBTCEAPIv2WRAPPERObj = new BTCEAPIv2WRAPPER(APIKEY, APIKEYSECRET);
            var info = TheBTCEAPIv2WRAPPERObj.GetInfo();

            decimal jjj;
            if (!BsonClassMap.IsClassMapRegistered(typeof(TRADEINFORMATIONv2)))
            {
                // register class map for MyClass
                jjj = 1;
            }
            string trades_deserial = JsonConvert.SerializeObject(trades);
            //    DeserializeObject(trades);
            var szdeserialised = JsonConvert.DeserializeObject(trades_deserial);
            //JsonConvert.SerializeObject(sampleGroupInstance);
            List<decimal> list = new List<decimal>();
            List<string> listJSON = new List<string>();
            foreach (TRADEINFORMATIONv2 item in trades)
            {
                list.Add(item.Price);
                listJSON.Add(JsonConvert.SerializeObject(item));
            } 

            foreach (int prime in list) // Loop through List with foreach
            {
                Console.WriteLine(prime);
            }

            for (int i = 0; i < list.Count; i++) // Loop through List with for
            {
                Console.WriteLine(list[i]);
            }

            // Tests with IO //////////////////////////////////////////////////////////////////////////////////////
            // Write in file, one (long) line:
            System.IO.File.WriteAllText(@"C:\data\WriteTxt.json", trades_deserial);
            // slicing over array ...
            System.IO.File.WriteAllLines(@"C:\data\WriteLin.json", listJSON);
            ///////////////////////////////////////////////////////////////////////////////////////////////////////

            // Test BSON //////////////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////////////////////////////
        Event e = new Event
        {   
            Name = "Movie Premiere",
            StartDate = new DateTime(2013, 1, 22, 20, 30, 0)
        };

        var a = new Event()
        {
            Name = "Movie Premiere",
            StartDate = new DateTime(2013, 1, 22, 20, 30, 0)
        };

        var jaja = a.ToBson();
        var text = Encoding.ASCII.GetString(jaja);
        Console.WriteLine(text);

        // Run Database
        DBMONGO.Current.mainfunct( trades );
        } 
}*/
