import subprocess
import os
from datetime import datetime

# Definição de parâmetros de conexão
server = 'localhost'
database = 'mydb'
username = 'root'
password = 'my_password'  # Remova a senha daqui!

# Diretório de backup
backup_dir = 'D:/backup'

# Nome do arquivo de backup (usando timestamp para evitar sobrescrita)
backup_file = os.path.join(backup_dir, f"backup_{database}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")

# Comando para executar o mysqldump (sem a senha)
backup_command = f"mysqldump -h {server} -u {username} -p{password} {database} > {backup_file}"

try:
    result = subprocess.run(backup_command, shell=True, capture_output=True, text=True, check=True)
    print("Backup concluído com sucesso!")
    #print(result.stdout)  # Descomente para ver a saída do mysqldump, se necessário
except subprocess.CalledProcessError as e:
    print(f"Erro durante o backup: {e}")
    print(e.stderr)
except Exception as e:
    print(f"Ocorreu um erro: {e}")





