import csv
import os

File1 = "1970s_zoobooks/1979.txt"
File2 = "1970s_zoobooks/1970-79_Zoobooks.csv"
year = 1979

# Minor function to parse names out of the city data
def parse_data(datastring):
		if ". " in datastring:
			datastring = datastring.split(". ")
			city = datastring[-1]
			city = city.replace(",", "")
			return city
		elif ", " in datastring:
			datastring = datastring.replace(",", "", 1)
			datastring = datastring.split(",")
			if len(datastring) > 1:
				city = datastring[1]
			else:
				city = datastring[0].replace(",", "")
			return city
		else:
			return datastring
		


with open(File1, "r") as txt_file, open(File2, "a") as write_to:
	csv_writer = csv.writer(write_to, delimiter=',', skipinitialspace = True)

	state_list = ["Alaska", "Alabama", "Arkansas", "American Samoa",
	"Arizona", "California", "Colorado", "Connecticut", "Washington, D. C.", "Delaware", "Florida", "Georgia", "Guam",
	"Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas",
	"Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine",
	"Michigan", "Minnesota", "Missouri", "Mississippi", "Montana",
	"North Carolina", "North Dakota", "Dakota",
	"Nebraska", "New Hampshire", "New Jersey", 
	"New Mexico", "Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
	"Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island",
	"South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
	"Virginia", "Virgin Islands", "Vermont", "Washington",
	"Wisconsin", "West Virginia", "Wyoming"]

	# Split the text file into lines, put those lines in a list
	lines = txt_file.read().splitlines()


	for line in lines:

		state_found = False
		state_index = -1

		#search each row for a state
		for state in state_list:
			if not state_found:
				state_index = line.rfind(state)

				# If a state is found, add it and its data to the csv file
				if state_index > -1 and line[(state_index - 1)] != "(":
					state_found = True
					city_data = line[0:state_index]
					city = parse_data(city_data)
					csv_writer.writerow([city, state, "United States", year])

		# If a state was not found, then the line might contain a country
		if not state_found and len(line) > 1:

			# Filter for lines that have names in them (i.e., the second letter is uppercase)
			if line[1].isupper():

				# Split line by periods
				if ". " in line:
					line = line.split(".")

					# Split the second section of the line by commas
					if ", " in line[1]:
						city_and_country = line[1]
						city = city_and_country.split(",")[0]
						country = city_and_country.split(",")[1]

						# Write city and country into csv file
						csv_writer.writerow([city, "", country, year])

			# Lastly, we want to make sure that we catch floating cities and countries (i.e. not associated with a name on the scan)
			elif "." in line:
				line = line.split(".")
				if ", " in line[0]:
					line = line[0].split(",")
					city = line[0]
					country = line[1]
					csv_writer.writerow([city, "", country, year])





