import os
import datetime

# 👉 EXTENSÕES QUE SERÃO LIDAS
EXTENSOES = (".php", ".css", ".js", ".py", ".html", ".txt", ".sql")

# 👉 PASTAS QUE SERÃO IGNORADAS (NÃO ENTRA NELAS)
IGNORAR_PASTAS = [
    ".git",
    ".gitignore",
    "__pycache__",
    ".env",
    "Scripts",
    "pyvenv.cfg",
    ".venv"
]

def ler_pastas(caminho, arquivo_saida, nivel=0):
    try:
        itens = os.listdir(caminho)
    except PermissionError:
        arquivo_saida.write(" " * nivel + "[Sem permissão]\n")
        return

    # 👉 SEPARA PASTAS E ARQUIVOS
    pastas = []
    arquivos = []

    for item in itens:
        caminho_completo = os.path.join(caminho, item)
        if os.path.isdir(caminho_completo):
            pastas.append(item)
        else:
            arquivos.append(item)

    # 👉 ORDENA
    pastas.sort()
    arquivos.sort()

    # 👉 PRIMEIRO: PASTAS
    for item in pastas:
        caminho_completo = os.path.join(caminho, item)

        # 👉 SE FOR PASTA IGNORADA
        if item in IGNORAR_PASTAS:
            linha = " " * nivel + f"📁 (pasta ignorada) {item}\n"
            print(linha, end="")
            arquivo_saida.write(linha)
            continue

        # 👉 PASTA NORMAL
        linha = " " * nivel + f"📁 {item}\n"
        print(linha, end="")
        arquivo_saida.write(linha)

        ler_pastas(caminho_completo, arquivo_saida, nivel + 4)

    # 👉 DEPOIS: ARQUIVOS
    for item in arquivos:
        caminho_completo = os.path.join(caminho, item)

        # 👉 SE FOR ARQUIVO VÁLIDO
        if item.endswith(EXTENSOES):
            linha = " " * nivel + f"📄 {item}\n"
            print(linha, end="")
            arquivo_saida.write(linha)

            try:
                with open(caminho_completo, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                cabecalho = " " * (nivel + 4) + "🧾 Conteúdo:\n"
                print(cabecalho, end="")
                arquivo_saida.write(cabecalho)

                for linha_arquivo in conteudo.splitlines():
                    linha_formatada = " " * (nivel + 6) + linha_arquivo + "\n"
                    print(linha_formatada, end="")
                    arquivo_saida.write(linha_formatada)

            except Exception as e:
                erro = " " * (nivel + 4) + f"[Erro ao ler arquivo: {e}]\n"
                print(erro, end="")
                arquivo_saida.write(erro)


# 👉 CAMINHO DO TEU PROJETO
pasta_principal = "C:\\Users\\gugas\\OneDrive\\Desktop\\controle-academia"

# 👉 DETECTA DESKTOP (COM OU SEM ONEDRIVE)
desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
if not os.path.exists(desktop):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# 👉 CRIA PASTA updates_sistema
pasta_updates = os.path.join(desktop, "arquivos")
os.makedirs(pasta_updates, exist_ok=True)

# 👉 NOME DO ARQUIVO COM DATA
agora = datetime.datetime.now()
nome_arquivo = f"controle-academia_{agora.day}_{agora.hour}_{agora.minute}.txt"

caminho_arquivo = os.path.join(pasta_updates, nome_arquivo)

# 👉 GERA O ARQUIVO
with open(caminho_arquivo, "w", encoding="utf-8") as saida:
    titulo = f"📦 RESUMO DO PROJETO: {pasta_principal}\n\n"
    print(titulo)
    saida.write(titulo)

    ler_pastas(pasta_principal, saida)

print(f"\n✅ Arquivo salvo em:\n{caminho_arquivo}")