<?php
date_default_timezone_set('America/Sao_Paulo');

echo date('d');
echo date('D');
echo date('l');
echo date('L');
echo date('m');
echo date('M');
echo date('y');
echo date('Y');

echo date('d/m/Y H:i:s');

// TIME 
$time = time();

// MKTIME
$data_que_eu_inventei = mktime(15, 30, 00, 02, 15, 2023);

// STRTOTIME
$data = '2019-04-10 13:00:00';
$data = strtotime($data);