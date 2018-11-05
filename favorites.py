import click
import pprint

# dictionary for currently available categories
favdict = {'favorite_color': "none", 'favorite_food': "none", 'favorite_animal': "none"}


def cli():
    # bool variable to continue the cli until exited
    again = True
    while again != False:

        # the command prompt
        input = click.prompt(">")
        inList = list(input.split(' '))

        # put option for adding a value to the category key
        if inList[0] == 'put':
            if inList[1] in favdict:
                favdict[inList[1]] = inList[2]
                print('ok')
            else:
                print('Not a valid category use: ' + str(favdict.keys()))
            again = True
        # fetch option to print what is currently a key's value
        elif inList[0] == 'fetch':
            if inList[1] in favdict:
                click.echo(favdict[inList[1]])
            else:
                click.echo('Not a valid category use: ' + str(favdict.keys()))
            again = True
        # add option to add new keys
        elif inList[0] == 'add':
            if inList[1] not in favdict:
                favdict[inList[1]] = "none"
            else:
                click.echo('Category already available')
        # list option to get a view of all the categories and values available
        elif inList[0] == 'list':
            listAll = pprint.PrettyPrinter(indent=2)
            click.echo(listAll.pprint(favdict))
        # exit option
        elif inList[0] == 'exit':
            click.echo('Goodbye!')
            again = False
        else:
            print('Not a valid command use put [category] [item], fetch [category], add [category], list or exit')

#     if str(value) == "exit":
#         click.echo("exit here")
#     elif str(value) == "put":
#         click.echo("added favorite item")
#     elif str(value) == "fetch":
#         click.echo("fetch favorite item")
#     else:
#         raise click.BadParameter('Not a valid command. Please enter put, fetch, or exit')
#     return value
#
#
# @click.command()
# @click.prompt('>', value_proc=validate_command())
# def cli():
#     """Store Favorites
#     This example allows you to edit and fetch favorite items
#     """
