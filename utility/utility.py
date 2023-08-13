import re
import random
from constants.response_list import *



def message_probability(user_message, recognised_words, required_words=[]):
    word_count = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            word_count += 1

    # Calculates the percent of recognised words in a user message 
    # i.e., how many words matched among recognized words(split message)
    percentage = float(word_count) / float(len(recognised_words))

    # Checks that the required words are in the string
    # we check for None, because a None list is not iterable
    if(required_words is not None):
        for word in required_words:
            if word not in user_message:
                has_required_words = False
            break

    # Must either have the required words for us to calculate the percentage. 
    """
    if the required_words is not None(i.e., has some value), and if any of our
    responses do not have that word, then we return 0(indicating not matched.)
    """ 
    if has_required_words:
        return int(percentage * 100)
    else:
        return 0




def check_all_responses(message):
    ordered_msg_prob_dict = {}

    # insert responses to dict according to message probablity
    def add_to_ordered_msg_prob_dict(bot_response, list_of_words, required_words=[]):
        nonlocal ordered_msg_prob_dict
        ordered_msg_prob_dict[bot_response] = message_probability(message, list_of_words, required_words)

    
    for key in response_dict:
        add_to_ordered_msg_prob_dict(key,response_dict.get(key),required_words=response_required_words_dict.get(key))

    best_response = max(ordered_msg_prob_dict, key=ordered_msg_prob_dict.get)
    # print(ordered_msg_prob_dict)
    # print(f'Best match = {best_response} | Score: {ordered_msg_prob_dict[best_response]}')

    if ordered_msg_prob_dict[best_response] < 1:
        return unknown()
    else:
        return best_response


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_responses(split_message)
    return response


def unknown():
     rand = random.randrange(5)
     return random_response_list[rand]

