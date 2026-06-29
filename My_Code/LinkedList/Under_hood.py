head = {
    "value" : 12,
    "next" : {
        "value" : 23,
        "next" :{

            "value" : 22,
            "next" :{

                "value" : 24,
                "next" :None
            }
        }
    }
}
print(head["next"]["next"]["value"])