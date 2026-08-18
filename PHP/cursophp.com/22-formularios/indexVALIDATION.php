<html>
    <body>
        <?php
            /* Validações
            Funções (filter_input - filter_var)
            FILTER_VALIDATE_INT
            FILTER_VALIDATE_EMAIL
            FILTER_VALIDATE_FLOAT
            FILTER_VALIDATE_IP
            FILTER_VALIDATE_URL
            */
        ?>

        <?php
            /* Sanitização
             * FILTER_SANITIZE_SPECIAL_CHARS
             * FILTER_SANITIZE_INT
             * FILTER_SANITIZE_EMAIL
             * FILTER_SANITIZE_URL
            */
        ?> 

        <?php
            if(isset($_POST['enviar'])):
                // Array de erros
                $erros = array();

                // Sanitizações
                $nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
                $idade = filter_input(INPUT_POST, 'idade', FILTER_SANITIZE_NUMBER_INT);
                $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
                $url = filter_input(INPUT_POST, 'url', FILTER_SANITIZE_URL);
                
                // Validações
                if (!$idade = filter_input(INPUT_POST, 'idade', FILTER_VALIDATE_INT)):
                    $erros[] = "Idade precisa ser um número inteiro.";
                endif;

                if (!$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)):
                    $erros[] = "E-mail precisa ser um e-mail válido.";
                endif;

                if (!$peso= filter_input(INPUT_POST, 'peso', FILTER_VALIDATE_FLOAT)):
                    $erros[] = "Peso precisa ser um número.";
                endif;

                if (!$ip = filter_input(INPUT_POST, 'ip', FILTER_VALIDATE_IP)):
                    $erros[] = "IP precisa ser um IP válido.";
                endif;

                if (!$url = filter_input(INPUT_POST, 'url', FILTER_VALIDATE_URL)):
                    $erros[] = "URL precisa ser uma URL válida.";
                endif;
                
                // Impressão dos resultados
                if (!empty($erros)):
                    foreach ($erros as $erro):
                        echo "<li> $erro </li>";
                    endforeach;
                else:
                    echo "Dados corretos!";
                endif;
            endif;
        ?>

        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
            Nome: <input type="text" name="nome"><br>
            Idade: <input type="text" name="idade"><br>
            E-mail: <input type="email" name="email"><br>
            Peso: <input type="email" name="peso"><br>
            IP: <input type="email" name="ip"><br>
            URL: <input type="text" name="url"><br>
            <button type="submit" name="enviar"> Enviar </button>
        </form>
    </body>
</html>