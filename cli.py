import click
from PyInquirer import prompt

truc = None

@click.group()
def main():
    """ Un Cli """
    pass

@main.command()
@click.argument('name')
def greet(name):
    click.echo("Alu " + name)

def load(name='truc'):
    with open(name+'.txt', 'r') as f:
        truc=f.readlines()
    return truc

def save(lignes, name='truc'):
    with open(name+'.txt', 'w') as f:
        f.writelines(lignes)

def load_touslestrucs():
    with open('_tas.txt', 'r') as f:
        touslestrucs = f.readlines()
    return touslestrucs

def save_touslestrucs(t):
    with open('_tas.txt', 'w') as f:
        f.writelines(t)

@main.command()
def reset():
    """ réinitialisation à un seul truc nommé truc """
    touslestrucs = ['truc']
    save_touslestrucs(touslestrucs)
    save([], 'truc')
    click.echo('inititialisation')

@main.command()
@click.option('--name', prompt='truc à créer')
def create(name = 'truc'):
    """ créer un nouveau fichier truc """
    touslestrucs = load_touslestrucs()
    if name not in touslestrucs:
        touslestrucs.append(name)
        save_touslestrucs(touslestrucs)
        save([], name)
        click.echo('création')
    else:
        click.echo('existe déjà')

@main.command()
def list():
    """ lister tous les trucs """
    touslestrucs = load_touslestrucs()
    for i in touslestrucs:
        click.echo(i)

@main.command()
def add():
    """ ajouter une ligne à un truc """
    touslestrucs = load_touslestrucs()
    questions = [
        {
            'type' : 'list',
            'name' : 'truc',
            'message' : 'Dans quel truc',
            'choices' : touslestrucs
        },
        {
            'type' : 'input',
            'name' : 'ligne',
            'message' : 'Une ligne'
        }
    ]
    answer = prompt(questions)
    if not answer:
        click.echo('rien fait')

    truc = load(answer['truc'])
    truc.append(answer['ligne'])
    save(truc, answer['truc'])
    click.echo(answer['ligne'] + ' est ajouté à ' + answer['truc'])


@main.command()
@click.argument('name')
def print(name='truc'):
    truc = load(name)
    for i in truc:
        click.echo(i)

if __name__ == "__main__":
    main()

