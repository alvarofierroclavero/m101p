use m101
db.zips.aggregate([
    {$match:
        {$or:
            [{state:'CA'}, {state:'NY'}]
        }
    },
    {$group:
        {
            _id:{city:'$city', state:'$state'},
            population:{$sum:'$pop'}
        }
    },
    {$match:
        {
            population:{$gt:25000}
        }
    },
    {$group:
        {
            _id: null,
            avg:{ $avg: '$population' }
        }
    }
])