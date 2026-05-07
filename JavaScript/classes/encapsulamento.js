class ContaBancaria{
#saldo; // Declarando variável PRIVADA. Ela não está no construtor, porque ela é independente dos parâmetros, ainda que parta deles.
    constructor(titular, saldoInicial){
        this.titular = titular;
        this.#saldo = saldoInicial;
    }

    get saldo() {
        return this.#saldo;
    }

    set saldo(valor) {
        this.#saldo = valor;
    }

    depositar(valor){
        if (valor > 0){
            this.#saldo += valor;
            console.log(`Depósito de R$ ${valor} realizado!`);
        } else {
            console.log("Valor inválido!");
        }
    }

    sacar(valor){
        if(valor > 0 && valor <= this.#saldo){
            this.#saldo -= valor;
            console.log(`Saque de R$ ${valor} realizado!`);
        } else {
            console.log("ERRO: valor inválido e/ou saldo insuficiente.")
        }
    }

    consultarSaldo(){
        console.log(`Saldo atual R$ ${this.#saldo}`);
    }
}

const ContaDoDaniel = new ContaBancaria("Daniel", 1000000000000000);

console.log();
ContaDoDaniel.consultarSaldo();
ContaDoDaniel.depositar(10);
ContaDoDaniel.sacar(1000000000000000);
ContaDoDaniel.consultarSaldo();
console.log();
ContaDoDaniel.saldo = 15; // Daria erro porque o saldo é privado. Só não dá por conta do set.
console.log(ContaBancaria.saldo); // Daria erro porque o saldo é privado. Só não dá por conta do get.