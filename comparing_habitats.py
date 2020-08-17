from species_richness import get_species_richness
from species_evenness import get_species_evenness


def compare_diversity(observed_list, diversity_measure):
    '''Return a list of tuples consisting of habitat from `observed_list` and
    diversity from `diversity_measure`, sorted from most diverse to least
    diverse habitat and alphabetically in the case of the same diversity'''

    # create list of habitats (without repetition)
    habitat_list = []
    for entry in observed_list:
        if entry[1] not in habitat_list:
            habitat_list.append(entry[1])

    # create list of tuples as (habitat, diversity)
    output_list = []
    for hab in habitat_list:

        # create list of species with repetition
        species_list = []
        for entry in observed_list:
            if entry[1] == hab:
                species_list.append(entry[0])

        # use `species_list` to compute habitat's diversity specified in
        # `diversity_measure`
        if diversity_measure == "richness":
            div = get_species_richness(species_list)[0]
        else:
            div = get_species_evenness(species_list)[0]

        # add tuple (habitat, diversity) to `ouput_list`
        output_list.append((hab, div))

    # sort `output_list` alphabetically, then in descending order of diversity
    alph_list = sorted(output_list)
    sorted_list = sorted(alph_list, key=lambda x: x[1], reverse=True)

    return sorted_list


