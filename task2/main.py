from generate_noise_trajectory import generate_noise_trajectory
from connect_nonredundant_similar_state import connect_similar_state
from measure_degree_distribution import measure_degree_distribution


def main():
    # takes random number of nodes
    node_number = int(input("Enter the number of nodes: "))

    # takes random average degree
    degree_k = int(input("Enter the average degree k: "))

    # generate noise trajectory
    noise_trajectory = generate_noise_trajectory(node_number, degree_k)

    # connect similar state in the noise trajectory
    connection = connect_similar_state(noise_trajectory)

    # measure degree distribution of noise trajectory
    measure_degree_distribution(connection)


if __name__ == "__main__":
    main()
