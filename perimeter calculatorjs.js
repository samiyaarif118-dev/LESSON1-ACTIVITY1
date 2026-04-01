var choice = prompt("Welcome to perimeter calculator. \n please enter your choice.\na. Perimeter of Rectangle. \nb.Perimeter of Triangle \nc.Perimeter of Circle \nd.Perimeter of Parellelogram");
if (choice == 'a') {
    var a = prompt('Enter the Length')
    var b = prompt('Enter the Breadth')
    var result = 2 * (Number(a) + Number(b))
    alert('The Perimeter is ' + result)
}
if (choice == 'b') {
    var a = prompt('Enter the height')
    var b = prompt('Enter the base')
    var result = Number(a) * Number(b) / 2
    alert('The Perimeter is ' + result)
}
if (choice == 'c') {
    var a = prompt('Enter the radius')
    var result = 2 * 3.14 * Number(a)
    alert('The Perimeter is ' + result)
}
if (choice == 'd') {
    var a = prompt('Enter the height')
    var b = prompt('Enter the corresponding base')
    var result = 2 * (Number(a) + Number(b))
    alert('The Perimeter is ' + result)
}