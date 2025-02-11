# automatic_database_backup

## GERANDO EXECUTÁVEL
1. Instale o PyInstaller:
´´´
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