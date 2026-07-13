# Gymnasium Solutions

## Repository Objective

This repository contains my own reinforcement learning implementations using Gymnasium.

The goal is to put the concepts I study into practice by developing my own algorithms and solutions for different environments.

## About Gymnasium

Gymnasium is a Python library used to create and test reinforcement learning environments.

It allows an agent to interact with an environment by taking actions, observing the results of those actions, and receiving rewards.

Gymnasium provides several ready-to-use environments, such as `FrozenLake`, `Taxi`, `Blackjack`, `CartPole`, and `MountainCar`.

For more information, see the [official Gymnasium documentation](https://gymnasium.farama.org/).

## Project Structure

```text
gymnasium-solutions/
│
├── Environment/
│   ├── Box2D/
│   ├── Classic Control/
│   ├── MuJoCo/
│   └── Toy_Text/
│       ├── blackjack.py
│       ├── ...
│       └── template_toy_text.py
│
├── Models/
│   ├── player.py
│   └── Reinforcement_Learning/
│       └── q_learning.py
│
├── .gitignore
└── README.md
```

* `Environment` contains the implementations for the different Gymnasium environments.
* Each environment category contains a dedicated template that can be used as a starting point to quickly implement new environments within that category.
* `Models` contains the reinforcement learning algorithms and reusable components used by the environments.

## Running an Environment

An environment can be launched as a Python module from the root directory of the project.

For example, to run `FrozenLake`:

```bash
python3 -m Environment.Toy_Text.frozen_lake
```

Other examples:

```bash
python3 -m Environment.Toy_Text.blackjack
python3 -m Environment.Toy_Text.cliff_walking
python3 -m Environment.Toy_Text.taxi
```

The command follows the package structure:

```text
python3 -m Environment.<category>.<python_file>
```

The command must be executed from the root directory of the project.
