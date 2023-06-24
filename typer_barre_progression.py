import typer
import time

def main():
    nombre = range(100)
    with typer.progressbar(nombre) as progress:
        for _ in progress:
            time.sleep(0.05)
    
    typer.echo("Fin du script !!!")

if __name__ == "__main__":
    typer.run(main)
