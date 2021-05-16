from gym.envs.registration import register

register(
    id='game-env-v0',
    entry_point='gym_neutreeko.envs:NeutreekoEnv',
)