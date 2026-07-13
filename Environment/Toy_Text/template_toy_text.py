def play_game(environement_training,environement_test,agent,NUMBER_EPISODE,NUMBER_TEST):
    print("Begin training")
    for episode in range(NUMBER_EPISODE):
        finish = False
        observation = environement_training.reset()[0]

        if (episode % 100 == 0):
            print("pourcentage ", round(episode / NUMBER_EPISODE, 3),"%")

        while not finish:
            action = agent.make_a_choice(observation)
            old_obs = observation
            observation, reward, finish, truncated, info = environement_training.step(action)
            agent.learn(old_obs, action,observation, reward, finish)

    environement_training.close()

    print("Begin real game")

    agent.print_memory()
    for _ in range(NUMBER_TEST):
        finish = False
        observation = environement_test.reset()[0]

        while not finish:
            action = agent.play(observation)
            observation, reward, finish, truncated, info = environement_test.step(action)

    environement_test.close()