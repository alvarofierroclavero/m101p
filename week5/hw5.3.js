/*
Sample data:
{
    "_id" : ObjectId("50b59cd75bed76f46522c34e"),
    "class_id" : 2,
    "student_id" : 0,
    "scores" : [
        {
            "score" : 57.92947112575566,
            "type" : "exam"
        },
        {
            "score" : 21.24542588206755,
            "type" : "quiz"
        },
        {
            "score" : 68.1956781058743,
            "type" : "homework"
        },
        {
            "score" : 67.95019716560351,
            "type" : "homework"
        },
        {
            "score" : 18.81037253352722,
            "type" : "homework"
        }
    ]
}
*/
use m101
db.grades.aggregate([
    {$unwind:
        '$scores'
    },
    {$match:
        {$or:
            [{"scores.type":'exam'}, {"scores.type":'homework'}]
        }
    },
    {$group:
        {
            _id:{student_id:"$student_id", class_id:"$class_id"},
            average_student:{$avg:'$scores.score'}
        }
    },
    {$group:
        {
            _id:"$_id.class_id",
            average_class:{$avg:'$average_student'}
        }
    },
    {$sort:
        {
            average_class:1
        }
    },
    {$limit:1}
])