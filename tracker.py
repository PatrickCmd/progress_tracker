'''
A command line program using python 3 to help boot camp 
participants track their progress using the learning map.
A user is able to add skills, view a list of all the skills added, 
indicate the skills studied, view a list of skills I’ve studied, 
view a list of skills I haven’t studied yet and see their learning progress.
'''


import click
from collections import defaultdict


@click.command()
@click.option('--command', type=click.Choice(['show_options']), 
                help='chose the choice for specific command')
def cli(command):
    intro()

    skills = defaultdict(list)
    
    if command == 'show_options':
        loop = True

        while loop:
            print_options()
            option = click.prompt('Enter your option', type=int)

            if option == 1:
                click.echo('Adding skill')
                skill = click.prompt('Enter skill to study', type=str)
                add_skill(skills, skill)
                click.echo('{} skill added' .format(skill))
            elif option == 2:
                added_skills = view_skills(skills)
                if len(added_skills) == 0:
                    click.echo('No skills yet added')
                else:
                    print_view_skills(added_skills)
            elif option == 3:
                skill_studied = click.prompt('Enter skill to mark studied', 
                                            type=str)
                mark_skill_studied(skills, skill_studied)
                click.echo('{} added to studied list' .format(skill_studied))
            elif option == 4:
                skills_studied = view_studied_skills(skills)
                if len(skills_studied) == 0:
                    click.echo('No skill studied yet')
                else:
                    print_studied_skills(skills_studied)
            elif option == 5:
                not_studied_skills = skills_not_studied(skills)
                if len(not_studied_skills) == 0:
                    click.echo('No skills added yet')
                else:
                    print_unstudied_skills(not_studied_skills)
            elif option == 6:
                progress_tracker(skills)
            elif option == 7:
                click.clear() # clearing terminal
            elif option == 0:
                click.echo('Application ended')
                loop = False
                


def intro():
    click.secho('-'*100, fg='red')
    click.secho('Welcome to progress tracker', fg='yellow')
    click.secho('Type tracker --help to show list of options', 
                fg='yellow')
    click.secho('-'*100, fg='red')


def print_options():
    '''Function to show options menu'''
    click.secho('===========SELECT FROM OPTIONS MENU========', fg='red')
    click.echo('1. Add skill')
    click.echo('2. View Skills')
    click.echo('3. Skill studied')
    click.echo('4. View skills studied')
    click.echo('5. Skills not yet studied')
    click.echo('6. Track your progress')
    click.echo('7. Clear screen/Terminal')
    click.echo('0. Exit')
    click.secho('='*70, fg='red')

def add_skill(skills, skill):
    key = 'skills_added'
    if skill not in skills[key]:
        skills[key].append(skill)
    else:
        click.echo('Skill already exists')

def view_skills(skills):
    added_skills = skills['skills_added']
    return added_skills

def mark_skill_studied(skills, skill):
    key = 'skills_studied'
    if skill in skills['skills_added']:
        skills[key].append(skill)
    else:
        click.echo('Skill does not added yet. Please add it first')

def view_studied_skills(skills):
    studied_skills = skills['skills_studied']
    return studied_skills

def skills_not_studied(skills):
    key = 'skills_not_studied'
    skills_unstudied = [skill for skill in skills['skills_added'] 
                        if skill not in skills['skills_studied']]
    skills[key] = skills_unstudied
    return skills[key]

def print_view_skills(added_skills):
    click.echo('Added skills: {}' .format(', '.join(added_skills)))

def print_studied_skills(studied_skills):
    click.echo('Studied skills: {}' .format(', '.join(studied_skills)))

def print_unstudied_skills(unstudied_skills):
    click.echo('skills not yet studied: {}' .format(', '.join(unstudied_skills)))

def progress_tracker(skills):
    for category, lists in skills.items():
        click.echo('{} : {}' .format(category, 
                    ', '.join(lists)))
