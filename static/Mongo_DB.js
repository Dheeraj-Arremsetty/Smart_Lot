var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost/connenction.Smart_Lot';

MongoClient.connect(url, function(err, db) {

  console.log("Connected");

    db.close()

});
