import click

from utils import countBytes, countLines

@click.command()
@click.option('-c', '--bytes', is_flag=True, default=False, help="print the byte counts")
@click.option('-l', '--lines', is_flag=True, default=False, help="print the newline counts")
@click.argument('file')
def main(bytes, lines, file):
    if bytes:
        try:
            res = countBytes(file)
            click.echo(f"{res} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    if lines:
        try:
            res = countLines(file)
            click.echo(f"{res} {file}")
        except FileNotFoundError:
            click.echo("File not found")

if __name__ == "__main__":
    main()