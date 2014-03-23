use enron
db.messages.aggregate([
    {$unwind:
        '$headers.To'
    },
    /*{$match:
        {
            'headers.Message-ID': '<1742192.1075843563490.JavaMail.evans@thyme>'
        }
    },*/
    {$project:
        {
            _id: '$_id',
            headers: '$headers',
            mailbox: '$mailbox'
        }
    },
    {$group:
        {
            _id: {'first-pass': '$_id', 'from-address':'$headers.From', 'to-address':'$headers.To'}
        }
    },
    {$project:
        {
            _id: '$_id.first-pass',
            'from-address2': '$_id.from-address',
            'to-address2': '$_id.to-address'
        }
    },
    {$group:
        {
            _id: {'from-address3':'$from-address2', 'to-address3':'$to-address2'},
            sum: {$sum:1}
        }
    },
    {$sort:
        {
            'sum':-1
        }
    },
    {$limit:5}
])