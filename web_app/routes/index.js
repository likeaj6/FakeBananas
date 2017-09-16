var express = require('express');
var router = express.Router();
/* GET home page. */

router.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

//Router does this when it receives a post
router.post('/claims', function(req, res) {

    // var python = require('child_process').spawn(
    //  'python',
    //  // second argument is array of parameters, e.g.:
    //  ["/my/python/script.py"
    //  , req.body.claim]
    //  );
    //  var output = "";
    //  python.stdout.on('data', function(data){ output += data });
    //  python.on('close', function(code){
    //    if (code !== 0) {
    //        //an error occured during the python script
    //        return res.status(status).send(body)
    //    }
        if (req.body.type == 'url') {
            
            return res.json([

                { name: "URL!!!", agree: "99%", disagree: "1%" },
                { name: "source", agree: "55%", disagree: "45%" },

            ]);
        } else if (req.body.type == 'claim') {
            return res.json([
                //output
                { name: "CLAIM!!!", agree: "99%", disagree: "1%" },
                { name: "Response #2", agree: "55%", disagree: "45%" },

            ]);
        } else {

        }


    //    return res.send(200, output);
    //  });

});


router.get('/', function(req, res, next) {
    console.log("getting page");
//res.send('respond with a resource');
});

module.exports = router;
