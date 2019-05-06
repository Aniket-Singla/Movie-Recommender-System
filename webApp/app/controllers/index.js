require('dotenv').config();
const path = require('path')
var amqp = require('amqplib/callback_api')

exports.getHome = function(req, res) {

var input = [
	req.query.number
  ]
  console.log(input)
amqp.connect('amqp://localhost',onceConnected );
function onceConnected(err, conn) {
	conn.createChannel(function (err, ch) {
	  var simulations = 'query';
	  ch.assertQueue(simulations, { durable: false });
	  var results = 'resultsDemographic';
	  ch.assertQueue(results, { durable: false});
		if(req.query.number){
			ch.sendToQueue(simulations, new Buffer(JSON.stringify(input)));
		}
	  else{
			console.log(JSON.stringify(['10']))
			ch.sendToQueue(simulations, new Buffer(JSON.stringify(['10'])));
		}

	  ch.consume(results, function (msg) {
		
		var final_json = JSON.parse(msg.content.toString())
		// console.log(JSON.parse(final_json))
		console.log(final_json)
		return res.render('home',{ port:process.env.PORT,title: 'Demographic', css: ['main.css'],movies:final_json });
	  }, { noAck: true });
	});
	setTimeout(function () { conn.close(); }, 500);  
  }
  
    
    
    
  
};

exports.getAbout = (req,res)=>{
	if(req.user){
		return res.render('about',{ layout:req.user.role,port:process.env.PORT,title: 'About', css: ['main.css'] })
	}
	return res.render('about',{ port:process.env.PORT,title: 'About', css: ['main.css'] })
}

exports.get404 = (req,res)=>{
	if(req.user)
	{
		return res.render('404',{ port:process.env.PORT,title: '404', layout: req.user.role,css: ['main.css','404.css'] })
	}
	return res.render('404',{ port:process.env.PORT,title: '404',css: ['404.css'],title:'404' })
}

exports.get500 = (req,res)=>{
	if(req.user)
	{
		return res.render('500',{ port:process.env.PORT,title: '500', layout: req.user.role,css: ['main.css','500.css'] })
	}
	return res.render('500',{ port:process.env.PORT,title: '500',title:'500',css: ['500.css'] })
}
