using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using MongoDB.Bson;
using MongoDB.Driver;


namespace BTCEAPIWRAPPER
{
    public class Entity
    {
        public ObjectId Id { get; set; }

        public string Name { get; set; }
    }
    /*class mongoDB_COMM
    {
        public BTCEAPIv3WRAPPER Id { get; set; }

        public string Name { get; set; }
    }*/
    /*
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            var database = server.GetDatabase("test");
     */
}
