size = int(input("Enter the size of the queue: "))
disk_size = int(input("Enter the disk size: "))

# Function to perform C-LOOK on the request
# array starting from the given head
def CLOOK(arr, head):
	
	seek_count = 0
	distance = 0
	cur_track = 0

	left = []
	right = []

	seek_sequence = []

	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beginning (left end)
	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	# Sorting left and right vectors
	left.sort()
	right.sort()

	# First service the requests
	# on the right side of the
	# head
	for i in range(len(right)):
		cur_track = right[i]
		
		# Appending current track
		# seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)
		print(distance)
		# Increase the total count
		seek_count += distance

		# Accessed track is now new head
		head = cur_track

	# Once reached the right end
	# jump to the last track that
	# is needed to be serviced in
	# left direction
	seek_count += abs(head - left[0])
	head = left[0]

	# Now service the requests again
	# which are left
	for i in range(len(left)):
		cur_track = left[i]

		# Appending current track to
		# seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)
		print(distance)
		# Increase the total count
		seek_count += distance

		# Accessed track is now the new head
		head = cur_track

	print("Total number of seek operations =",
		seek_count)
	print("Seek Sequence is")

	for i in range(len(seek_sequence)):
		print(seek_sequence[i])

# Driver code


arr = []
for i in range(size):
    val = int(input("Enter the disk requests: "))
    arr.append(val)
head = int(input("Enter the head value: "))
print("  ")
print("Solution:")
print("  ")

print("Initial position of head:", head)
print("  ")
print("Distance is:")
CLOOK(arr, head)

