import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"),
         extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    Affiche les fichiers trouvés avec l'extension donnée
    """
    # print(delete)
    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    # extension = typer.prompt("Quelle extension chercher ?")
    if delete:
        msg_alert = typer.style("Suppression des fichiers.", fg=typer.colors.WHITE, bg=typer.colors.RED)
        typer.echo({msg_alert})
        # confirm = typer.confirm("Etes vous sûr ??? ", abort=True)
        # if not confirm:
        #     typer.echo("On annule l'opération.")
        #     raise typer.Abort()
        
    # print("Suppression des fichiers !")

@app.command("search")
def search_py():
    main(delete=False, extension="py")

@app.command("delete")
def delete_py():
    main(delete=True, extension="py")

# typer.run(main)
app()