
from lab2_model import ClassroomAgent

agent = ClassroomAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]

for step, percept in enumerate(percepts, 1):

    previous_mode = agent.previous_mode

    target_mode, send_command = agent.act(*percept)

    if send_command:
        outcome = "SEND COMMAND"
    else:
        outcome = "NO COMMAND"

    print("Step:", step)
    print("Previous mode:", previous_mode)
    print("Percept:", percept)
    print("Target mode:", target_mode)
    print("Outcome:", outcome)
    print("-------------------------")
