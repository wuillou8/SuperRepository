using System;

namespace BTCEAPIWRAPPER.UTILS
{
    public static class UNIXTIME
    {
        static DateTime unixEpoch;
        static UNIXTIME()
        {
            unixEpoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
        }
        public static UInt32 Now
        {
            get
            {
                return GetFromDateTime(DateTime.UtcNow);
            }
        }
        public static UInt32 GetFromDateTime(DateTime d)
        {
            return (UInt32)(d - unixEpoch).TotalSeconds;
        }
        public static DateTime ConvertToDateTime(UInt32 unixtime)
        {
            return unixEpoch.AddSeconds(unixtime);
        }
    }
}
