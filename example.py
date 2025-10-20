import os
from github_release_counter.github_api import GitHubAPI, RepoFormatError, GitHubAPIError

# --- Ejemplo de uso como librería ---
print("--- Probando como librería ---")

# Reemplaza con un repositorio público que tenga lanzamientos
REPO = "jesseduffield/lazydocker"

try:
    # No se necesita token para repositorios públicos, pero se puede pasar como segundo argumento
    print(f"Creando instancia de GitHubAPI para el repositorio: {REPO}")
    api = GitHubAPI(REPO)
    
    print("Obteniendo lanzamientos...")
    releases = api.get_releases()

    if releases:
        print(f"Se encontraron {len(releases)} lanzamientos para {REPO}.")
        
        # Imprimir el tag del primer lanzamiento (el más reciente)
        print(f"El tag del último lanzamiento es: {releases[0]['tag_name']}")

        # Imprimir el número de assets del primer lanzamiento
        print(f"El último lanzamiento tiene {len(releases[0]['assets'])} assets.")
        print("-" * 20)
    else:
        print(f"No se encontraron lanzamientos para {REPO}.")

except (RepoFormatError, GitHubAPIError) as e:
    print(f"Ocurrió un error: {e}")


# --- Ejemplo de uso desde la línea de comandos ---
print("\n--- Probando desde la línea de comandos ---")

# Se usa os.system para evitar problemas de decodificación en Windows al capturar la salida.

# 1. Prueba estándar (reporte completo)
print("\n1. Obteniendo reporte completo...")
os.system(f"python -m github_release_counter.cli {REPO}")

# 2. Prueba con --tags-only
print("\n2. Obteniendo solo los tags...")
os.system(f"python -m github_release_counter.cli {REPO} --tags-only")

# 3. Prueba con --assets-only
print("\n3. Obteniendo solo los assets...")
os.system(f"python -m github_release_counter.cli {REPO} --assets-only")