class dog:

    species = "dog"

    def __init__(self,name,breed):

        self.name = name
        self.breed = breed

rosy = dog("rosy","chocolet lab")
felix = dog("felix","golden retriver")

print("{} is a {} ".format(rosy.name, rosy.breed))
print("{} is a {} ".format(felix.name, felix.breed))