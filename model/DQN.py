from torch import nn


class DQN(nn.Module):

    def __init__(self, n_observation: int, n_actions: int):

        super().__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(n_observation, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, n_actions),
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits
