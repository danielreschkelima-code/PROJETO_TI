<?php
session_start(); // inicia a sessão.

$_SESSION['cor'] = "Verde";
$_SESSION['carro'] = "Onix";

echo $_SESSION['cor']."<br>".$_SESSION['carro']."<br>".session_id();