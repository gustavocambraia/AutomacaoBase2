# AutomacaoBase2

Repositório de artefatos para os testes automatizados realizados no projeto da Base2.

Aqui serão inseridos os documentos descrevendo os BDDs utilizados como referência para os testes
e os respectivos arquivos Python.

No main branch há diretórios de um único projeto Python, com classes que se comunicam e que realizam os seguintes testes: 
            - Visualizar tarefas criadas (test_visualizar_tarefas);
            - Atualizar uma tarefa criada (test_atualizar_tarefa);
            - Apagar uma tarefa criada (test_apagar_tarefa);
            - Pesquisar tarefa com código válido (test_pesquisar_tarefa_valida);
            - Pesquisar tarefa com código inválido (test_pesquisa_invalida);
            - Mudar e-mail cadastrado (test_alterar_email);
            - Mudar o nome real (test_mudar_nome_real);
            - Alterar a senha (test_alterar_senha);
            - Alterar a senha sem preencher o campo "Senha Atual" (test_alterar_senha_invalido);
            - Gerar uma chave de acesso para minha API (test_criar_api);
            - Revogar o acesso de uma API (test_deletar_token).
            
Já no master branch, os diretório atuam como projetos individuais, cada um voltado para uma feature específica conforme o título do arquivo.
Em todos os projetos, seja do main ou do master branch, as constantes CHROMEDRIVER_PATH e GECKODRIVER_PATH devem ser alteradas de acordo com a máquina do usuário; elas se encontram no diretório Config, arquivo config.py.
Nos arquivos individuais do master branch, os projetos apresentam modelo Data Driven - nestes casos, além de realizar a alteração da constante PATH, é necessário, também, alterar a constante do caminho para o arquivo Data Driven.
