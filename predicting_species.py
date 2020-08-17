def infer_bird_species(environment, observations, region_list):
    # create a list of species without repetition
    species_list = []
    for row in observations:
        for region in row:
            for bird in region:
                if bird not in species_list:
                    species_list.append(bird)

    # for each species, identify which environmental factors are present
    # in all of the regions in which it was observed and create list of tuples
    # as (species, factors)
    species_factors_list = []
    only_factors_list = []
    for species in species_list:
        factors_list = [1] * len(environment[0][0])
        for row in observations:
            index_row = observations.index(row)
            for region in row:
                index_region = row.index(region)
                if species in region:
                    j = 0
                    for i in environment[index_row][index_region]:
                        if i == 0 and factors_list[j] == 1:
                            factors_list[j] = 0
                        j += 1
        species_factors_list.append((species, factors_list))
        only_factors_list.append(factors_list)

    # for each unsampled region, extract corresponding environmental factors
    # and predict which species are expected to be observed there
    predicted_list = []
    for tup in region_list:
        pred = []
        index_row = tup[0]
        index_region = tup[1]
        for index in range(len(only_factors_list)):
            count = 0
            j = 0
            for i in environment[index_row][index_region]:
                if i == 1 and only_factors_list[index][j] == 1:
                    count += 1
                j += 1
            if count == only_factors_list[index].count(1):
                pred.append(species_factors_list[index][0])
        predicted_list.append(sorted(pred))

    return predicted_list



