console.log();

class Produto {
    #preço;
    getter() {
        console.log(`${this.#preço}`);
    }
    setter(npreco) {
        if (npreco > 0){
            this.#preço = npreco;
        } else {
            console.log("\nERRO: valor inválido\n");
        }
    }
}

const produtor = new Produto()

produtor.getter();
produtor.setter(-29);
produtor.setter(20);
produtor.getter();

console.log();