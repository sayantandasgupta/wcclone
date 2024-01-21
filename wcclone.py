import click

@click.command()
@click.argument('file')
def count(file):
    try:
        f = open(file)
    except FileNotFoundError as E:
        click.echo("File not found")


    # click.echo(f"Sum is {sum}")

if __name__ == "__main__":
    count()