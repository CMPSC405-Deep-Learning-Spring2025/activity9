# Activity 9
## Due: 9am on February 19, 2025

## Objectives
- Learn about weight initialization methods in neural networks
- Understand different initialization strategies for different layers
- Compare Xavier and Kaiming (He) initialization methods

## Tasks
1. Observe default PyTorch weight initialization
2. Implement Xavier initialization for all linear layers
3. Create a custom initialization scheme:
   - Xavier initialization for the first layer
   - Kaiming (He) initialization for the second layer

## Initialization Methods
- **Default:** PyTorch's built-in initialization
- **Xavier/Glorot:** Suitable for layers with symmetric activation functions
- **Kaiming/He:** Optimized for ReLU activation functions

## Run the Program
- Execute `initialization.py` to see the different initialization results

## Observations
TODO: 
1. Compare the weight distributions from different initialization methods
2. Explain why different layers might benefit from different initialization strategies
