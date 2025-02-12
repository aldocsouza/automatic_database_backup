import subprocess
import os
from datetime import datetime

# Definição de parâmetros de conexão
server = 'localhost'
database = 'mydb'
username = 'root'
password = 'my_password'

# Diretório de backup
backup_dir = 'C:/backup'

# Nome do arquivo de backup (usando timestamp para evitar sobrescrita)
backup_file = os.path.join(backup_dir, f"backup_{database}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")

# Comando para executar o mysqldump (sem a senha)
backup_command = f"mysqldump -h {server} -u {username} -p{password} {database} > {backup_file}"

os.environ['MYSQL_PWD'] = password # Variável de ambiente para MySQL

def executar_backup():
    try:
        result = subprocess.run(backup_command, shell=True, capture_output=True, text=True, check=True)
        print("Backup concluído com sucesso!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro durante o backup: {e}")
        print(e.stderr)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        del os.environ['MYSQL_PWD']

def executar_git():
    try:
        os.chdir("C:/backup")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"ref: backup_{database}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Comandos Git executados com sucesso!")
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"Erro ao executar comandos Git: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def desligar_computador():
    try:
        subprocess.run(["shutdown", "/s", "/t", "1"], shell=True, check=True)
        print("Computador será desligado em 1 segundo.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desligar o computador: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

executar_backup()
executar_git()
desligar_computador() # Remova se não for necessário
