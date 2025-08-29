from sample_madlibs import adventure, recipe, superhero, vacation
import random


if __name__ == "__main__":
    m = random.choice([adventure, recipe, superhero, vacation])
    m.madlibs()