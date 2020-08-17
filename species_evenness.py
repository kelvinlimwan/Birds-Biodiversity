def get_species_evenness(observed_list):
    '''Return species evenness and alphabetically sorted list of tuples
    consisting of bird species in `observed_list` and the number of times each
    species were observed'''

    # in case of empty `observed_list`
    if not observed_list:
        return (0, [])

    species_list = []  # list of species, without repetition
    tuple_list = []  # list of tuples as (species, number of observations)
    propsquared_list = []  # list of proportions squared for each species

    # for each species not already listed
    for bird in observed_list:
        if bird not in species_list:
            # add species to 'species_list'
            species_list.append(bird)

            # count the number of times species was observed and add its
            # tuple (species, number of observations) to `tuple_list`
            count = observed_list.count(bird)
            tuple_list.append((bird, count))

            # compute species' proportion squared and add to `propsquared_list`
            prop2 = (count / len(observed_list)) ** 2
            propsquared_list.append(prop2)

    # compute species evenness
    evenness = 1 / sum(propsquared_list)

    # sort `tuple_list` alphabetically
    alph_list = sorted(tuple_list)

    return (evenness, alph_list)
