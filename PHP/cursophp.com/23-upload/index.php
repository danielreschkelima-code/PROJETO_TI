<html>
    <body>

        <?php
            if(isset($_POST['enviar'])):
                $formatoPermitidos = array("png", "jpeg", "jpg", "gif");

                $quantidadeArquivos = count($_FILES['arquivo']['name']);
                $contador = 0;

                while($contador < $quantidadeArquivos):


                    $extensao = pathinfo($_FILES['arquivo']['name'][$contador], PATHINFO_EXTENSION);

                    if (in_array($extensao, $formatoPermitidos)):
                        $pasta = "arquivos/";
                        $temporario = $_FILES['arquivo']['tmp_name'][$contador];
                        $novoNome = uniqid().".$extensao";

                        if(move_uploaded_file($temporario, $pasta.$novoNome)):
                            $mensagem[] = "Upload feito com sucesso para o $pasta.$novoNome!<br>";
                        else:
                            $mensagem[] = "Erro, não foi possível fazer o upload para o $temporiario!<br>";
                        endif;
                    else:
                        $mensagem[] = "$extensao inválida em ".$_FILES['arquivo']['name'][$contador]." !<br>";
                    endif;
                    $contador++;
                endwhile;
            endif;
        ?>

        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
            <input type="file" name="arquivo[]" multiple><br>
            <button type="submit" name="enviar"> Enviar </button>

        </form>
    </body>
</html>