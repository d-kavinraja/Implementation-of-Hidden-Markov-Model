import numpy as np
#Define the transition matrix
transition_matrix =np.array([[0.7,0.3],[0.4,0.6]])
#Define the emission matrix
emission_matrix =np.array ([[0.1,0.9],[0.8,0.2]])
#Define the initial probabilities
initial_probabilities = np.array([0.5,0.5])
#Define the observed sequence
observed_sequence = np.array([0,1,0,0,0,0])

# Initialize the alpha matrix
alpha = np. zeros ((len(observed_sequence) ,len (initial_probabilities) ) )
# Calculate the first row of the alpha matrix
alpha [0,:] = initial_probabilities *emission_matrix[:, observed_sequence [0]]

# Loop through the rest of the observed sequence and calculate the rest of the alpha matrix
for t in range (1, len (observed_sequence) ) :
  for j in range (len (initial_probabilities) ) :
    alpha[t,j]= emission_matrix [j,observed_sequence[t]] *np.sum(alpha[t-1:]*transition_matrix[:, j])
    
# Calculate the probability of the observed sequence
probability = np.sum(alpha[-1,:])
# Print the probability of the observed sequence
print ("The probability of the observed sequence is: " ,probability)
# Find the most likely sequence of weather states given the observed sequence
most_likely_sequence=[]
for t in range (len (observed_sequence)):
  if alpha [t, 0] > alpha [t,1]:
    most_likely_sequence.append ("sunny")
  else:
    most_likely_sequence.append ("rainy")
    
print("The most likely sequence of Weather States is",most_likely_sequence)