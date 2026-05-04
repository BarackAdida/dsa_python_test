# def check_membership():
#     fruits = ["mangoes", "apples", "oranges"]
    
#     print ("is applein list?", "apple" in fruits)
    
# check_membership()

# def sort_list():
#     numbers = [10,3,5,1,7,9,5,7]
    
#     numbers.sort()
#     num_ordered = sorted(numbers)
    
#     print(num_ordered)
    
#     print("sorted list:", numbers)
    
# sort_list()

# def mordify_values():
#     student = {
#         "name": "Barack",
#         "age": 21
#     }
#     student["age"] = 20
    
#     print(student)
    
#     student.update({"age" : 19})
    
#     print(student)
    
# mordify_values()

# def create_tuple():
#     numbers = (1,2,3,4,5)
    
#     print("created tuple:", numbers)
    
# create_tuple()

# def loop_tuple():
#     fruits = ("mango", "Orange", "pineapple")
    
#     for fruit in fruits:
#         print(fruit)
# loop_tuple()

def remove_elements():
    numbers = {1, 2, 3, 4, 6}
    
    numbers.remove(3)
    print(numbers)
    numbers.discard(2)
    print(numbers)
    popped = numbers.pop()
    print(popped)
    
remove_elements()

def dictionary():
    student = {
        "name": "Barack",
        "age": 20,
        "course": "ICS" 
    }
    
    print(student)
    
    print("name:", student["name"])
    # print("age:" get.student["age"])
    for values in student.values():
        print(values)
        
    student.clear()
    print("after clear:", student)
    
dictionary()

if __name__ == "__main__":
    main()