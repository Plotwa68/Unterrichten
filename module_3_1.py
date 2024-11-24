calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(satz):
    count_calls()
    return len(satz), satz.upper(), satz.lower()


def is_contains(satz, aufsatz):
    count_calls()
    for i in aufsatz:
        if satz.lower() in i.lower():
            return True

    return False


print(string_info('Capybara'))

print(string_info('Armageddon'))


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)