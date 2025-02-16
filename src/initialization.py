# Default initialization
linear = nn.Linear(5, 3)
print(linear.weight)

# Custom Initialization
def init_xavier_weights(m):
    # Uses Xavier initialization for linear layers
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        nn.init.zeros_(m.bias)

model.apply(init_xavier_weights)

# TODO: complete the function below that uses Xavier for the first layer and Kaiming(He) for the second
def init_two_layer_weights():

# model.apply(init_two_layer_weights())

# TODO: Uncomment 'model.apply(init_two_layer_weights())' for two-layer models