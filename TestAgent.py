import Environment
import Agent

ROWS = 12
COLS = 12
SIGHT = 3

env = Environment.GridWorld(tot_row=ROWS, tot_col=COLS)
env.reset()

agent = Agent.AgentRL(env, SIGHT)

while True:
    agent.updateWorldObservation()
    agent.render()

    action = agent.choseAction()
    print(action)

    observe, terminate, goal_picked, reward = env.execute(action)

    if goal_picked:
        print("You have picked a goal, reward = {}".format(reward))
        agent.updateWorldObservation()
        agent.render()
        action = agent.choseAction()
        print(action)
        env.render()

        break
    if terminate:
        print("Game result: ", reward)
        break

    #input("Press the <Enter> key to continue...")