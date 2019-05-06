const amqp = require('amqplib');
const express = require("express");
const app = express();
const url = require("url");

// Use body-parser to handle the PUT data
const bodyParser = require("body-parser");
app.use(
  bodyParser.urlencoded({
    extended: false
  })
);
let port = process.env.PORT || 8080;
var open = amqp.connect('amqp://localhost');  
var qName = 'query'
open
  .then(conn => {
    return conn.createChannel();
  })
  .then(ch => {
    // Bind a queue to the exchange to listen for messages
    // When we publish a message, it will be sent to this queue, via the exchange
    // return ch
    //   .assertExchange(exchangeName, "direct", { durable: true })
    //   .then(() => {
    //     return ch.assertQueue(qName, { exclusive: false });
    //   })
    ch.assertQueue(qName)
    ch.assertQueue('resultsDemographic')
    //   .then(q => {
    //     return ch.bindQueue(q.queue, exchangeName, routingKey);
    //   });
  })
  .catch(err => {
    console.err(err);
    process.exit(1);
  });

  function addMessage(message) {
    return open
      .then(conn => {
        return conn.createChannel();
      })
      .then(ch => {
        // ch.publish(exchangeName, routingKey, new Buffer(message));
        // let msgTxt = message + " : Message sent at " + new Date();
        // console.log(" [+] %s", msgTxt);
        ch.sendToQueue(qName, new Buffer(JSON.stringify(input)));
        return new Promise(resolve => {
          resolve(message);
        });
      });
  }
  
  function getMessage() {
    return open
      .then(conn => {
        return conn.createChannel();
      })
      .then(ch => {
        // return ch.get(qName, {}).then(msgOrFalse => {
        return ch.consume('resultsDemographic').then(msgOrFalse=>{
          return new Promise(resolve => {
            let result = "No messages in queue";
            if (msgOrFalse !== false) {
              result =
                msgOrFalse.content.toString() +
                " : Message received at " +
                new Date();
              ch.ack(msgOrFalse);
            }
            console.log(" [-] %s", result);
            resolve(result);
          });
        });
      });
  }
  

  app.use(express.static(__dirname + "/public"));

  // The user has clicked submit to add a word and definition to the database
  // Send the data to the addWord function and send a response if successful
  app.put("/message", function(request, response) {
    addMessage(request.body.message)
      .then(resp => {
        response.send(resp);
      })
      .catch(err => {
        console.log("error:", err);
        response.status(500).send(err);
      });
  });
  
  // Read from the database when the page is loaded or after a word is successfully added
  // Use the getWords function to get a list of words and definitions from the database
  app.get("/message", function(request, response) {
    getMessage()
      .then(words => {
        response.send(words);
      })
      .catch(err => {
        console.log(err);
        response.status(500).send(err);
      });
  });
  
  // Listen for a connection.
  app.listen(port, function() {
    console.log("Server is listening on port " + port);
  });