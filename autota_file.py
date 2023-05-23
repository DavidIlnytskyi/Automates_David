'''This module contains simulation of my life'''
from random import random

class Simulation:
    '''Simulates my life'''
    def __init__(self):
        self.state = None
        self._time = None

    def set_simulation_input(self, time=24):
        '''Sets number of time'''
        self._time = time

    def simulate(self):
        '''Simulates'''
        State = States()
        self.state = State.CHILL
        for hour in range(0, 2 * 30 * self._time + 30, 30):

            if hour % 24 < 1440:
                hour = hour % 1440

            if self.state == State.SLEEP:
                if random() <= 0.9 and int(hour/60) == 9 and hour%60 == 0:
                    print(f'{self.get_time(hour)} Good morning world! Let\'s make my morning routine.')
                    self.state = State.EAT
                elif int(hour//60) == 10 and hour%60 == 30:
                    print(f'{self.get_time(hour)} I have overslept this time, this is bad')
                    self.state = State.EAT
                else:
                    print(f'{self.get_time(hour)} Sleeping...')


            elif self.state == State.EAT:
                    if 9 <= int(hour//60) <= 11:
                        print(f'{self.get_time(hour)} That was awesome breakfast, time to regenerate')
                        self.state = State.CHILL
                    elif 15 <= int(hour//60) <= 16:
                        print(f'{self.get_time(hour)} That was awesome dinner')
                        self.state = State.CHILL
                    elif 19 <= int(hour//60) <= 20:
                        print(f'{self.get_time(hour)} That was awesome supper')
                        self.state = State.CHILL
                    else:
                        self.state = State.STUDY

            elif self.state == State.CHILL:
                if random() >= 0.6:
                    print(f'{self.get_time(hour)} I have to rest')
                    self.state = State.COMMUNICATE
                elif 10 <= int(hour//60) <= 21:
                    print(f'{self.get_time(hour)} Going on a walk')
                    self.state = State.WALK
                else:
                    print(f'{self.get_time(hour)} Hm, let\'s watch Stranger Things')
                    self.state = State.MOVIE

            elif self.state == State.COMMUNICATE:
                if random() >= 0.6 and int(hour//60) == 0:
                    print(f'{self.get_time(hour)} It was fun to communicate with you.')
                    self.state = State.SLEEP_READY

                elif int(hour//60) == 1 and hour%60 in (0, 30):
                    print(f'{self.get_time(hour)} Talking with friends')
                    self.state = State.SLEEP_READY

                elif int(hour//60) in (21, 22, 16, 17, 11, 12):
                    print(f'{self.get_time(hour)} Talking with friends')
                    self.state = State.STUDY

                else:
                    print(f'{self.get_time(hour)} Talking with friends')

            elif self.state == State.SLEEP_READY:
                if random() >= 0.2:
                    print(f'{self.get_time(hour)} I have to get ready to sleep')
                    self.state = State.SLEEP
                else:
                    print(f'{self.get_time(hour)} I have to get ready for sleep')
                    self.state = State.PROCRASTINATE

            elif self.state == State.WALK:
                if random() >= 0.2:
                    print(f'{self.get_time(hour)} Walking')
                    self.state = State.STUDY
                else:
                    print(f'{self.get_time(hour)} Walking')


            elif self.state == State.MOVIE:
                if random() > 0.1 and 10 <= int(hour//60) <= 21:
                    print(f'{self.get_time(hour)} This one is the last one!')
                    self.state = State.STUDY
                elif not 10 <= int(hour//60) <= 23:
                    print(f'{self.get_time(hour)} This one is the last one!')
                    self.state = State.SLEEP_READY
                else:
                    print(f'{self.get_time(hour)} Let\'s watch one more')

            elif self.state == State.STUDY:
                if 15 <= int(hour//60) <= 16:
                    print(f'{self.get_time(hour)} Studying')
                    self.state = State.EAT
                elif 19 <= int(hour//60) <= 20:
                    print(f'{self.get_time(hour)} Studying')
                    self.state = State.EAT
                elif int(hour//60) == 22:
                    print(f'{self.get_time(hour)} Studying')
                    self.state = State.CHILL
                else:
                    print(f'{self.get_time(hour)} Studying')

            elif self.state == State.PROCRASTINATE:
                if 9 >= int(hour//60) >= 0:
                    if random() >= 0.9:
                        print(f'{self.get_time(hour)} Let\'s check Instagram')
                    else:
                        print(f'{self.get_time(hour)} Let\'s check Instagram')
                        self.state = State.SLEEP

    @staticmethod
    def get_time(hour):
        '''Return hour representation'''
        return f'{hour//60 if not hour//60 == 0 else "00"}:{hour%60 if not hour%60 == 0 else "00"}:'

class States:
    '''Class contains states that David can be in'''
    def __init__(self):
        '''Containts all states'''
        States.SLEEP = 1
        States.STUDY = 2
        States.EAT = 3
        States.COMMUNICATE = 4
        States.WALK = 5
        States.CHILL = 6
        States.SLEEP_READY = 7
        States.MOVIE = 8
        States.PROCRASTINATE = 9

David = Simulation()
David.set_simulation_input(24)
David.simulate()
