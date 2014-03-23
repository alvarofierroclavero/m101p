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
            _id: {'from-address3':'$headers.From', 'to-address3':'$headers.To'},
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