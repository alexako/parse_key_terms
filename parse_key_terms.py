from bs4 import BeautifulSoup
import sys


def get_wordlist(soup):
	return soup.find_all("div", "vtbegenerated")[0]
	
def parse_line(line):
	return (line.b.string[:-1],
		line.contents[1])

def build_wordlist(list):
	wordlist = {}
	wordlist[str(list.li.b.string)[:-1]] = str(list.contents[1])
	for line in list.li.find_next_siblings("li"):
		wordlist[parse_line(line)[0]] = parse_line(line)[1]
	
	return wordlist


if __name__ == '__main__':

	if len(sys.argv) > 1:
		file = sys.argv[1]
	else:
		file = raw_input("Enter filename: ")
	
	output_file = file.split(".")[0] + ".txt"
	
	wordlist = {}

	try:
		html = open(file)
	except:
		print "Couldn't open file"
		
	soup = BeautifulSoup(html, "lxml")
	
	unprocessed_list = get_wordlist(soup)
	
	wordlist = build_wordlist(unprocessed_list)
	
	with open(output_file, 'w+') as f:
		for key,value in wordlist.items():
			try:
				s = str(key) + ": " + value.encode('ascii', 'ignore')
				f.write(s + '\n')
				print s
			except:
				print "Encoding Error"
		
	
	