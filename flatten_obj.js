//flatten a js object

data = {'key1':1, 'key2':arr, 'key3': 3, 'key4': {'hi':1, 'hello':2, 'yes':3, 'no':4}, 'key5': 'string', 'key6':6, 'key7':'key7'};

function print_all(obj) {
    for (var key in obj){
        if (obj[key] instanceof Object){
            print_all(obj[key]);
        } else {
            console.log(obj[key]);
        }
    }
}


print_all(data);
