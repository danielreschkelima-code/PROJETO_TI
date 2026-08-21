<?php
$senha = "123456";

$novasenha = base64_encode($senha);
echo "base64: ".$novasenha."<br>";
echo "Sua senha é: ".base64_decode($novasenha);

echo "<hr>";

echo "Md5: ".md5($senha)."<br>"; // Não pode ser descriptografada.
echo "Sha1: ". sha1($senha)."<br>"; // Também não pode.

// PASSWORD HASH

$senha = "123456";
$options = [
        'cost' => 10, // quanto maior, mais seguro, mas também mais processamnto
];

$senhaSegura = password_hash($senha, PASSWORD_DEFAULT, $options);
echo $senhaSegura;

$senha_db = $senhaSegura;

if(password_verify($senha, $senha_db)):
    echo "Senha válida";
else:
    echo "Senha inválida";
endif;