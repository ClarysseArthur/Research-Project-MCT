def render_cmd(approaches, exits):
    for x in range(10):
        for i in range(20):
            print(' ', end='')
        print('|', end='')
        for i in range(approaches[0].get_length() - 1):
            print(' ', end='')
            print(':', end='')
        print(' ', end='')
        print('|', end='')
        for i in range(exits[0].get_length() - 1):
            print(' ', end='')
            print(':', end='')
        print(' ', end='')
        print('|')

    for x in range(20):
        print('─', end='')
    for x in range(approaches[0].get_length() + 10 + exits[0].get_length()):
        print(' ', end='')
    for x in range(19):
        print('─', end='')
    print('─')

    for x in range(max(approaches[1].get_length(), approaches[3].get_length()) + max(exits[1].get_length(), exits[3].get_length())):
        for i in range(19 + approaches[0].get_length() + 10 + exits[0].get_length()):
            print(' ', end='')
        print(' ')

        if x < exits[3].get_length() - 1:
            for i in range(10):
                print('•', end='')
                print(' ', end='')
        elif x == exits[3].get_length() - 1:
            for i in range(20):
                print('─', end='')
        elif x - exits[3].get_length() < approaches[3].get_length() - 1:
            for i in range(10):
                print('•', end='')
                print(' ', end='')
        elif x - exits[3].get_length() == approaches[3].get_length() - 1:
            for i in range(20):
                print('─', end='')
        else:
            for i in range(20):
                print(' ', end='')
            
        for i in range(approaches[0].get_length() + 10 + exits[0].get_length()):
            print(' ', end='')

        if x < approaches[1].get_length() - 1:
            for i in range(9):
                print('•', end='')
                print(' ', end='')
            print('• ')
        elif x == approaches[1].get_length() - 1:
            for i in range(19):
                print('─', end='')
            print('─')
        elif x - approaches[1].get_length() < exits[1].get_length() - 1:
            for i in range(9):
                print('•', end='')
                print(' ', end='')
            print('• ')
        elif x - approaches[1].get_length() == exits[1].get_length() - 1:
            for i in range(19):
                print('─', end='')
            print('─')
        else:
            for i in range(19):
                print(' ', end='')
            print(' ')

    for x in range(10):
        for i in range(20):
            print(' ', end='')
        print('|', end='')
        
        for i in range(exits[2].get_length() - 1):
            print(' ', end='')
            print(':', end='')
        print(' ', end='')
        print('|', end='')

        for i in range(approaches[2].get_length() - 1):
            print(' ', end='')
            print(':', end='')
        print(' ', end='')
        print('|')