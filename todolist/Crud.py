import csv;

class CRUD():

    def __init__(self):
        self.tasks = []

    # create task
    def add(todo):
        with open('data.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(todo)

        # create task
    def edit(new_data, old_task):
        new_list= []
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                new_list.append(row)
                for element in row:
                    if element == old_task:
                        index = new_list.index(row)
                        new_list[index] = new_data
                        
        filename = "data.csv"
        open(filename, "w+")
        
        with open('data.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
        
            if len(new_list) > 2:
                for item in new_list:
                    data = [item]
                    writer.writerows(data)
                
            else:
                writer.writerows(new_list)
    # read task
    def view():
        data = []
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    # delete task
    def remove(param):
        def save(item):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(item)
                
        new_list = []
        task = param
        
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                new_list.append(row)
                
                for element in row:
                    if element == task:
                        new_list.remove(row)
                        
        save(new_list)
