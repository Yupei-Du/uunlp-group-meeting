import random
from collections import defaultdict, Counter


PRESENT_TIMES = {'frequent': 2, 'non-frequent': 1}
NAMES = {
    'frequent': ['eduardo', 'danill', 'lukas', 'yingjin', 'hugh mee', 'anna'], 
    # Yupei has presented once
    'non-frequent': ['yupei', 'fafa', 'kees', 'albert', 'massimo', 'marijn', 'gerard', 'guanyi']
    }


def capitalize(name):
    name = [name] if len(name.split(' ')) == 1 else name.split(' ')
    name = [word[0].upper() + word[1:] for word in name]
    return ' '.join(name)


def main():
    random.seed(42)  # The answer to the ultimate question of life, the universe and everything

    # Generating in-group order
    present_order_indices_dict = defaultdict(list)
    for group in NAMES:
        for _ in range(PRESENT_TIMES[group]):
            present_order_indices = list(range(len(NAMES[group])))
            random.shuffle(present_order_indices)
            present_order_indices_dict[group] += present_order_indices
    
    # Sample names
    present_order = []
    num_remain_dict = {group: len(present_order_indices_dict[group]) 
                       for group in present_order_indices_dict}
    num_presences = sum(num_remain_dict.values())
    while len(present_order) < num_presences:
        sampled_group = random.sample(
            list(NAMES.keys()), counts=[num_remain_dict[group] for group in NAMES], k=1)[0]
        sampled_order_idx = num_remain_dict[sampled_group] - 1
        sampled_order = present_order_indices_dict[sampled_group][sampled_order_idx]
        sampled_name = NAMES[sampled_group][sampled_order]
        present_order.append(sampled_name)
        num_remain_dict[sampled_group] -= 1
    
    # verify
    present_counter = Counter(present_order)
    for group in NAMES:
        for name in NAMES[group]:
            assert present_counter[name] == PRESENT_TIMES[group]
    print('Successfully generated present order') 

    present_order = [capitalize(name) for name in present_order]
    print('\n'.join(present_order))
    

if __name__ == '__main__':
    main()




