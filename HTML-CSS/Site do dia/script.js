function carregar() {
    let msg = window.document.getElementById("msg");
    let img = window.document.getElementById("img");
    let data = new Date();
    let hora = data.getHours();
    if (hora >= 0 && hora < 12){
        msg.innerHTML = `<p>Agora são ${hora} horas.</p><p><strong>É MANHÃ!</strong></p>`;
        img.src = "fotoManha.webp";
        document.body.style.background = "#4ab7ff";
    } else if (hora < 18){
        msg.innerHTML = `<p>Agora são ${hora} horas.</p><p><strong>É TARDE!</strong></p>`;
        img.src = "fotoTarde.png";
        document.body.style.background = "#ffaf26";
    } else {
        msg.innerHTML = `<p>Agora são ${hora} horas.</p><p><strong>É NOITE!</strong></p>`;
        img.src = "fotoNoite.png";
        document.body.style.background = "#4d4aff";
    }
}