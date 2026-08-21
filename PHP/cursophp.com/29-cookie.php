<?php
// COOKIE
setcookie('user', 'Daniel', time()+3600);
setcookie('email', 'daniel@gmail', time()+3600);
setcookie('ultima_pesquisa', 'Brandon', time()+3600);

var_dump($_COOKIE);