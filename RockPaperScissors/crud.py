import csv;

class CRUD:
    # Add user
    def add(i):
        with open('data.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(i)
            
    def view():
        data = []
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    # remove user
    def remove(i):
        def save(j):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(j)
                
        new_list = []
        telephone = i
        
        with open('data.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                new_list.append(row)
                
                for element in row:
                    if element == telephone:
                        new_list.remove(row)
                        
        save(new_list)
        
    # update user
    def update(new_data, old_data):
        
        new_list = []
        index: int = 0
        print("OLD_DATA: ", old_data)
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                new_list.append(row)
                for element in row:
                    if element == old_data[0] or element == old_data[1]:
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
           

    def search(search_term):
        data = []
        
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for element in row:
                    if element == search_term:
                        data.append(row)
                        
        return data
    