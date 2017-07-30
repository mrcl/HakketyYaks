
def calc_approve( pool, area, age, group, amount, percent ):

	debug=False

	print("calculating results")

	approve=0.65
	decline=0.35

	approve *= list_pool[pool][0]
	decline *= list_pool[pool][1]

	approve *= list_area[area][0]
	decline *= list_area[area][1]

	approve *= list_age[age][0]
	decline *= list_age[age][1]

	approve *= list_group[group][0]
	decline *= list_group[group][1]

	approve *= list_amount[amount][0]
	decline *= list_amount[amount][1]

	approve *= list_percent[percent][0]
	decline *= list_percent[percent][1]

	result="Your grant application is likely to be "
	if (approve > decline):
		result+="approved. :D"
	else:
		result+="declined. =("

	if debug:
		result += " DEBUG: (" + str(approve) + " : " + str(decline) + ")"
	return result





list_pool={
    'Creative Communities Local Funding Scheme':(0.126,0.186),
    'Social And Recreation Fund':(0.114,0.164),
    'Betty Campbell Accommodation Assistance':(0.066,0.024),
    'Wellington Venue Subsidy':(0.063,0.028),
    'Built Heritage Incentive Fund':(0.060,0.029),
    'C H Izard Bequest':(0.020,0.068),
    'Our Living City Fund':(0.038,0.033),
    'Community Events Sponsorship':(0.014,0.026),
    'Wellington Regional Amenities Fund':(0.005,0.018),
    'General Grants':(0.189,0.111),
    'Arts And Culture Fund':(0.147,0.208)
}

list_area={
    'TeAro':(0.067,0.089),
    'Newtown':(0.063,0.090),
    'Tawa':(0.045,0.044),
    'Miramar':(0.040,0.036),
    'AroValley-Highbury':(0.033,0.042),
    'Kilbirnie':(0.028,0.039),
    'IslandBay-OwhiroBay':(0.031,0.031),
    'Karori':(0.030,0.033),
    'Kelburn':(0.013,0.033),
    'All':(0.192,0.135),
    'WellingtonCBD':(0.444,0.566)
}

list_age={
    'Seniors':(0.011,0.019),
    'Youth':(0.100,0.168),
    'Children':(0.057,0.079),
    'All':(0.831,0.734)
}

list_group={
    'Youth/Students/School':(0.041,0.035),
    'Children':(0.007,0.034),
    'Women':(0.014,0.011),
    'Families':(0.005,0.037),
    'Residents':(0.013,0.001),
    'Maori/Pacific':(0.030,0.026),
    'Arts':(0.008,0.001),
    'Parents':(0.001,0.017),
    'New Zealand':(0.006,0.001),
    'Disabilities':(0.01,0.026),
    'Refugees':(0.011,0.003),
    'Community/People':(0.756,0.653)
}

list_amount={
	'>100000':(0.145,0.080),
	'<=1000000':(0.113,0.084),
	'<=500000':(0.306,0.322),
	'<=10000':(0.143,0.185),
	'<=5000':(0.264,0.322),

}

list_percent={
    '<=10':(0.109,0.111),
    '<=20':(0.124,0.103),
    '<=30':(0.124,0.082),
    '<=40':(0.088,0.080),
    '<=50':(0.079,0.071),
    '<=60':(0.058,0.055),
    '<=70':(0.055,0.043),
    '<=80':(0.050,0.069),
    '<=90':(0.040,0.051),
    '<=100':(0.242,0.328)
}
