import random 

data={
    "case1":{
        "user1":"jack",
        "socialapp":"snapchat",
        "age":17,
    },
    "case2":{
        "user2":"vannesa",
        "scoial":"snapchat",
        "age":16,
    }
}

def id():
    try:
        random_case_key= random.choice(list(data.keys()))
        print(f"random case {random_case_key}")

        inner_dict=data[random_case_key]

        random_inner_key, random_inner_value = random.choice(list(inner_dict.items()))
        print(f"Random key: {random_inner_key}, Random value: {random_inner_value}")
        
    except Exception as e:  # Catch any exception
        print(f"An error occurred: {e}")
id()
    
        