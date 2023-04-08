class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):

        is_monster = {'size': set(), 'color': set(), 'covering': set(), 'foot-type': set(), 'leg-count': set(), 'arm-count': set(), 'eye-count': set(), 'horn-count': set(), 'lays-eggs': set(), 'has-wings': set(), 'has-gills': set(), 'has-tail': set()}
        not_monster = {'size': set(), 'color': set(), 'covering': set(), 'foot-type': set(), 'leg-count': set(), 'arm-count': set(), 'eye-count': set(), 'horn-count': set(), 'lays-eggs': set(), 'has-wings': set(), 'has-gills': set(), 'has-tail': set()}
        can_be_monster = {'size': set(), 'color': set(), 'covering': set(), 'foot-type': set(), 'leg-count': set(), 'arm-count': set(), 'eye-count': set(), 'horn-count': set(), 'lays-eggs': set(), 'has-wings': set(), 'has-gills': set(), 'has-tail': set()}

        for monster, positive_classification in samples:
            if positive_classification:
                for key, value in monster.items():
                    # if we haven't classified this value yet, put it in is_monster
                    if not (value in is_monster[key]) and not (value in not_monster[key]) and not (value in can_be_monster[key]):
                        is_monster[key].add(value)
                    # if this value was classified as not a monster, then we remove it from there, due to this case, and move it to can_be
                    elif value in not_monster[key]:
                        not_monster[key].remove(value)
                        can_be_monster[key].add(value)
            else:
                for key, value in monster.items():
                    #if we haven't classified this value yet, put it in not_monster
                    if not (value in is_monster[key]) and not (value in not_monster[key]) and not (value in can_be_monster[key]):
                        not_monster[key].add(value)
                        # if this value was classified as a monster, then we remove it from there, due to this case, and move it to can_be
                    elif value in is_monster[key]:
                        is_monster[key].remove(value)
                        can_be_monster[key].add(value)


        is_this_type_of_monster = True

        # we loop through the values for the new monster and say no if we find any values that we have obvious evidence that it is not a monster
        # if we have not seen the value for not_monster, we assume it is a monster
        for key, value in new_monster.items():
            invalid_values = not_monster[key]
            is_this_type_of_monster = is_this_type_of_monster and (not value in invalid_values)

        return is_this_type_of_monster
