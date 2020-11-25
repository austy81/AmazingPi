import pygame
import random
import os
import time


script_path = os.path.dirname(os.path.realpath(__file__))
questions_dir = os.path.join(script_path, 'samples', 'questions')
answers_dir = os.path.join(script_path, 'samples', 'answers')


def get_random_file(dir_path):
    audio_files = [f"{dir_path}/{f}" for f in os.listdir(dir_path) if f.endswith('.wav') or f.endswith('.mp3')]
    return random.choice(audio_files)


pygame.mixer.init()


def play():
    question = pygame.mixer.Sound(get_random_file(questions_dir))
    answer = pygame.mixer.Sound(get_random_file(answers_dir))

    question.play()
    time.sleep(question.get_length() + 0.5)

    answer.play()
    time.sleep(answer.get_length())


if __name__ == "__main__":
    play()
