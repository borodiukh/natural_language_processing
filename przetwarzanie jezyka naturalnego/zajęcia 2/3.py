import re


with open('text.txt') as input_file:
    input_file = input_file.readlines()
    with open('answer.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            tmp = re.sub('(arse|arsehead|arsehole|ass|asshole|bastard|bitch|bloody|bollocks|brotherfucker|bugger|bullshit|cock|cocksucker|crap|cunt|damn|dick|dickhead|dyke|fatherfucker|frigger|fuck|goddamn|godsdamn|hell|horseshit|kike|motherfucker|nigga|nigra|piss|prick|pussy|shit|shite|sisterfucker|slut|spastic|twat|wanker)', '---', line)
            output_file.write(tmp)
