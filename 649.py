collection = get_inital_state()
state_var = None
for datum in data_set:
    if condition(state_var):
        state_var = calculate_from(datum)
        new = modify(datum,state_var)
        collection.add_to(new)
    else:
        new = modify_differently(datum)
        collection.add_to(new)


for thing in collection:
    process(thing)
