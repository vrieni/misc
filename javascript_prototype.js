function Parentclass(){
    this.property1= "Hola";
    this.parentmethod1 = function parentmethod1(arg1){
        return arg1+ "Parent method 1 return data ....";
    }
}
//javascript prototypal inheritance


function Childclass(){
    this.property1= "Adios";
    this.childmethod1 = function childmethod1(arg1){
        return arg1+ "Child method 1 return data ....";
    }
}

Childclass.prototype = new Parentclass();

var instance1 = new Childclass();

console.log(instance1 instanceof Parentclass);
console.log(instance1 instanceof Childclass);


console.log(instance1.parentmethod1("RESULT"));


console.log(instance1.childmethod1("RESULT"));

Childclass.prototype.parentmethod1 = function parentmethod1(arg1){
    return arg1+" I have overriden Parent method 1";
}

console.log(instance1.parentmethod1("RESULT: "));


console.log(instance1.property1);
console.log(instance1.property1);






