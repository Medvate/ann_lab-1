EXP = 2.7182818284959045

main_results = (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0)

coef_of_education = 0.3
w_0 = 1
w_i = [0, 0, 0, 0]


def num_to_bin(num):
    num_bin = bin(num)[2:]
    zeros = '0000'
    return zeros[0:4 - len(num_bin)] + num_bin


def get_net(x_i):
    net = w_0

    for x, w in zip(x_i, w_i):
        net += int(x) * w

    return net


def F_from_net(net):
    return 1 / (1 + EXP ** (-net))


# START
for epoch in range(20000):
    F = []
    
    for i in range(16):
        x_i = num_to_bin(i)
        net = get_net(x_i)
        result = F_from_net(net)
    
        mistake_on_neuron = main_results[i] - result
    
        w_0 += coef_of_education * mistake_on_neuron * (result * (1 - result))
    
        for index, x in enumerate(x_i):
            w_i[index] += coef_of_education * mistake_on_neuron * (result * (1 - result)) * int(x)
    
        if result >= 0.5:
            F.append(1)
        else:
            F.append(0)

    k = 0
    for i, j in zip(main_results, F):
        if i != j:
            k += 1
    
    if k == 0:
        print("k =", k)
        print("epoch =", epoch)
        break
    
    print("k =", k)
    
print("w_i =", w_i)
print("  F =", F)
