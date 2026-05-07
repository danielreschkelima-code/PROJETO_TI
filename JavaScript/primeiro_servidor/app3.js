const express = require('express');
const app = express();
const PORT = 3000;

// Middleware para interpretar JSON
app.use(express.json());

// Banco de dados simulado (array de objetos)
let filmes = [
  { id: 1, titulo: "Matrix", ano: 1999, genero: "FicÃ§Ã£o" },
  { id: 2, titulo: "Titanic", ano: 1997, genero: "Romance" }
];

// GET - Listar todos os filmes
app.get('/filmes', (req, res) => {
  res.json(filmes);
});

// GET - Buscar filme por ID
app.get('/filmes/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const filme = filmes.find(f => f.id === id);
  
  if (filme) {
    res.json(filme);
  } else {
    res.status(404).json({ erro: "Filme não encontrado" });
  }
});

// POST - Adicionar novo filme
app.post('/filmes', (req, res) => {
  const novoFilme = {
    id: filmes.length + 1,
    titulo: req.body.titulo,
    ano: req.body.ano,
    genero: req.body.genero
};
  
  filmes.push(novoFilme);
  res.status(201).json(novoFilme);
});

// PUT - Atualizar filme existente
app.put('/filmes/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = filmes.findIndex(f => f.id === id);
  
  if (index !== -1) {
    filmes[index] = {
      id: id,
      titulo: req.body.titulo,
      ano: req.body.ano,
      genero: req.body.genero
    };
    res.json(filmes[index]);
  } else {
    res.status(404).json({ erro: "Filme não encontrado" });
  }
});

// DELETE - Remover filme
app.delete('/filmes/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = filmes.findIndex(f => f.id === id);
  
  if (index !== -1) {
    filmes.splice(index, 1);
    res.status(204).send();
  } else {
    res.status(404).json({ erro: "Filme não encontrado" });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor de filmes rodando em http://localhost:${PORT}`);
});