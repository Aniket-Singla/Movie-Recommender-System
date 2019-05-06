var express = require('express');
const path = require('path');
var collabController = require(path.join(__dirname,'../controllers/collabController'));
var router = express.Router();
router.get('/',collabController.getCollab);

module.exports = router;