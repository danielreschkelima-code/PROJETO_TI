<?php
// Superglobais
/*
 * $GLOBALS contém array com todas as var de qualquer escopo
 * $_SERVER contém array com informações do cabeçalho
 * $_POST contém um array com todos as var recebidas de um POST
 * $_GET contém um array com dados recebidos do GET
 * $_FILES
 * $_ENV
 * $_REQUEST
 * $_COOKIE
 * $_SESSION
*/

// $GLOBALS
$x = 10;
$y = 5;
function soma() {
    echo $GLOBALS['x'] + $GLOBALS['y'];
}
soma();

// $_SERVER
echo $_SERVER['PHP_SELF']."<br>";
echo $_SERVER['SERVER_NAME']."<br>";
echo $_SERVER['SCRIPT_FILENAME']."<br>";
echo $_SERVER['DOCUMENT_ROOT']."<br>";
echo $_SERVER['SERVER_PORT']."<br>";
echo $_SERVER['REMOTE_ADDR']."<br>";

// $_POST
// ver arquivos na pasta de formulários

// GET
// ver arquivos na pasta de formulários