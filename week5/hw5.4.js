use m101
db.zips.aggregate([
	{$project:
		{
			first_char: {$substr : ['$city',0,1]},
			population: '$pop',
			city: '$city'
		}
	},
	{$match:
		{
			first_char: {'$regex':'[0-9]'}
		}
	},
	{$group:
		{
			_id: null,
			total_population:{'$sum':'$population'}
		}
	}
])