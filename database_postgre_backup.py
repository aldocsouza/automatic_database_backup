import subprocess
from datetime import datetime
import os

# Configurações do banco
server = "localhost"
database = "mydb"
username = "root"
password = "my_password"  # Remova a senha daqui!

# Caminho completo do pg_dump (ajuste conforme necessário)
pg_dump_path = r'"C:\Program Files\PostgreSQL\16\bin\pg_dump.exe"'

# Nome do arquivo de backup com data e hora
backup_file = f"D:/backup/backup_{database}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

# Comando para backup (sem a senha)
backup_command = f'{pg_dump_path} -h {server} -U {username} -F c -b -v -f "{backup_file}" {database}'

# Criar o arquivo .pgpass (se não existir)
pgpass_file = os.path.join(os.path.expanduser("~"), ".pgpass")  # Padrão para Windows
with open(pgpass_file, "w") as f:
    f.write(f"{server}:{5432}:{database}:{username}:{password}\n") # Porta 5432 é a padrão do Postgres
os.chmod(pgpass_file, 0o600) # Permissões restritas (importante!)

# Variável de ambiente para o pgpass (necessário no Windows)
os.environ["PGPASSFILE"] = pgpass_file

# Executar no CMD
try:
    result = subprocess.run(backup_command, shell=True, capture_output=True, text=True, check=True)
    print("Backup concluído com sucesso!")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Erro durante o backup: {e}")
    print(e.stderr)
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Limpeza: opcional, mas recomendado remover o arquivo .pgpass após o uso, se quiser.
os.remove(pgpass_file)

# Deligar Computador: O comando abaixo é específico para desligar o computador após o backup, remova se não for necessário.
try:
    # ... (seu código de backup) ...
    subprocess.run(["shutdown", "/s", "/t", "1"], shell=True, check=True)  # Desliga o computador após o backup
except subprocess.CalledProcessError as e:
    print(f"Erro ao desligar o computador: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")