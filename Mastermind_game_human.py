import random
build = True #Don't touch this!

def list_sort(ls_input_list):

	def zip(z_list1, z_list2):
		zip_res = []
		i = 0
		j = 0
		while (i < len(z_list1)) and (j < len(z_list2)):
			if (z_list1[i] < z_list2[j]):
				zip_res.append(z_list1[i])
				i += 1
			else:
				zip_res.append(z_list2[j])
				j += 1
		if (i < len(z_list1)):
			zip_res.extend(z_list1[i:])
		if (j < len(z_list2)):
			zip_res.extend(z_list2[j:])

		return zip_res

	lenn = len(ls_input_list)
	if (lenn < 2):
		return ls_input_list
	else:
		return zip((list_sort(ls_input_list[:(lenn // 2)])), (list_sort(ls_input_list[(lenn // 2):])))

def how_many_common(hmc_sorted_input_list1, hmc_sorted_input_list2):
	#assuming that both lists are sorted in non-decreasing order
	temp = []
	if (len(hmc_sorted_input_list2) > len(hmc_sorted_input_list1)):
		temp = hmc_sorted_input_list1
		hmc_sorted_input_list1 = hmc_sorted_input_list2
		hmc_sorted_input_list1 = temp
	#From now on, hmcsil1 is definately smaller in size
	res = 0
	i = 0
	j = 0
	while (i < len(hmc_sorted_input_list1)) and (j < len(hmc_sorted_input_list2)):
		if (hmc_sorted_input_list1[i] < hmc_sorted_input_list2[j]):
			i += 1
		elif (hmc_sorted_input_list1[i] > hmc_sorted_input_list2[j]):
			j += 1
		else:
			res += 1
			i += 1
			j += 1
	return res

def how_many_right(hmr_unsorted_input_list1, hmr_unsorted_input_list2):
	res = 0
	for i in range(0, len(hmr_unsorted_input_list1)):
		if (i >= len(hmr_unsorted_input_list2)):
			break
		if (hmr_unsorted_input_list2[i] == hmr_unsorted_input_list1[i]):
			res += 1

	return res

def judge(judge_input_list):
	print "\n///////////////////////////////////////////////////////////"
	print "judge input list:\t", judge_input_list
	number_of_reds = int(raw_input("Enter number of reds:"))
	total_balls = int(raw_input("Enter total number of balls:"))
	return (number_of_reds, total_balls)

def rm_duplicates(lst): #sahi hai ye
	i = 0
	while i < len(lst):
		val = lst[i]
		replaced = False
		if lst.count(val) > 1:
			replaced = True
		while lst.count(val) > 1:
			lst.remove(val)
		if replaced:
			i -= 1	#as we want i unchanged
		i += 1
	return lst


def permute_list(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
 
    l = []
 
    for i in range(len(lst)):
       m = lst[i]

       remLst = lst[:i] + lst[i+1:]

       for p in permute_list(remLst):
           l.append(p + [m])
    return rm_duplicates(l)

skip = False
def main():
	trials = [] #a possible element of trial: [[1, 2, 6, 4], (num_of_red, tot)]
	
	def play(a, b, c, d):
		inp_to_judge = [a, b, c, d]
		return play2(inp_to_judge)

	def play2(inp_to_judge):
		out_from_judge = judge(inp_to_judge)
		trials.append([inp_to_judge, out_from_judge])
		return out_from_judge

	def homework():
		global skip
		tmp_cnt = play(1, 1, 2, 3)
		if tmp_cnt[1] == 0 or tmp_cnt[1] == 4:
			skip = True

		# if not skip:
		# 	play(4, 5, 6, 7)
		return

	sorted_candidates = []

	def build_sorted_candidates():
		bsc_output = []
		for i1 in range(1, 9):
			for i2 in range(i1, 9):
				for i3 in range(i2, 9):
					for i4 in range(i3, 9):
						temp = [i1, i2, i3, i4]
						psaa = True
						for t in trials:
							kye = list_sort(t[0])
							hmc = how_many_common(kye, temp)
							if hmc != t[1][1]:
								# if (temp == sorted_correct_answer):
								# 	print "\treached here!"
								# 	print "trials:"
								# 	print trials
								# 	print "t:\t", t
								#print "\treached here!"
								psaa = False
								break
						if psaa:
							#print "reached here!"
							bsc_output.append(temp)

		del(sorted_candidates[:])
		sorted_candidates.extend(bsc_output)
		return

	def build_sorted_candidates2():
		bsc_output = []
		for i in ([i1, i2, i3, i4] for i1 in range(1, 9) for i2 in range(i1, 9) for i3 in range(i2, 9) for i4 in range(i3, 9)):
			psaa = True
			for t in trials:
				kye = list_sort(t[0])
				hmc = how_many_common(kye, i)
				if hmc != t[1][1]:
					psaa = False
					break

			if psaa:
				bsc_output.append(i)

		del(sorted_candidates[:])
		sorted_candidates.extend(bsc_output)
		return

	def sorted_filter(sf_input_list):
		psaa = True
		for t in trials:
			kye = list_sort(t[0])
			hmc = how_many_common(kye, sf_input_list)
			if hmc != t[1][1]:
				# if sf_input_list == sorted_correct_answer:
				# 	print "locha:(\tsf_input_list:\t", sf_input_list
				# 	print "t:\t", t
				# 	print "trials:\t", trials
				psaa = False
				break

		return psaa

	def filter_sorted_candidates():
		sorted_candidates_temp = filter(sorted_filter, sorted_candidates)
		del(sorted_candidates[:])
		sorted_candidates.extend(sorted_candidates_temp)
		return

	unsorted_candidates = [] #one example member: [[1, 2, 3, 4], [[1, 2, 4, 3], [1, 2, 3, 4], [1, 3, 2, 4]]]
#					[[1st list is sorted], [list of possible unsorted lists(need not be all permutations)]]

	def build_unsorted_candidates_based_on_sorted_one():
		for i in sorted_candidates:
			unsorted_candidates.append([i, permute_list(i)]) #uc = unsorted candidate
		return

	def filter_unsorted_candidates_based_on_sorted_one():
		list_of_indices = []
		#I will go through each elem in unsorted_candidates to see:
		#1->which ones are not in sorted_candidates
		#2->which ones' permutation list is empty
		#in case #2, I will remove those elem from both sorted and unsorted lists

		for i in range(0, len(unsorted_candidates)):
			unsorted_elem = unsorted_candidates[i][0]
			if (sorted_candidates.count(unsorted_elem) < 1):
				list_of_indices.append(i)
			elif (len(unsorted_candidates[i][1]) < 1):
				list_of_indices.append(i)
				# if elem == sorted_correct_answer:
				# 	print "locha hai:(\telem:\t", elem
				# 	print "unsorted candidate:"
				# 	print unsorted_candidates[i]
				sorted_candidates.remove(elem)

		for i in reversed(list_of_indices):
			unsorted_candidates.pop(i)

		return

	def filter_unsorted_candidates_based_on_testing():
		list_of_indices = [] #one possible elem: [2, [4, 6, 9]]

		#building list_of_indices
		for i in range(0, len(unsorted_candidates)):
			temp = []
			temp_right = []
			for j in range(0, len(unsorted_candidates[i][1])):
				for trial in trials:
					trial_list = trial[0]
					hmr = how_many_right(trial_list, unsorted_candidates[i][1][j])
					if (hmr != trial[1][0]):
						# if(unsorted_candidates[i][0] == sorted_correct_answer):
						# 	if unsorted_candidates[i][1][j] == correct_answer:
						# 		print "\n\n-----------------------------------------------------"
						# 		print "super llocha:(\t"
						# 		print "\nunsorted candidate:"
						# 		print unsorted_candidates[i]
						# 		print "trial:\t", trial
						# 		print "trials:"
						# 		print trials
						# 		print "-----------------------------------------------------\n\n"

						temp_right.append(j)
						break
			if (len(temp_right) > 0):
				temp = [i, temp_right]
				list_of_indices.append(temp)


		list_of_indices.reverse()
		for i in range(0, len(list_of_indices)):
			list_of_indices[i][1].reverse()

		for elem in list_of_indices:
			indx = elem[0]
			inner_remove_list = elem[1]
			#doom = False
			#if(unsorted_candidates[indx][0] == sorted_correct_answer):
				# print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
				# print "Before removal:"
				# print unsorted_candidates[indx]

			if (len(inner_remove_list) >= len(unsorted_candidates[indx][1])):
				# if (unsorted_candidates[indx][0] == sorted_correct_answer):
				# 	doom = True


				if (sorted_candidates.count(unsorted_candidates[indx][0]) > 0):
					sorted_candidates.remove(unsorted_candidates[indx][0])
				unsorted_candidates.pop(indx)
				continue

			for j in inner_remove_list:
				unsorted_candidates[indx][1].pop(j)
			#if (not doom) and (unsorted_candidates[indx][0] == sorted_correct_answer):
				# print "After removal: "
				# print unsorted_candidates[indx]

		return

	def choose_candidate(cc_mode):
		freq_list = []	#It will store the frequency of elements in sorted_candidates
						#w.r.t the no. of their corr. permutations

		keys_of_unsorted_candidates = []	#it will have elem of: unsorted_candidates[i][1]
						#this will help me to find the indices of corresponding lists in sorted_candidates

		for i in range(0, len(unsorted_candidates)):
			keys_of_unsorted_candidates.append(unsorted_candidates[i][0])

		for elem in sorted_candidates:
			i = keys_of_unsorted_candidates.index(elem)
			freq_list.append(len(unsorted_candidates[i][1]))

		def give_max_min_median(gmmm_mode):
			srtd = freq_list
			# print freq_list
			srtd.sort()
			val = 0
			if (gmmm_mode > 0): 	#max
				val = srtd[len(srtd)-1]
			elif (gmmm_mode < 0):	#min
				val = srtd[0]
			else:					#median
				val = srtd[len(srtd) // 2]

			start_index = 0
			end_index = len(srtd) - 1
			if (gmmm_mode > 0):
				start_index = srtd.index(val)
			elif (gmmm_mode < 0):
				end_index = len(srtd) - 1 - srtd[::-1].index(val)
			else:
				start_index = srtd.index(val)
				end_index = len(srtd) - 1 - srtd[::-1].index(val)

			count = random.randrange(0, end_index - start_index + 1)

			pos = freq_list.index(val)
			k = pos + 1
			while (count > 0) and k < len(freq_list):
				if freq_list[k] == val:
					pos = k
					count -= 1
				k += 1

			return pos

		outer_index = give_max_min_median(cc_mode)
		inner_index = random.randrange(0, len(unsorted_candidates[outer_index][1]))

		return unsorted_candidates[outer_index][1][inner_index]

	def cmd_interface():
		#cmd = raw_input("Enter command:")
		cmd = "start"
		if cmd == "help":
			print("This help")
		elif cmd == "start":

			skip = False
			homework()
			build_sorted_candidates()
			# print sorted_candidates
			build_unsorted_candidates_based_on_sorted_one()
			# print "\n\n*******************************************************\n"
			# print "Correct Answer:"
			# print correct_answer
			# print sorted_correct_answer
			# print "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
			# print sorted_candidates
			while (True):
				candi = choose_candidate(1)
				# print "candi choosen:\t", candi
				play2(candi)
				filter_sorted_candidates()
				# cmmd = raw_input("Print sorted list(1)?(Y?)")
				# if cmmd == "Y" or cmmd == "y":
				# 	print sorted_candidates
				# 	print "--------------------------------------------------------\n\n"
				filter_unsorted_candidates_based_on_sorted_one()
				filter_unsorted_candidates_based_on_testing()
				if(len(sorted_candidates) == 1):
					if(len(unsorted_candidates) > 1):
						filter_unsorted_candidates_based_on_sorted_one()
					if(len(unsorted_candidates[0][1]) == 1):
						print "I found out this:"
						for i in unsorted_candidates[0][1][0]:
							print i,

						# print "\nThe correct answer is:"
						# for i in correct_answer:
						# 	print i, 

						break

				# cmmd = raw_input("Print sorted list(2)?(Y?)")
				# if cmmd == "Y" or cmmd == "y":
				# 	print sorted_candidates
				# 	print "--------------------------------------------------------\n\n"


				# cmmd = raw_input("Print unsorted List?(Y?)")
				# if cmmd == "Y" or cmmd == "y":
				# 	print unsorted_candidates
				# 	print "--------------------------------------------------------\n\n"
				# cmmd = raw_input("Print correct_answer?")
				# if cmmd == "Y" or cmmd == "y":
				# 	print "correct_answer:"
				# 	print correct_answer
		return

	cmd_interface()
	return

main()