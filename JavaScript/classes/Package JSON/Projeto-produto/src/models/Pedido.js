export default class Pedido {
    constructor(cliente="desconhecido", listaProdutos=[]) {
        this.cliente = cliente;
        this.listaProdutos = listaProdutos;
    }

    calcularValorTotal() {
        let total = 0;
        this.listaProdutos.forEach((produto) => {
            total += (produto.preco * produto.quantidade);
        });
        return total;
    }
}