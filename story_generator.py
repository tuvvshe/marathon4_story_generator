import random
when = ['YESTERDAY', 'LONG LONG LONG TIME AGO', 'IN DIFFERENT TIME']
who = ['CHICKEN', 'CAT', 'HORSE', 'MAN', 'WOMAN']
name = ['AMAR', 'AMOUR', 'BEN', 'BONNY', 'DENNIS', 'DENDEW']
residence = ['HOME', 'TREE', 'MIRROR', 'GARAGE', 'DORM']
went = ['BAR', 'CLUB', 'SEMINAR', 'RANCH']
happened = ['FOUND GOLD', 'FOUND SILVER']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))