import numpy as np

# System matrices
Q = np.diag([100, 100, 1, 1])
R = np.array([[10]])
A = np.array([[0, 1, 0, 0], [0, 0, -0.245, 0], [0, 0, 0, 1], [0, 0, 20.09, 0]])
B = np.array([[0], [0.05], [0], [-0.1]])

# Random policy
policy = np.random.uniform(-1, 1, (A.shape[0], 1))
print("Random policy:\n", policy)

# Solve the algebraic Riccati equation
P = np.matrix(np.zeros((A.shape[0], A.shape[0])))
while True:
    Pnew = Q + A.T @ P @ A - A.T @ P @ B @ np.linalg.inv(R + B.T @ P @ B) @ B.T @ P @ A
    if np.allclose(P, Pnew):
        break
    P = Pnew

# Compute the optimal value function
V = np.zeros((A.shape[0], 1))
for i in range(100):
    V = Q + A.T @ P @ V

print(F"Optimal value function:\n{V}")
