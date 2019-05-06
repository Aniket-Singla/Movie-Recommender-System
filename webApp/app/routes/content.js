var express = require('express');
var router = express.Router();
const path = require('path');
// const passportConfig = require(path.join(__dirname,'../config/passport'));
var contentController = require(path.join(__dirname,'../controllers/content'));

// router.get('/',passportConfig.isAuthenticated,InvestorsController.getInvestors);
router.get('/',contentController.getContent);

module.exports = router;