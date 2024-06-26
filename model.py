import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size): # size of the different layers
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x)) # applying ReLU to intorduce non-linearity allowing model to understand complex patterns
        x = self.linear2(x)
        return x
    
    def save(self, file_name='model.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr # amount the paramters are changed during training
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr) # adjusts the models paramteres to reduce error
        self.criterion = nn.MSELoss() # calculuates the erorr

    def train_step(self, state, action, reward, next_state, done):

        # reformats inputs into tensors so NN can process them
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)

        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )

        # 1: get predicted Q values for current state
        pred = self.model(state) # models predicted value
        target = pred.clone() # copy to adjust depending on actual outcome
        
        # 2:Q_new = r + y * max(next_predicted Q value) -> only do if hasn't been done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        for index in range(len(done)):
            Q_new = reward[index]
            if not done[index]:
                Q_new = reward[index] + self.gamma * torch.max(self.model(next_state[index]))
            
            target[index][torch.argmax(action).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()

        # Training Step Method Summary

        # 1. Convert inputs to tensors so NN can process them
        # 2. Model predicts the current state
        # 3. Adjust the predictions based on the actual outcome
        # 4. Computer loss between actual and predicted values
        # 5. Backpropogation to update models weights and reduce error