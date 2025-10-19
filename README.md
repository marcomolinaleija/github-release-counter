# GitHub Release Download Counter

Este script de Python te permite obtener el número total de descargas de todos los assets de los lanzamientos de un repositorio de GitHub.

## Características

- Obtiene el conteo de descargas por lanzamiento y por asset.
- Muestra el total de descargas de todos los lanzamientos.
- Manejo básico de errores para problemas de conexión o respuestas inesperadas de la API.

## Requisitos

- Python 3.x
- La librería `requests`

## Instalación

Puedes instalar este paquete directamente desde PyPI (una vez publicado) o desde el código fuente.

### Desde PyPI (próximamente)

```bash
pip install github-release-counter
```

### Desde el código fuente

1.  Clona este repositorio:
    ```bash
    git clone https://github.com/your-username/github-release-counter.git
    cd github-release-counter
    ```
2.  Instala el paquete en modo editable (para desarrollo) o normal:
    ```bash
    pip install .
    ```

## Uso

Después de la instalación, puedes ejecutar el comando `github-release-counter` directamente en tu terminal.

### Argumentos

-   `<propietario/repositorio>` (obligatorio): La ruta del repositorio de GitHub en formato `propietario/repositorio` (ej. `marcomolinaleija/github-release-counter`).
-   `--token` o `-t` (opcional): Tu Token Personal de Acceso (PAT) de GitHub. Usar un token aumenta el límite de la API de GitHub, lo que es útil para repositorios con muchos lanzamientos o para evitar interrupciones.

### Ejemplos

Para obtener las estadísticas de descargas de un repositorio:

```bash
github-release-counter marcomolinaleija/github-release-counter
```

Para usar un token de GitHub:

```bash
github-release-counter marcomolinaleija/github-release-counter --token Tu_GITHUB_TOKEN
```

### Obtener un Token Personal de Acceso (PAT) de GitHub

1.  Ve a [GitHub Settings](https://github.com/settings/tokens).
2.  Haz clic en "Generate new token" (o "Generate new token (classic)").
3.  Dale un nombre descriptivo (ej. "Release Counter Token").
4.  Selecciona los permisos necesarios. Para este script, no se necesitan permisos específicos, ya que solo lee información pública. Puedes dejarlo sin seleccionar ningún scope.
5.  Haz clic en "Generate token" y copia el token generado. ¡Guárdalo en un lugar seguro, ya que solo se muestra una vez!

## Uso como Librería

Puedes importar la función `obtener_stats_descargas` en tus propios scripts de Python para obtener los datos de los lanzamientos de forma programática.

```python
from github_release_counter.cli import obtener_stats_descargas
import os

# Reemplaza con el repositorio que quieras y tu token de GitHub si lo tienes
repo = "octocat/Spoon-Knife"
github_token = os.getenv("GITHUB_TOKEN") # O pásalo directamente como string

releases_data = obtener_stats_descargas(repo, github_token)

if releases_data:
    print(f"Se encontraron {len(releases_data)} lanzamientos para {repo}.")
    for release in releases_data:
        print(f"  Lanzamiento: {release['release_name']} (Tag: {release['tag_name']})")
        print(f"    Total de descargas del lanzamiento: {release['total_release_downloads']}")
        for asset in release['assets']:
            print(f"      Asset: {asset['name']}, Descargas: {asset['download_count']}")
else:
    print(f"No se pudieron obtener los datos de los lanzamientos para {repo}.")
```


-   Si no proporcionas `propietario/repositorio`, el script usará `marcomolinaleija/ml-player-releases` por defecto.

### Ejemplos

Para obtener las estadísticas de descargas del repositorio por defecto:

```bash
python release_download_counter.py
```

Para obtener las estadísticas de descargas de un repositorio específico (ej. `octocat/Spoon-Knife`):

```bash
python release_download_counter.py octocat/Spoon-Knife
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un error o tienes una sugerencia de mejora, por favor abre un "issue" o envía un "pull request".

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
