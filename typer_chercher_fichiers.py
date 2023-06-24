import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()

@app.command('run')
def main(extension: str, 
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
    """Affiche les fichiers trouvés avec l'extension donnée
    """

    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()
    
    if not directory.exists():
        typer.echo(f"Le dossier ''{directory}'' n'existe pas !")
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm("Voulez vous vraiment supprimer tous les fichiers trouvés ? ", abort=True)
        for file in files:
            file.unlink()
            typer.echo(f"Suppression du fichier {file} !")
    else:
        typer.echo(f"Fichiers trouvés avec l'extension {extension}: ")
        for file in files:
            typer.echo(file)

@app.command()
def search(extension: str, directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher.")):
    """Chercher les fichiers avec l'extension donnée
    """
    main(extension=extension, directory=directory, delete=False)

@app.command()
def delete(extension: str, directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher.")):
    """Supprimer les fichiers avec l'extension donnée
    """
    main(extension=extension, directory=directory, delete=True)

if __name__ == "__main__":
    # typer.run(main)
    app()
