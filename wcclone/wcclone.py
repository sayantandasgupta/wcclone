import click

from wcclone.utils import countBytes, countLines, countWords


@click.command()
@click.option('-c', '--bytes', is_flag=True, default=False, help="print the byte counts")
@click.option('-l', '--lines', is_flag=True, default=False, help="print the newline counts")
@click.option('-w', '--words', is_flag=True, default=False, help="print the word counts")
@click.argument('file', type=click.File('rb', lazy=True), default='-')
def main(bytes, lines, words, file):

    file_name = file.name if file.name != '-' else ''

    data = file.readlines()

    lineCount = countLines(fileData=data)
    wordCount = countWords(fileData=data)
    byteCount = countBytes(fileData=data)

    if lines and bytes:
        click.echo(f"  {lineCount} {byteCount} {file_name}")

    elif lines and words:
        click.echo(f"  {lineCount} {wordCount} {file_name}")

    elif words and bytes:
        click.echo(f"  {wordCount} {byteCount} {file_name}")

    elif lines:
        click.echo(f"  {lineCount} {file_name}")

    elif bytes:
        click.echo(f"  {byteCount} {file_name}")

    elif words:
        click.echo(f"  {wordCount} {file_name}")

    else:
        click.echo(f"  {lineCount} {wordCount} {byteCount} {file_name}")