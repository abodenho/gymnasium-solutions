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
│   ├── Classic_Control/
│   ├── MuJoCo/
│   └── Toy_Text/
│       ├── template_toy_text.py
│       └── Frozen_Lake/
│           ├── frozen_lake.py
│           └── README.md
│
├── Models/
│   └── Reinforcement_Learning/
│       └── Q_learning.py
│
├── .gitignore
└── README.md
```

* `Environment` contains the implementations for the different Gymnasium environments.
* Each environment category contains a dedicated template that can be used as a starting point to quickly implement new environments within that category.
* `Models` contains the reinforcement learning algorithms used by these environments.
