def load_from_txt(FILE_PATH: str) -> list[str]:
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            # Remove o '\n' de cada linha
            rows = file.read().splitlines()
        return rows
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []
