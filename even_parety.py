import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_parity_generator_circuit():
    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Hide axes
    ax.axis('off')

    # Define positions for inputs and output
    input_positions = [(1, 4), (1, 3), (1, 2)]  # A2, A1, A0
    output_position = (4, 3)  # Parity Bit P
    xor1_position = (2, 4)  # First XOR gate
    xor2_position = (3, 3)  # Second XOR gate
    not_position = (4, 2)  # NOT gate
    
    # Draw inputs
    for i, pos in enumerate(input_positions):
        ax.text(pos[0], pos[1], f'A{i+2}', fontsize=12, ha='center')
        ax.add_patch(patches.Circle((pos[0]-0.1, pos[1]), 0.1, color='black'))
    
    # Draw first XOR gate
    ax.text(xor1_position[0], xor1_position[1] + 0.1, 'XOR', fontsize=12, ha='center', bbox=dict(facecolor='lightgray', edgecolor='black'))
    ax.add_patch(patches.Rectangle((xor1_position[0]-0.2, xor1_position[1]-0.15), 0.4, 0.3, edgecolor='black', facecolor='lightgray'))

    # Draw second XOR gate
    ax.text(xor2_position[0], xor2_position[1] + 0.1, 'XOR', fontsize=12, ha='center', bbox=dict(facecolor='lightgray', edgecolor='black'))
    ax.add_patch(patches.Rectangle((xor2_position[0]-0.2, xor2_position[1]-0.15), 0.4, 0.3, edgecolor='black', facecolor='lightgray'))

    # Draw NOT gate
    ax.text(not_position[0], not_position[1] + 0.1, 'NOT', fontsize=12, ha='center', bbox=dict(facecolor='lightgray', edgecolor='black'))
    ax.add_patch(patches.Rectangle((not_position[0]-0.2, not_position[1]-0.15), 0.4, 0.3, edgecolor='black', facecolor='lightgray'))

    # Draw output
    ax.text(output_position[0], output_position[1], 'P', fontsize=12, ha='center')
    ax.add_patch(patches.Circle((output_position[0]+0.1, output_position[1]), 0.1, color='black'))

    # Draw connections
    # A2 to XOR1
    ax.plot([1-0.1, xor1_position[0]-0.2], [4, 4], color='black')
    ax.plot([1-0.1, xor1_position[0]-0.2], [3.5, 3.5], color='black')

    # A1 to XOR1
    ax.plot([1-0.1, xor1_position[0]-0.2], [3, 3], color='black')

    # XOR1 to XOR2
    ax.plot([xor1_position[0]+0.2, xor2_position[0]-0.2], [4, 3.5], color='black')
    
    # A0 to XOR2
    ax.plot([1-0.1, xor2_position[0]-0.2], [2, 3], color='black')

    # XOR2 to NOT
    ax.plot([xor2_position[0]+0.2, not_position[0]-0.2], [3, 2.5], color='black')

    # NOT to output
    ax.plot([not_position[0]+0.2, output_position[0]-0.1], [2.5, 3], color='black')

    # Show the circuit
    plt.title("3-Bit Even Parity Generator Circuit", fontsize=14)
    plt.show()

draw_parity_generator_circuit()
