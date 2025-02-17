from twitchbot import sql_commands


class Viewer:
    def __init__(self):
        self.uid = ""
        self.honor = 0

        self.join_message_check = None  # implemented
        # ^ if None then not checked yet, if False then no message
        self.last_seen = 0  # implemented
        self.time_before_last_seen = 0  # implemented

        self.points = (
            0
        )  # points should be loaded on creation and updated/written periodically
        self.seconds = {}  # key = each game, value = seconds
        self.chat = []  # implemented, list of username, time of message, game, date
        self.chat_line_dict = (
            {}
        )  # implemented, just adds amount of chatlines together as a number for each game

        self.invited_by = None

        self.old_uid = 0
        self.last_honored = 0
        self.last_dishonored = 0

        self.trivia_answers = 0

        self.last_seen_date = None


def create_all_viewerobjects(getviewers, general):
    # print(getviewers)
    for viewer in getviewers:
        if viewer not in general.viewer_objects:
            if sql_commands.get_uid_from_username(viewer) is False:
                # print(34, viewer)
                pass
            else:
                create_viewer = Viewer()
                create_viewer.name = viewer
                general.viewer_objects[viewer] = create_viewer
                general.viewer_objects[viewer].uid = sql_commands.get_uid_from_username(
                    viewer
                )


def add_one_viewerobject(
    general, viewer
):  # saving viewer objects to general class variable
    if viewer not in general.viewer_objects:
        if sql_commands.get_uid_from_username(viewer) is False:
            pass
        else:
            create_viewer = Viewer()
            create_viewer.name = viewer
            general.viewer_objects[create_viewer.name] = create_viewer
            general.viewer_objects[viewer].uid = sql_commands.get_uid_from_username(
                viewer
            )


def time_honor_movement(viewer, general):
    general.viewer_objects[viewer].honor += (
        viewer.chat * 0.15
    )  # each chatline = .15 of a point
    general.viewer_objects[viewer].honor += viewer.seconds * 0.01
    # 60 seconds in a minute, 10 minutes = 600 * .01 = 60 points


def chat_honor_movement(
    viewer, message, general
):  # this entire thing should be moved to botcommands
    starting_val = general.starting_val
    if viewer not in general.viewer_objects:
        pass
    else:
        if message.startswith(starting_val + "honor"):
            # this should give points both to honored person and person who honored them
            general.viewer_objects[viewer].honor += 100
        elif message.startswith(starting_val + "dishonor"):
            general.viewer_objects[viewer].honor -= 150
        else:
            cursewords = ["shit", "fuck", "gay", "ghey", "cunt"]
            goodwords = []
            commands = ["-help", "-discord"]
            words_list = message.split(" ")
            for i in words_list:
                if i in cursewords:
                    general.viewer_objects[viewer].honor -= 1
                elif i in goodwords:
                    general.viewer_objects[viewer].honor += 0.5
                elif i in commands:
                    general.viewer_objects[viewer].honor += 0.5


def invite_honor_movement(general, inviter_viewer):
    general.viewer_objects[inviter_viewer].honor += 10


# for sublist in uid, chatcounter += 1, then write that number to db
def save_chat_for_sql(username, date, formatted_time, message, game, general):
    uid = sql_commands.get_uid_from_username(username)
    if uid is False:
        pass
    elif username not in general.viewer_objects:
        add_one_viewerobject(general=general, viewer=username)
        general.viewer_objects[username].chat.append(
            [date, formatted_time, message, game]
        )
    else:
        general.viewer_objects[username].chat.append(
            [date, formatted_time, message, game]
        )


# the day will always be current day
def save_seconds_for_sql(getviewers, game, seconds, general):
    for username in getviewers:
        if username not in general.viewer_objects:
            pass
        else:
            uid = sql_commands.get_uid_from_username(username)
            if uid is False:
                pass

            if game not in general.viewer_objects[username].seconds:
                general.viewer_objects[username].seconds[game] = 0
            else:
                general.viewer_objects[username].seconds[game] += seconds
