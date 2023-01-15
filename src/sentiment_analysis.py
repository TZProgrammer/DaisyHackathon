import io
import os
import time

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchtext
from happytransformer import HappyTextClassification


def get_model(model, trained):
    if trained == "finetunned":
        return HappyTextClassification(model, "distilbert-base-uncased-finetuned-sst-2-english")
    elif trained == "pretrained":
        return HappyTextClassification(model, "distilbert-base-uncased", num_labels=3)
    else:
        print("arguments of model version 'pretrained' and 'finetunned' not correct")


def run_testcases(model):
    print(model.classify_text("I am so happy about this!"))
    print(model.classify_text("This is the most dissapointing news I have had in a while."))
    print(model.classify_text("This house was built three years ago."))
    print(model.classify_text("I am amazed by how amazing these nuts are!"))
    print(model.classify_text("They have no milk, this sucks."))

def get_str_diff(new_string, old_string):
    return new_string[len(old_string):]


def main(trained = "finetunned", test_cases = True):

    happy_tc = get_model("DISTILBERT", trained)

    if test_cases == True:
        run_testcases(happy_tc)
        return 0

    stream_path = "../results/stream/transcription.txt"
    max_time = 100
    start = time.time()
    previous_dialogue = ""
    prev_mod_time = -1
    while time.time() - start < max_time:
        time.sleep(0.05)
        
        if(os.stat(stream_path).st_mtime == prev_mod_time):
            continue

        with open(stream_path, 'r') as transcription_file:
            dialogue = transcription_file.read().strip()

        if((len(dialogue) - len(previous_dialogue) < 20) or (dialogue == previous_dialogue) or not (dialogue[-1] == '.' and dialogue[-2] != '.')):
            continue

        str_diff = get_str_diff(dialogue, previous_dialogue)
        print(f"{happy_tc.classify_text(str_diff)}: {str_diff}")
        previous_dialogue = dialogue





if __name__ == "__main__":
    main(trained = "finetunned", test_cases = False)
