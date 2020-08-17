def optimise_study(sample_data, unseen_species, consecutive_visits):
    '''Return number of visits that occur before the study stops- when number
    of consecutive unproductive visits (visits with lower number of previously
    unseen bird species than `unseen_species`) reaches `consecutive_visits` and
    proportion of total bird species observed at that point compared to if all
    visits were conducted'''

    # create list of species (without repetition) if all visits were conducted
    full_list = []
    for visit in sample_data:
        for bird in visit:
            if bird not in full_list:
                full_list.append(bird)

    stopped_list = []  # list of species until study stops (without repetition)
    visits = 0  # number of visits until study stops
    unprod = 0  # number of consecutive unproductive visits

    # compute number of visits until study stops and add species to
    # 'stopped_list'
    for study in sample_data:

        # check if number of consecutive unproductive visits has reached
        # `consecutive_visits`; if so, break loop
        if unprod == consecutive_visits:
            break

        else:
            if study == sample_data[0]:
                visits += 1
            unseen = 0  # number of previously unseen species

            # add each previously unseen species to `stopped_list` and add its
            # total count to `unseen`
            for bird in study:
                if bird not in stopped_list:
                    stopped_list.append(bird)
                    unseen += 1

                    # check if visit is unproductive; if so add 1 to `prod`, if not
            # set `unprod` to 0
            if unseen < unseen_species:
                unprod += 1
            else:
                unprod = 0

    # proportion of total species observed until study stops to that if all
    # visits have been conducted
    prop = len(stopped_list) / len(full_list)

    return (visits, prop)