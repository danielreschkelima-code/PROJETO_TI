import Produto from "./models/Produto.js";
import Pedido from "./models/Pedido.js";

const computador = new Produto("Computador", 1400, 1);
const tablet = new Produto("Tablet", 1000, 3);
const celular = new Produto("Celular", 400, 1);

const pedido1 = new Pedido("Carolina", [computador, tablet, celular]);

console.log(`\n================== PEDIDOS ==================\n\nCliente: ${pedido1.cliente}\n---------------------------------------------\nProdutos:`);  

pedido1.listaProdutos.forEach((produto) => {
            console.log(`   - ${produto.nome}: R$ ${produto.preco.toFixed(2)} x ${produto.quantidade} un`);
        });

console.log(`---------------------------------------------\nVALOR TOTAL: R$ ${pedido1.calcularValorTotal().toFixed(2)}\n=============================================\n`);