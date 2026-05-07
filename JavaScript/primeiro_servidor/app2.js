const express = require("express");
const app = express();
const PORT = 3000;

//Array de linguagens
const linguagens = [
    "Python",
    "JavaScript",
    "Java",
    "C",
    "Rust",
    "Ruby"
];

//Rota para listar as linguagens
app.get("/linguagens",(req, res)=>{
    res.json(linguagens);
});

//Rota para retornar uma linguagem específica por índice
app.get("/linguagens/:id",(req,res)=>{
    const id = parseInt(req.params.id);

    if(id >= 0 && id < linguagens.length){
        res.json({linguagem: linguagens[id]});
    } else{
        res.status(404).json({erro: "Linguagem não encontrada"})
    }
});

app.listen(PORT, ()=>{
    console.log("Servidor rodando em http://localhost:3000")
});