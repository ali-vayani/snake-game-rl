# Snake RL Agent

This project implements an AI agent to play the classic Snake game using Reinforcement Learning (RL). The agent is trained using Q-learning and a neural network to maximize its score by learning the optimal actions through interactions with the game environment.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Results](#results)

## Features
- Implements the classic Snake game using Pygame.
- Uses Q-learning with a neural network for the AI agent.
- Includes training scripts and visualizations of the training process.

## How It Works
1. **Game Environment**: The Snake game is implemented using Pygame.
2. **Agent**: An agent interacts with the game environment to learn the optimal actions.
3. **Model**: A simple neural network with one hidden layer is used to predict Q-values for state-action pairs.
4. **Training**: The agent is trained using Q-learning, where it learns from the rewards obtained by playing the game.
5. **Evaluation**: The trained agent can play the game and maximize its score by making optimal decisions.

### Neural Network Architecture
- Input Layer: Represents the current state of the game.
- Hidden Layer: Processes the input state.
- Output Layer: Outputs Q-values for possible actions (left, right, straight).

### Training Process
- The agent starts with random actions to explore the game environment.
- Over time, it learns to take actions that maximize cumulative rewards.
- The Q-learning algorithm is used to update the neural network based on the rewards received.

## Results
- The agent learns to play the Snake game and can achieve high scores by learning from its experiences.
- Training progress and scores are visualized using matplotlib.


