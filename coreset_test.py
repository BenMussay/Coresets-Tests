from typing import Callable, List
from time import sleep

import torch
from torch import optim
from tqdm import tqdm


class CoresetTest:
    def __init__(self,
                 points: torch.tensor,
                 weights: torch.tensor,
                 loss: Callable,
                 queries_shape: List[int],
                 additive_error: bool = False,
                 num_epochs: int = 100,
                 learning_rate: float = 1e-3):
        self.__points = points
        self.__weights = weights
        self.__loss = loss
        self.__queries_shape = queries_shape
        self.__additive_error = additive_error
        self.__num_epochs = num_epochs
        self.__learning_rate = learning_rate

    def forward(self, coreset: torch.tensor, coreset_weights: torch.tensor):
        x = torch.randn(self.__queries_shape, requires_grad=True)

        optimizer = optim.Adam([x], lr=self.__learning_rate)

        sleep(1)
        for _ in tqdm(range(self.__num_epochs)):
            optimizer.zero_grad()  # zero the gradient buffers
            loss_p = self.__loss(points=self.__points, weights=self.__weights, query=x)
            loss_c = self.__loss(points=coreset, weights=coreset_weights, query=x)
            error = - abs(loss_p - loss_c)

            if not self.__additive_error:
                error /= loss_p
            error.backward()
            optimizer.step()
        sleep(1)

        loss_p = self.__loss(points=self.__points, weights=self.__weights, query=x)
        loss_c = self.__loss(points=coreset, weights=coreset_weights, query=x)

        error = abs(loss_p - loss_c)
        if not self.__additive_error:
            error /= loss_p

        return error.tolist()
