import argparse
import json
import time

from council import Council
from persona import Persona


def eval_one_jailbreak(id: int, personas: list[Persona]):
    start = time.time()
    with (open("datasets/jailbreaks.json", "r") as file):
        prompt = json.load(file)["jailbreak"][id]
        council = Council(personas)
        print(council.decide(prompt))

    print(f"Time taken: {time.time() - start}")


def main():
    parser = argparse.ArgumentParser(
        prog='Consilium',
        description='Tool that uses AI to detect attacks on AI.')

    parser.add_argument('-i','--input', help="The path to the file containing the input")
    parser.add_argument('-o','--output', help="The path to the file containing the input")
    parser.add_argument('-p','--personas', help="The path to the file containing the personas", nargs='+')
    parser.add_argument('-v','--verbose', help="Prints the output", action='store_true')


if __name__ == "__main__":
    main()
