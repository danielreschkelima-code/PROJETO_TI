<?php
$senha = "123456";

$novasenha = base64_encode($senha);
echo "base64: ".$novasenha."<br>";
echo "Sua senha é: ".base64_decode($novasenha);

echo "<hr>";

echo "Md5: ".md5($senha)."<br>"; // Não pode ser descriptografada.
echo "Sha1: ". sha1($senha)."<br>"; // Também não pode.