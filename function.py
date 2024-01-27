print("for testing");
filepath = 'todos.txt'


def get_todo(filep = filepath):
    with open(filep, 'r') as file_local:
        todos_local = file_local.readlines();
        return todos_local;


def write_todo(todos_arg, filep = filepath):
    with open(filep, 'w') as file_local:
        file_local.writelines(todos_arg);


if __name__ == "__main__":
    import time

    print(time.strftime("%A"))
    print("for testing");
    print(get_todo("todos.txt"));

    temperature = float(input());


    def water_state(temperature):
        if temperature <= 0:
            return "solid";
        if temperature > 0 and temperature < 100:
            return "Liquid";
        elif temperature > 100:
            return "gas";


    print(water_state(temperature))
