import nmmo
from nmmo import Agent
from ijcai2022nmmo import CompetitionConfig, TeamBasedEnv, scripted
import pdb

class Config(CompetitionConfig):
    SAVE_REPLAY = "demo"

def printConfig(config):
    """printConfig.
    Print the Game Configuration and Settings.
    Args:
        config:
    """
    for attr in dir(config):
        if not attr.startswith('__'):
            print('{}:{}'.format(attr, getattr(config,attr)))

if __name__ == "__main__":
    # Creating the Env objecti.
    # This is the global Env. 
    # Use the Team Based env for the actual settings.
    config = Config()
    env = TeamBasedEnv(config=config)
    scripted_api = scripted.CombatTeam(None, config)
    obs = env.reset()
    t, horizon = 0, 32
    while True:
        env.render()
        decision = {}
        for team_id, o in obs.items():
            decision[team_ids] = scripted_ai.act(o)
        env.step(action)
        t += 1
        if t >= horizon:
            break
    env.terminal()


