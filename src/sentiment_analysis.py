import io

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchtext
from happytransformer import HappyTextClassification


def create_model(model, version):
    return HappyTextClassification(model, version)



def main(version = "finetunned", test_cases = True):
    happy_tc = 0
    if version == "finetunned":
        happy_tc = create_model("DISTILBERT", "distilbert-base-uncased-finetuned-sst-2-english")
    elif version == "pretrained":
        happy_tc = create_model("DISTILBERT", "distilbert-base-uncased", num_labels=3)
    else:
        print("arguments of model version 'pretrained' and 'finetunned' not correct")

    if test_cases == True:
        print(happy_tc.classify_text("I am so happy about this!"))
        print(happy_tc.classify_text("This is the most dissapointing news I have had in a while."))
        print(happy_tc.classify_text("This house was built three years ago."))
        print(happy_tc.classify_text("I am amazed by how amazing these nuts are!"))
        print(happy_tc.classify_text("They have no milk, this sucks."))


if __name__ == "__main__":
    main()
