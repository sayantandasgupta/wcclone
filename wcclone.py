import click

from utils import countBytes, countLines, countWords


@click.command()
@click.option('-c', '--bytes', is_flag=True, default=False, help="print the byte counts")
@click.option('-l', '--lines', is_flag=True, default=False, help="print the newline counts")
@click.option('-w', '--words', is_flag=True, default=False, help="print the word counts")
@click.argument('file')
def main(bytes, lines, words, file):

    if lines and bytes and words:
        try:
            lineCount = countLines(file)
            wordCount = countWords(file)
            byteCount = countBytes(file)
            click.echo(f"{lineCount} {wordCount} {byteCount} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif lines and bytes:
        try:
            lineCount = countLines(file)
            byteCount = countBytes(file)
            click.echo(f"{lineCount} {byteCount} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif lines and words:
        try:
            lineCount = countLines(file)
            wordCount = countWords(file)
            click.echo(f"{lineCount} {wordCount} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif words and bytes:
        try:
            wordCount = countWords(file)
            byteCount = countBytes(file)
            click.echo(f"{wordCount} {byteCount} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif lines:
        try:
            res = countLines(file)
            click.echo(f"{res} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif bytes:
        try:
            res = countBytes(file)
            click.echo(f"{res} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    elif words:
        try:
            res = countWords(file)
            click.echo(f"{res} {file}")
        except FileNotFoundError:
            click.echo("File not found")

    else:
        try:
            lineCount = countLines(file)
            wordCount = countWords(file)
            byteCount = countBytes(file)
            click.echo(f"{lineCount} {wordCount} {byteCount} {file}")
        except FileNotFoundError:
            click.echo("File not found")


if __name__ == "__main__":
    main()
