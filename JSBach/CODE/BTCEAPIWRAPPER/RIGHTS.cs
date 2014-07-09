using Newtonsoft.Json.Linq;

namespace BTCEAPIWRAPPER
{
    public class RIGHTS
    {
        public bool Info { get; private set; }
        public bool Trade { get; private set; }
        public static RIGHTS ReadFromJObject(JObject o)
        {
            if (o == null)
                return null;
            return new RIGHTS()
            {
                Info = o.Value<int>("info") == 1,
                Trade = o.Value<int>("trade") == 1
            };
        }
    }
}
