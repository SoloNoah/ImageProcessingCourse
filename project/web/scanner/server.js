//cors - managing access to the sever.
//multer - managing files.
//express - server side rendering, hosts html and js files. 
var express = require('express');
const fileUpload = require('express-fileupload');
const app = express();

app.use(fileUpload());

//set the POST route to a file
app.post('/upload',(req,res)=>{
    if(req.files===null){
        return res.status(400).json({msg: 'No file uploaded'});
    }
    const file = req.files.file;

    file.mv(`${__dirname}/uploads/${file.name}`,err =>{
        if(err){
            console.error(err);
            return res.status(500).send();
        }
        res.json({fileName:file.name, filePath:`/uploads/${file.name}`});
    });
});

app.listen(8000,()=> {
    console.log("App running on port 8000");
});

