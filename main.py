from pyscript import document


def result_checker(e):
    # these are the names of the club members, just using made-up names
    club_members = [
        'Orion Vale', 'Lyra Solstice', 'Cassian Voss',
        'Nova Calder', 'Elio Marlowe', 'Sable Quinn'
    ]

    # gets what was typed into the first name box
    f_name = document.getElementById('first_name').value.strip()

    # same thing but for the last name box
    l_name = document.getElementById('last_name').value.strip()

    # joins both names together with a space in between
    candidate = f_name + ' ' + l_name

    # checks if the name is already on the list
    # lower makes capital letters not matter, like in the original code
    member_checker = candidate.lower() in [
        member.lower() for member in club_members
    ]

    # the first message is for false, the second is for true
    # this lets us pick a message without using if or else
    messages = (
        f'Sorry {candidate}, your name is not on the list.',
        f'Congratulations {candidate}! You are now part of the ICT club.'
    )

    # shows the correct message in the result box on the webpage
    document.getElementById('output').innerText = messages[member_checker]
