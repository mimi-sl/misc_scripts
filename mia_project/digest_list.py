# where digest is the base32 version, old_list is old list

#values for testing
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digest = 8

# part that's relevant to you
new_list = []

for i in range(0, len(old_list)):
	if i == (len(old_list) - 1) and old_list[i] < digest:
		new_list.extend([old_list[0], old_list[1], old_list[2], old_list[3]])

	else:
		if old_list[i] >= digest:
			new_list.extend([old_list[i % len(old_list)], old_list[(i + 1) % \
				len(old_list)], old_list[(i + 2) % len(old_list)], \
				old_list[(i + 3) % len(old_list)]])

			break

print new_list