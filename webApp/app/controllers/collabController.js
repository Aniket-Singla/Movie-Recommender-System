const path = require('path');
var amqp = require('amqplib/callback_api')

exports.getCollab = (req,res)=>{
  var input = [
    req.query.type,
    req.query.userId,
    req.query.movieId,
    ]
    console.log(input)
  amqp.connect('amqp://localhost',onceConnected );
  function onceConnected(err, conn) {
    conn.createChannel(function (err, ch) {
      var simulations = 'query';
      ch.assertQueue(simulations, { durable: false });
      var results = 'resultsCollab';
      ch.assertQueue(results, { durable: false });
      if(req.query.userId){
        // ch.sendToQueue(simulations, new Buffer(JSON.stringify(input)));
        var getquery = input;
        // console.log(JSON.stringify(input))
      }
      else{
        console.log(JSON.stringify(["collab", "1"]))
        var getquery = ["collab", "1","302"]
      }
      ch.sendToQueue(simulations, new Buffer(JSON.stringify(getquery)));
      ch.consume(results, function (msg) {
      // res.send(msg.content.toString())
      var final_json = JSON.parse(msg.content.toString())
      
      console.log(final_json)
    
      return res.render('collab',{ port:process.env.PORT,title: 'Collaborative', 
                        css: ['main.css'],user:getquery[1],movieId:getquery[2],userRows:final_json });
      }, { noAck: true });
    });
    setTimeout(function () { conn.close(); }, 500);  
    }
  
}