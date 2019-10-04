#!/usr/bin/env python3

import searchmodes
import resources
import sys
from termcolor import colored

def main():
	if resources.options().version:
		resources.version()
		sys.exit(0)

	elif resources.options().keywords or resources.options().file \
	and not resources.options().createsubs:
		if not resources.options().domain:
			print(colored("\nDomain needed to parse subs against!", "red"))
			sys.exit(1)

		else:
			resources.title()
			searchmodes.generate_sub_keywords()


	elif resources.options().createsubs:
		if not resources.options().domain:
			print(colored("\nDomain needed to parse subs against!", "red"))
			sys.exit(1)

		elif not resources.options().file:
			print(colored("\nA file is needed to parse subs against!", "red"))
			sys.exit(1)

		else:
			resources.title()
			searchmodes.create()

	elif not resources.options().createsubs or resources.options().keywords \
	or resources.options().file:
		if not resources.options().domain:
			print(colored("\nDomain needed!", "red"))
			sys.exit(1)
		else:
			resources.title()
			searchmodes.crtsh()
			searchmodes.certspotter()
			searchmodes.certdb()
			searchmodes.censys()

if __name__ == "__main__":
	main()
