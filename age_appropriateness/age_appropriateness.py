from decimal import *

age = float(raw_input('Age in question? '))

def appropriateness(age):
	lower_bound = (.5 * age) + 7
	upper_bound = (age - 7) * 2

	#tests to see if the resulting lower bounds are whole numbers. if not, makes them display without too many zeros
	if int(upper_bound) == upper_bound and int(lower_bound) == lower_bound:
		print "Your lower bound is %d and your upper bound is %d" %	(lower_bound, upper_bound)

	else:
		#sets the precision of the decimal lower
		getcontext().prec = 1
		print "Your lower bound is %s and your upper bound is %s" %	(Decimal(lower_bound), Decimal(upper_bound))

appropriateness(age)