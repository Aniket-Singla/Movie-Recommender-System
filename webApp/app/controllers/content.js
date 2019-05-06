const path = require('path');
var amqp = require('amqplib/callback_api')

exports.getContent = (req,res)=>{
  var input = [
    req.query.type,
    req.query.title,
    ]
    console.log(input)
  amqp.connect('amqp://localhost',onceConnected );
  function onceConnected(err, conn) {
    conn.createChannel(function (err, ch) {
      var simulations = 'query';
      ch.assertQueue(simulations, { durable: false });
      var results = 'resultsContent';
      ch.assertQueue(results, { durable: false });
      if(req.query.title){
        ch.sendToQueue(simulations, new Buffer(JSON.stringify(input)));
        console.log(JSON.stringify(input))
      }
      else{
        console.log(JSON.stringify(["content", "The Shadow"]))
        ch.sendToQueue(simulations, new Buffer(JSON.stringify(["content", "The Shadow"])));
      }
  
      ch.consume(results, function (msg) {
      // res.send(msg.content.toString())
      var final_json = JSON.parse(msg.content.toString())
      // console.log(JSON.parse(final_json))
      console.log(final_json)
      return res.render('content',{ port:process.env.PORT,title: 'Content Based', css: ['main.css'],movies:final_json });
      }, { noAck: true });
    });
    setTimeout(function () { conn.close(); }, 500);  
    }
  
}