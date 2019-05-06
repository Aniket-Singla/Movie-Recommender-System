
const express = require('express');
const bodyParser = require('body-parser');

const path = require("path");

require('dotenv').config();
const env = process.env.NODE_ENV || 'development';

const exphbs = require('express-handlebars');
const logger = require('morgan');
const indexRouter = require(path.join(__dirname,'app','routes','index'));
const contentRouter = require(path.join(__dirname,'app','routes','content'));
const collabRouter = require(path.join(__dirname,'app','routes','collab'));


console.log('process.env.NODE_ENV (in index.js) = ' + process.env.NODE_ENV);


// Set up Express Application
var app = express();
var port = process.env.PORT || 8080;
// development error handler
// will print stacktrace
if (env === 'development') {
    app.use(function (err, req, res, next) {
        res.status(err.status || 500);
        console.log('indev')
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function (err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});
app.use(express.static(process.cwd() + '/public'));
// Morgarn logger
app.use(logger('dev'));

// Sets up the Express app to handle data parsing
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.text());
app.use(bodyParser.json({ type: "application/vnd.api+json" }));
app.use(express.static(path.join(__dirname,'app/views')));


// Connect Flash
// app.use(flash());

// Set Handlebars as the view engine
app.set('views',path.join(__dirname,'/app/views'))
app.engine('handlebars', exphbs({ 
	defaultLayout: path.join(__dirname ,'app','/views/layouts/base.handlebars'),
	partialsDir: path.join(__dirname,'app','/views/partials'),
  	layoutsDir: path.join(__dirname ,'app','/views/layouts') }));
app.set('view engine', 'handlebars');

//routing 
app.use('/',indexRouter);
app.use('/content',contentRouter);
app.use('/collab',collabRouter);
app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).redirect('/500')
})
app.get('*',(req,res)=>{res.redirect('/404')});

 module.exports = app;