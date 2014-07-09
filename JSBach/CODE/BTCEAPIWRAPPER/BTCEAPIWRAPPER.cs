using BTCEAPIWRAPPER.UTILS;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Web;

namespace BTCEAPIWRAPPER
{
    class WEBAPI
    {
        public static string Query(string url)
        {
            var request = WebRequest.Create(url);
            request.Proxy = WebRequest.DefaultWebProxy;
            request.Proxy.Credentials = System.Net.CredentialCache.DefaultCredentials;
            if (request == null)
            {
                throw new Exception("THIS IS NOT A VALID HTTP WEB REQUEST");
            }
            return new StreamReader(request.GetResponse().GetResponseStream()).ReadToEnd();
        }
    }
    public class BTCEAPIv2WRAPPER
    {
        string key;
        HMACSHA512 hashMaker;
        UInt32 nonce;
        public BTCEAPIv2WRAPPER(string key, string secret)
        {
            this.key = key;
            hashMaker = new HMACSHA512(Encoding.ASCII.GetBytes(secret));
            nonce = UNIXTIME.Now; // INITIAL
        }
        public USERINFORMATION GetInfo()
        {
            var resultStr = Query(new Dictionary<string, string>()
            {
                {
                    "method",
                    "getInfo"
                }
            }
                                 );
            var result = JObject.Parse(resultStr);
            if (result.Value<int>("success") == 0)
            {
                throw new Exception(result.Value<string>("error"));
            }
            return USERINFORMATION.ReadFromJObject(result["return"] as JObject);
        }
        public TRANSACTIONHISTORY GetTransactionHistory(int? from = null,
                                                        int? count = null,
                                                        int? fromId = null,
                                                        int? endId = null,
                                                        bool? orderAsc = null,
                                                        DateTime? since = null,
                                                        DateTime? end = null)
        {
            var args = new Dictionary<string, string>()
            {
                {
                    "method",
                    "TransHistory"
                }
            };
            if (from != null)
                args.Add("from", from.Value.ToString());
            if (count != null)
                args.Add("count", count.Value.ToString());
            if (fromId != null)
                args.Add("from_id", fromId.Value.ToString());
            if (endId != null)
                args.Add("end_id", endId.Value.ToString());
            if (orderAsc != null)
                args.Add("order", orderAsc.Value ? "ASC" : "DESC");
            if (since != null)
                args.Add("since", UNIXTIME.GetFromDateTime(since.Value).ToString());
            if (end != null)
                args.Add("end", UNIXTIME.GetFromDateTime(end.Value).ToString());
            var result = JObject.Parse(Query(args));
            if (result.Value<int>("success") == 0)
                throw new Exception(result.Value<string>("error"));
            return TRANSACTIONHISTORY.ReadFromJObject(result["return"] as JObject);
        }
        public TRADEHISTORY GetTradeHistory(int? from = null,
                                            int? count = null,
                                            int? fromId = null,
                                            int? endId = null,
                                            bool? orderAsc = null,
                                            DateTime? since = null,
                                            DateTime? end = null)
        {
            var args = new Dictionary<string, string>()
            {
                { "method", "TradeHistory" }
            };
            if (from != null)
                args.Add("from", from.Value.ToString());
            if (count != null)
                args.Add("count", count.Value.ToString());
            if (fromId != null)
                args.Add("from_id", fromId.Value.ToString());
            if (endId != null)
                args.Add("end_id", endId.Value.ToString());
            if (orderAsc != null)
                args.Add("order", orderAsc.Value ? "ASC" : "DESC");
            if (since != null)
                args.Add("since", UNIXTIME.GetFromDateTime(since.Value).ToString());
            if (end != null)
                args.Add("end", UNIXTIME.GetFromDateTime(end.Value).ToString());
            var result = JObject.Parse(Query(args));
            if (result.Value<int>("success") == 0)
                throw new Exception(result.Value<string>("error"));
            return TRADEHISTORY.ReadFromJObject(result["return"] as JObject);
        }
        public ORDERLIST GetOrderList(int? from = null,
                                      int? count = null,
                                      int? fromId = null,
                                      int? endId = null,
                                      bool? orderAsc = null,
                                      DateTime? since = null,
                                      DateTime? end = null,
                                      BTCECURRENCYPAIR? pair = null,
                                      bool? active = null)
        {
            var args = new Dictionary<string, string>()
            {
                { "method", "OrderList" }
            };
            if (from != null)
                args.Add("from", from.Value.ToString());
            if (count != null)
                args.Add("count", count.Value.ToString());
            if (fromId != null)
                args.Add("from_id", fromId.Value.ToString());
            if (endId != null)
                args.Add("end_id", endId.Value.ToString());
            if (orderAsc != null)
                args.Add("order", orderAsc.Value ? "ASC" : "DESC");
            if (since != null)
                args.Add("since", UNIXTIME.GetFromDateTime(since.Value).ToString());
            if (end != null)
                args.Add("end", UNIXTIME.GetFromDateTime(end.Value).ToString());
            if (pair != null)
                args.Add("pair", BTCECURRENCYPAIRHELPER.ToString(pair.Value));
            if (active != null)
                args.Add("active", active.Value ? "1" : "0");
            var result = JObject.Parse(Query(args));
            if (result.Value<int>("success") == 0)
                throw new Exception(result.Value<string>("error"));
            return ORDERLIST.ReadFromJObject(result["return"] as JObject);
        }
        public TRADEANSWER Trade(BTCECURRENCYPAIR pair, TRADETYPE type, decimal rate, decimal amount)
        {
            var args = new Dictionary<string, string>()
            {
                { "method", "Trade" },
                { "pair", BTCECURRENCYPAIRHELPER.ToString(pair) },
                { "type", TRADETYPEHELPER.ToString(type) },
                { "rate", DecimalToString(rate) },
                { "amount", DecimalToString(amount) }
            };
            var result = JObject.Parse(Query(args));
            if (result.Value<int>("success") == 0)
                throw new Exception(result.Value<string>("error"));
            return TRADEANSWER.ReadFromJObject(result["return"] as JObject);
        }
        public CANCELORDERANSWER CancelOrder(int orderId)
        {
            var args = new Dictionary<string, string>()
            {
                { "method", "CancelOrder" },
                { "order_id", orderId.ToString() }
            };
            var result = JObject.Parse(Query(args));
            if (result.Value<int>("success") == 0)
                throw new Exception(result.Value<string>("error"));
            return CANCELORDERANSWER.ReadFromJObject(result["return"] as JObject);
        }
        string Query(Dictionary<string, string> args)
        {
            args.Add("nonce", GetNonce().ToString());
            var dataStr = BuildPostData(args);
            var data = Encoding.ASCII.GetBytes(dataStr);
            var request = WebRequest.Create(new Uri("https://btc-e.com/tapi")) as HttpWebRequest;
            if (request == null)
                throw new Exception("Non HTTP WebRequest");
            request.Method = "POST";
            request.Timeout = 15000; // timeout request of 15s !!!
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = data.Length;
            request.Headers.Add("Key", key);
            request.Headers.Add("Sign", ByteArrayToString(hashMaker.ComputeHash(data)).ToLower());
            var reqStream = request.GetRequestStream();
            reqStream.Write(data, 0, data.Length);
            reqStream.Close();
            return new StreamReader(request.GetResponse().GetResponseStream()).ReadToEnd();
        }
        static string ByteArrayToString(byte[] ba)
        {
            return BitConverter.ToString(ba).Replace("-", "");
        }




        static string BuildPostData(Dictionary<string, string> d)
        {
            StringBuilder s = new StringBuilder();
            foreach (var item in d)
            {
                s.AppendFormat("{0}={1}", item.Key, HttpUtility.UrlEncode(item.Value));
                s.Append("&");
            }
            if (s.Length > 0) s.Remove(s.Length - 1, 1);
            return s.ToString();
        }
        UInt32 GetNonce()
        {
            return ++nonce; // should be bounded by the maximum value that an UInt32 can take...
        }
        static string DecimalToString(decimal d)
        {
            return d.ToString(CultureInfo.InvariantCulture);
        }
        public static DEPTH GetDepth(BTCECURRENCYPAIR pair)
        {
            string queryStr = string.Format("https://btc-e.com/api/2/{0}/depth", BTCECURRENCYPAIRHELPER.ToString(pair));
            return DEPTH.ReadFromJObject(JObject.Parse(WEBAPI.Query(queryStr)));
        }
        public static TICKER GetTicker(BTCECURRENCYPAIR pair)
        {
            string queryStr = string.Format("https://btc-e.com/api/2/{0}/ticker", BTCECURRENCYPAIRHELPER.ToString(pair));
            return TICKER.ReadFromJObject(JObject.Parse(WEBAPI.Query(queryStr))["ticker"] as JObject);
        }
        public static List<TRADEINFORMATIONv2> GetTrades(BTCECURRENCYPAIR pair)
        {
            string queryStr = string.Format("https://btc-e.com/api/2/{0}/trades", BTCECURRENCYPAIRHELPER.ToString(pair));
            return JArray.Parse(WEBAPI.Query(queryStr)).OfType<JObject>().Select(TRADEINFORMATIONv2.ReadFromJObject).ToList();
        }
        public static decimal GetFee(BTCECURRENCYPAIR pair)
        {
            string queryStr = string.Format("https://btc-e.com/api/2/{0}/fee", BTCECURRENCYPAIRHELPER.ToString(pair));
            return JObject.Parse(WEBAPI.Query(queryStr)).Value<decimal>("trade");
        }
    }
    public class BTCEAPIv3WRAPPER
    {
        private static string MakePairListString(BTCECURRENCYPAIR[] pairlist)
        {
            return string.Join("-", pairlist.Select(x => BTCECURRENCYPAIRHELPER.ToString(x)).ToArray());
        }

        private static string Query(string method, BTCECURRENCYPAIR[] pairlist, Dictionary<string, string> args = null)
        {
            var pairliststr = MakePairListString(pairlist);
            StringBuilder sb = new StringBuilder();
            sb.Append("https://btc-e.com/api/3/");
            sb.Append(method);
            sb.Append("/");
            sb.Append(pairliststr);
            if (args != null && args.Count > 0)
            {
                sb.Append("?");
                var arr = args.Select(x => string.Format("{0}={1}", HttpUtility.UrlEncode(x.Key), HttpUtility.UrlEncode(x.Value))).ToArray();
                sb.Append(string.Join("&", arr));
            }
            var queryStr = sb.ToString();
            return WEBAPI.Query(queryStr);
        }
        private static string QueryIgnoreInvalid(string method, BTCECURRENCYPAIR[] pairlist, Dictionary<string, string> args = null)
        {
            var newargs = new Dictionary<string, string>() { { "ignore_invalid", "1" } };
            if (args != null)
                newargs.Concat(args);
            return Query(method, pairlist, newargs);
        }
        private static Dictionary<BTCECURRENCYPAIR, T> ReadPairDict<T>(JObject o, Func<JContainer, T> valueReader)
        {
            return o.OfType<JProperty>().Select(x => new KeyValuePair<BTCECURRENCYPAIR, T>(BTCECURRENCYPAIRHELPER.FromString(x.Name), valueReader(x.Value as JContainer))).ToDictionary(x => x.Key, x => x.Value);
        }
        private static Dictionary<BTCECURRENCYPAIR, T> MakeRequest<T>(string method, BTCECURRENCYPAIR[] pairlist, Func<JContainer, T> valueReader, Dictionary<string, string> args = null, bool ignoreInvalid = true)
        {
            string queryresult;
            if (ignoreInvalid)
                queryresult = QueryIgnoreInvalid(method, pairlist, args);
            else
                queryresult = Query(method, pairlist, args);
            var resobj = JObject.Parse(queryresult);
            if (resobj["success"] != null && resobj.Value<int>("success") == 0)
                throw new Exception(resobj.Value<string>("error"));
   
            var r = ReadPairDict<T>(resobj, valueReader);
            return r;
        }
        public static Dictionary<BTCECURRENCYPAIR, DEPTH> GetDepth(BTCECURRENCYPAIR[] pairlist, int limit = 150)
        {
            //return MakeRequest<DEPTH>("depth", pairlist, new Func<JContainer, DEPTH>(x => DEPTH.ReadFromJObject(x as JObject)), new Dictionary<string, string>() { { "limit", limit.ToString() } }, true);
            return MakeRequest<DEPTH>("depth", pairlist, new Func<JContainer, DEPTH>(x => DEPTH.ReadFromJObject(x as JObject)), new Dictionary<string, string>() { { "limit", limit.ToString() } }, false);
        }
        public static Dictionary<BTCECURRENCYPAIR, TICKER> GetTicker(BTCECURRENCYPAIR[] pairlist)
        {
            return MakeRequest<TICKER>("ticker", pairlist, x => TICKER.ReadFromJObject(x as JObject), null, true);
        }
        public static Dictionary<BTCECURRENCYPAIR, List<TRADEINFORMATIONv3>> GetTrades(BTCECURRENCYPAIR[] pairlist, int limit /*= 150*/)
        {
            Func<JContainer, List<TRADEINFORMATIONv3>> tradeInfoListReader = (x => x.OfType<JObject>().Select(TRADEINFORMATIONv3.ReadFromJObject).ToList());
            //return MakeRequest<List<TRADEINFORMATIONv3>>("trades", pairlist, tradeInfoListReader, new Dictionary<string, string>() { { "limit", limit.ToString() } }, true);
            return MakeRequest<List<TRADEINFORMATIONv3>>("trades", pairlist, tradeInfoListReader, new Dictionary<string, string>() { { "limit", limit.ToString() } }, false);
        }
    }
}
