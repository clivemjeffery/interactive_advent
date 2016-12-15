import click
from datetime import datetime

@click.command()
@click.option('--day', default=datetime.now(), help='The December day to show advent for.')

def run_advent(count, name):
    click.echo('Running advent for %s!' % day.strftime('%Y/%m/%d %H:%M:%S'))

if __name__ == '__main__':
    run_advent()
