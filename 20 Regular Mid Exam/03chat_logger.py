command = input()

chat_log = []
while command != 'end':
    input_data = command.split()
    action = input_data[0]
    message = input_data[1]

    if action == 'Chat':
        chat_log.append(message)
    elif action == 'Delete':
        if message in chat_log:
            chat_log.remove(message)
    elif action == 'Edit':
        if message in chat_log:
            new_message = input_data[2]
            index = chat_log.index(message)
            chat_log[index] = new_message
    elif action == 'Pin':
        if message in chat_log:
            chat_log.remove(message)
            chat_log.append(message)
    elif action == 'Spam':
        spam = [input_data[msg_idx] for msg_idx in range(1, len(input_data))]
        chat_log.extend(spam)
    command = input()

print(*chat_log, sep='\n')
