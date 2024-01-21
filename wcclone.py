import click

@click.command()
@click.option('-c', '--bytes', is_flag=True, default=False, help="print the byte counts")
@click.option('-l', '--lines', is_flag=True, default=False, help="print the newline counts")
@click.argument('file')
def main(bytes, lines, file):
    
    if lines:
        try:
            res = countLines(file)
            click.echo(res)
        except FileNotFoundError:
            click.echo("File not found")

def countLines(file : str) -> str:
    try:
        with open(file) as f:
            lines = f.readlines()
            numLines = len(lines)
            
            return f"{numLines} {file}"
    except FileNotFoundError:
        raise FileNotFoundError

if __name__ == "__main__":
    main()