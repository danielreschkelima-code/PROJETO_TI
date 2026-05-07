//Importando o express
const express = require("express");

//Criando a aplicação
const app = express();

//Definindo a porta
const PORT = 3000;

//Definindo a rota principal
app.get("/inicio",(req, res)=>{
    res.send("Bem-vindo ao meu primeiro servidor Express!");
});

//Iniciando o servidor
app.listen(PORT, ()=>{
    console.log(`Servidor rodando em http://localhost:${PORT}`);
})