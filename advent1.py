import click
from datetime import datetime
from mote import Mote
import time


mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

# A dictionary of days mapped to a list of mote numbers (first is the strip, rest are motes)
day_motes = {
    1:[3,1],
    2:[3,15],
    3:[3,7],
    9:[3,4,5],
    10:[3,13],
    19:[3,9,10,11],
    20:[1,7],
    21:[4,1],
    24:[1,12,13,14,15,16]
}

@click.command()
@click.option('--day', default=datetime.today().day, help='The December day to show advent for.')

def run_advent(day):
    click.echo('Running advent for December {}.'.format(day))
    while True:
        mote.clear()
        for iday in range(1, day+1):
            if (iday in day_motes):
                mote_list = day_motes[iday]
                click.echo('{} : {}'.format(iday, mote_list))
                for imote in range(1, len(mote_list)):
                    strip = mote_list[0]
                    click.echo('calling mote.setpixel({},{},red,green,blue)'.format(strip, mote_list[imote]))
                    mote.set_pixel(strip, mote_list[imote] - 1, 100, 100, 100)
            else:
                click.echo('{} : motes not yet defined.'.format(iday))
            mote.show()
            time.sleep(0.5)
        time.sleep(5)


if __name__ == '__main__':
    run_advent()
