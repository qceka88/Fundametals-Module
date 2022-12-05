##################################### variant 01 #####################################

followers = {}

while True:
    command = input()
    if command == 'Log out':
        break

    data = command.split(': ')
    action = data[0]
    username = data[1]

    if action == 'New follower':
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
    elif action == 'Like':
        number_of_likes = int(data[2])
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
        followers[username]['likes'] += number_of_likes
    elif action == 'Comment':
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
        followers[username]['comments'] += 1
    elif action == 'Blocked':
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f'{len(followers)} followers')

for name, data in followers.items():
    total = data['likes'] + data['comments']
    print(f'{name}: {total}')


##################################### variant 02 #####################################

class NewFollower:

    def __init__(self, some_dict, some_data):
        self.some_dict = some_dict
        self.some_data = some_data
        self.message = ''

    def new_follower(self):
        username = self.some_data[1]
        if username not in self.some_dict:
            self.some_dict[username] = {'likes': 0, 'comments': 0}

    def return_data(self):
        return self.some_dict, self.message


class NewLike:

    def __init__(self, some_dict, some_data):
        self.some_dict = some_dict
        self.some_data = some_data
        self.message = ''

    def new_like(self):
        username, number_of_likes = self.some_data[1], int(self.some_data[2])
        if username not in self.some_dict:
            self.some_dict[username] = {'likes': 0, 'comments': 0}
        self.some_dict[username]['likes'] += number_of_likes

    def return_data(self):
        return self.some_dict, self.message


class NewComment:

    def __init__(self, some_dict, some_data):
        self.some_dict = some_dict
        self.some_data = some_data
        self.message = ''

    def new_comment(self):
        username = self.some_data[1]
        if username not in self.some_dict:
            self.some_dict[username] = {'likes': 0, 'comments': 0}
        self.some_dict[username]['comments'] += 1

    def return_data(self):
        return self.some_dict, self.message


class NewBlock:

    def __init__(self, some_dict, some_data):
        self.some_dict = some_dict
        self.some_data = some_data
        self.message = ''

    def new_block(self):
        username = self.some_data[1]
        if username not in self.some_dict:
            self.message = f"{username} doesn't exist.\n"
        else:
            del self.some_dict[username]

    def return_data(self):
        return self.some_dict, self.message


class Follower:

    def __init__(self, some_dict, some_input):
        self.some_dict = some_dict
        self.some_input = some_input
        self.log = ''

    def action(self):
        data = self.some_input.split(': ')
        action = data[0]

        if action == 'New follower':
            new = NewFollower(self.some_dict, data)
            new.new_follower()
            self.some_dict = new.return_data()[0]
            self.log = new.return_data()[1]
        elif action == 'Like':
            like = NewLike(self.some_dict, data)
            like.new_like()
            self.some_dict = like.return_data()[0]
            self.log = like.return_data()[1]
        elif action == 'Comment':
            comment = NewComment(self.some_dict, data)
            comment.new_comment()
            self.some_dict = comment.return_data()[0]
            self.log = comment.return_data()[1]
        elif action == 'Blocked':
            block = NewBlock(self.some_dict, data)
            block.new_block()
            self.some_dict = block.return_data()[0]
            self.log = block.return_data()[1]

    def return_to_main(self):
        return self.some_dict, self.log


class Main:

    def __init__(self):
        self.followers = {}
        self.log_file = ''

    def read_input(self):
        while True:
            command = input()
            if command == 'Log out':
                break
            extract = Follower(self.followers, command)
            extract.action()
            self.followers = extract.return_to_main()[0]
            self.log_file += extract.return_to_main()[1]

    def output_information(self):
        self.log_file += f'{len(self.followers)} followers\n'
        for name, data in self.followers.items():
            total = data['likes'] + data['comments']
            self.log_file += f'{name}: {total}\n'

    def __repr__(self):
        return f'{self.log_file}'


output = Main()
output.read_input()
output.output_information()
print(output)


#'''' Problem conditions are in .docx .jpg files!'''