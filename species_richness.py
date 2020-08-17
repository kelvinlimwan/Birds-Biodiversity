def get_species_richness(observed_list):
    '''Return species richness and alphabetically sorted list of bird species
    in `observed_list`'''

    # create list of species (without repetition)
    species_list = []
    for bird in observed_list:
        if bird not in species_list:
            species_list.append(bird)

    # compute species richness
    richness = len(species_list)

    # sort `species_list` alphabetically
    alph_list = sorted(species_list)

    return (richness, alph_list)