# BACKUP AUTOMÁTICO DE BANCO DE DADOS

## Resumo:
Aqui está um código melhor estruturado, incluindo suporte para MySQL e PostgreSQL, além de comentários explicativos. Também organizei a parte de criação do executável para uso no Agendador de Tarefas do Windows.

📌 Recursos inclusos: <br>
✅ Suporte a MySQL e PostgreSQL<br>
✅ Geração automática de backups em diretórios organizados por data<br>
✅ Criação de executável para uso com o Agendador de Tarefas do Windows<br>

## Gerando Executável:
1. Instale o PyInstaller:
O PyInstaller é uma ferramenta que permite "empacotar" scripts Python em executáveis independentes. Você pode instalá-lo usando o pip:

    ```bash
        pip install pyinstaller
    ```
2. Crie o executável:
Abra o terminal (cmd ou PowerShell) na pasta onde você salvou o script Python (backup_mysql.py) e execute o seguinte comando:

    ```bash
        pyinstaller --onefile backup_mysql.py
        --onefile: Esta opção cria um único arquivo executável.
    ```

3. O executável será gerado na pasta:

    ```bash
        Copiar
        Editar
        dist/database_backup.exe
    ```

## 🖥 Agendando o Backup no Windows:

1. Abra o "Agendador de Tarefas" (Windows + R → taskschd.msc)
2. Crie uma nova tarefa
3. Na aba "Gatilhos", defina a frequência do backup (ex: diário, semanal)
4. Na aba "Ações", escolha "Iniciar um programa" e selecione database_backup.exe
5. Salve a tarefa e teste

Agora, seu backup será executado automaticamente! 🚀🔥
